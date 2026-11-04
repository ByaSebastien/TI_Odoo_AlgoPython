"""PyBooks : le menu de la librairie, de l'accueil jusqu'à la sortie."""

from decimal import ROUND_HALF_UP, Decimal

# --- Constantes de la boutique ---
SHOP_NAME = "PyBooks"
FREE_SHIPPING_THRESHOLD = Decimal("50")
CATALOG_SIZE = 1200
SHIPPING_DELAY_HOURS = 48
BOOK_VAT_RATE = Decimal("0.06")
SHIPPING_FEE = Decimal("4.90")
CENT = Decimal("0.01")

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
print("========================================")
print(f"       {SHOP_NAME} - Librairie en ligne")
print("========================================")
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
    print("Q. Quitter")
    choice = input("Votre choix : ")

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
            # Choix du format, redemandé tant qu'il n'est pas valide.
            is_ebook = False
            while True:
                format_choice = input("Format : (p)apier ou (n)umérique ? ")
                match format_choice:
                    case "p" | "P":
                        is_ebook = False
                        break
                    case "n" | "N":
                        is_ebook = True
                        break
                    case _:
                        print(f"Format inconnu : {format_choice!r}.")

            if not is_ebook and stock == 0:
                print("Rupture de stock : choisissez la version numérique.")
                continue

            # Quantité, redemandée tant qu'elle n'est pas valide.
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
                shipping_label = "sans objet (téléchargement)"
            elif amount_incl_vat >= FREE_SHIPPING_THRESHOLD:
                shipping = Decimal(0)
                shipping_label = "offerts"
            else:
                shipping = SHIPPING_FEE
                shipping_label = f"{SHIPPING_FEE:.2f} €"

            total_to_pay = amount_incl_vat + shipping

            print()
            print("--- Votre commande ---")
            print(f"Format        : {'numérique' if is_ebook else 'papier'}")
            print(f"Montant HT    : {amount_excl_vat:.2f} €")
            print(f"TVA ({BOOK_VAT_RATE * 100:.0f} %)     : {vat:.2f} €")
            print(f"Montant TTC   : {amount_incl_vat:.2f} €")
            print(f"Frais de port : {shipping_label}")
            print(f"Total à payer : {total_to_pay:.2f} €")

            # Mise à jour du stock et des statistiques de la session.
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

        case "q" | "Q":
            break

        case _:
            print(f"Choix inconnu : {choice!r}.")

print()
print(f"Merci de votre visite ! {orders_count} commande(s), {session_total:.2f} €.")
