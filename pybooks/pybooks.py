"""PyBooks : menu de la librairie, vérification d'ISBN et ticket de caisse."""

from decimal import ROUND_HALF_UP, Decimal

# --- Constantes de la boutique ---
SHOP_NAME = "PyBooks"
FREE_SHIPPING_THRESHOLD = Decimal("50")
CATALOG_SIZE = 1200
SHIPPING_DELAY_HOURS = 48
BOOK_VAT_RATE = Decimal("0.06")
SHIPPING_FEE = Decimal("4.90")
CENT = Decimal("0.01")

# --- Constantes de mise en forme ---
TICKET_WIDTH = 40
LABEL_WIDTH = 28
VALUE_WIDTH = TICKET_WIDTH - LABEL_WIDTH
AMOUNT_WIDTH = VALUE_WIDTH - 2  # place laissée pour « € »
SEPARATOR = "-" * TICKET_WIDTH

# --- Constantes ISBN-13 ---
ISBN_LENGTH = 13
ISBN_ODD_POSITION_WEIGHT = 3

# --- Livre du jour ---
title = "Le Petit Prince"
author = "Antoine de Saint-Exupéry"
isbn = "9782070612758"
paper_price = Decimal("7.50")
ebook_price = Decimal("5.99")
stock = 7

# --- Statistiques de la session ---
orders_count = 0
session_total = Decimal(0)

# --- Bannière ---
print("=" * TICKET_WIDTH)
print(f"{SHOP_NAME + ' - Librairie en ligne':^{TICKET_WIDTH}}")
print("=" * TICKET_WIDTH)
print("Bienvenue !")
print("Livres, ebooks et cadeaux pour lecteurs curieux.")
print()
print("Nos engagements :")
print(f"- Livraison offerte dès {FREE_SHIPPING_THRESHOLD} € d'achat")
print(f"- Plus de {CATALOG_SIZE} titres en stock")
print(f"- Expédition sous {SHIPPING_DELAY_HOURS} heures")

# --- Menu principal ---
while True:
    print()
    print("=== Menu ===")
    print("1. Voir le livre du jour")
    print("2. Commander")
    print("3. Récapitulatif de la session")
    print("4. Vérifier un ISBN")
    print("Q. Quitter")
    choice = input("Votre choix : ").strip().lower()

    match choice:
        case "1":
            print()
            print("--- Livre du jour ---")
            print(f"Titre    : {title}")
            print(f"Auteur   : {author}")
            print(f"ISBN     : {isbn}")
            print(f"Papier   : {paper_price:.2f} € HT")
            print(f"Ebook    : {ebook_price:.2f} € HT")
            if stock > 0:
                print(f"En stock : {stock} exemplaire(s)")
            else:
                print("En stock : rupture (l'ebook reste disponible)")

        case "2":
            is_ebook = False
            while True:
                format_choice = input("Format : (p)apier ou (n)umérique ? ")
                match format_choice.strip().lower():
                    case "p":
                        is_ebook = False
                        break
                    case "n":
                        is_ebook = True
                        break
                    case _:
                        print(f"Format inconnu : {format_choice!r}.")

            if not is_ebook and stock == 0:
                print("Rupture de stock : choisissez la version numérique.")
                continue

            quantity = int(input("Combien d'exemplaires souhaitez-vous ? "))
            while quantity < 1 or (not is_ebook and quantity > stock):
                if quantity < 1:
                    print("La quantité doit être au moins égale à 1.")
                else:
                    print(f"Stock insuffisant : {stock} exemplaire(s) disponible(s).")
                quantity = int(input("Combien d'exemplaires souhaitez-vous ? "))

            unit_price = ebook_price if is_ebook else paper_price
            amount_excl_vat = unit_price * quantity
            vat = (amount_excl_vat * BOOK_VAT_RATE).quantize(
                CENT, rounding=ROUND_HALF_UP
            )
            amount_incl_vat = amount_excl_vat + vat

            if is_ebook:
                shipping = Decimal(0)
                shipping_label = "sans objet"
            elif amount_incl_vat >= FREE_SHIPPING_THRESHOLD:
                shipping = Decimal(0)
                shipping_label = "offerts"
            else:
                shipping = SHIPPING_FEE
                shipping_label = f"{SHIPPING_FEE:.2f} €"

            total_to_pay = amount_incl_vat + shipping

            # --- Ticket de caisse ---
            item_label = f"{title} ({'ebook' if is_ebook else 'papier'})"
            print()
            print(SEPARATOR)
            item_detail = f"{quantity} x {unit_price:.2f} €"
            print(f"{item_label:<{LABEL_WIDTH}}{item_detail:>{VALUE_WIDTH}}")
            print(SEPARATOR)
            print(
                f"{'Montant HT':<{LABEL_WIDTH}}{amount_excl_vat:>{AMOUNT_WIDTH}.2f} €"
            )
            vat_label = f"TVA ({BOOK_VAT_RATE * 100:.0f} %)"
            print(f"{vat_label:<{LABEL_WIDTH}}{vat:>{AMOUNT_WIDTH}.2f} €")
            print(
                f"{'Montant TTC':<{LABEL_WIDTH}}{amount_incl_vat:>{AMOUNT_WIDTH}.2f} €"
            )
            print(f"{'Frais de port':<{LABEL_WIDTH}}{shipping_label:>{VALUE_WIDTH}}")
            print(SEPARATOR)
            print(
                f"{'TOTAL À PAYER':<{LABEL_WIDTH}}{total_to_pay:>{AMOUNT_WIDTH}.2f} €"
            )
            print(SEPARATOR)

            if not is_ebook:
                stock -= quantity
            orders_count += 1
            session_total += total_to_pay

        case "3":
            print()
            print("--- Récapitulatif de la session ---")
            print(f"Commandes passées : {orders_count}")
            print(f"Montant total     : {session_total:.2f} €")
            print(f"Stock restant     : {stock} exemplaire(s)")

        case "4":
            raw_isbn = input("ISBN à vérifier : ")
            candidate = raw_isbn.strip().replace("-", "").replace(" ", "")

            if len(candidate) != ISBN_LENGTH:
                print(
                    f"Un ISBN-13 compte {ISBN_LENGTH} chiffres, pas {len(candidate)}."
                )
            elif not candidate.isdecimal():
                print("Un ISBN-13 ne contient que des chiffres (et des tirets).")
            else:
                # Pondérations 1, 3, 1, 3… sur les 12 premiers chiffres.
                weighted_sum = 0
                for index in range(ISBN_LENGTH - 1):
                    weight = 1 if index % 2 == 0 else ISBN_ODD_POSITION_WEIGHT
                    weighted_sum += int(candidate[index]) * weight
                expected_check = (10 - weighted_sum % 10) % 10

                if int(candidate[-1]) == expected_check:
                    print(f"ISBN {candidate} valide.")
                else:
                    print(
                        f"ISBN {candidate} invalide : la clé de contrôle "
                        f"devrait être {expected_check}."
                    )

        case "q":
            break

        case _:
            print(f"Choix inconnu : {choice!r}.")

print()
print(f"Merci de votre visite ! {orders_count} commande(s), {session_total:.2f} €.")
