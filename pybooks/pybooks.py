"""PyBooks : catalogue de plusieurs livres, panier et ticket de caisse."""

from decimal import ROUND_HALF_UP, Decimal

# --- Constantes de la boutique ---
SHOP_NAME = "PyBooks"
FREE_SHIPPING_THRESHOLD = Decimal("50")
SHIPPING_DELAY_HOURS = 48
BOOK_VAT_RATE = Decimal("0.06")
SHIPPING_FEE = Decimal("4.90")
EBOOK_DISCOUNT = Decimal("0.20")
CENT = Decimal("0.01")

# --- Constantes de mise en forme ---
TICKET_WIDTH = 40
LABEL_WIDTH = 20
DETAIL_WIDTH = 10
AMOUNT_WIDTH = TICKET_WIDTH - LABEL_WIDTH - DETAIL_WIDTH - 2  # 2 : place de « € »
SEPARATOR = "-" * TICKET_WIDTH

# --- Constantes ISBN-13 ---
ISBN_LENGTH = 13
ISBN_ODD_POSITION_WEIGHT = 3

# --- Catalogue : (isbn, titre, auteur, prix papier HT) ---
catalog = [
    ("9782070612758", "Le Petit Prince", "Antoine de Saint-Exupéry", Decimal("7.50")),
    ("9782070360024", "L'Étranger", "Albert Camus", Decimal("6.90")),
    ("9782253004899", "Les Misérables (tome 1)", "Victor Hugo", Decimal("9.20")),
    ("9782266320320", "Dune", "Frank Herbert", Decimal("12.50")),
    ("9782253001409", "Le Comte de Monte-Cristo", "Alexandre Dumas", Decimal("11.90")),
]
# Stocks des livres papier, dans le même ordre que le catalogue.
stocks = [7, 3, 0, 12, 5]

# --- Panier : lignes (indice du livre dans le catalogue, ebook ?, quantité) ---
cart: list[tuple[int, bool, int]] = []

# --- Statistiques de la session ---
orders_count = 0
session_total = Decimal(0)

# --- Bannière ---
print("=" * TICKET_WIDTH)
print(f"{SHOP_NAME + ' - Librairie en ligne':^{TICKET_WIDTH}}")
print("=" * TICKET_WIDTH)
print(f"{len(catalog)} titres, en papier et en numérique.")
print(f"Livraison offerte dès {FREE_SHIPPING_THRESHOLD} € de livres papier.")
print(f"Ebooks : {EBOOK_DISCOUNT * 100:.0f} % moins chers que le papier.")

# --- Menu principal ---
while True:
    print()
    print("=== Menu ===")
    print("1. Catalogue")
    print("2. Ajouter au panier")
    print(f"3. Voir le panier ({len(cart)} ligne(s))")
    print("4. Valider la commande")
    print("5. Vider le panier")
    print("6. Vérifier un ISBN")
    print("Q. Quitter")
    choice = input("Votre choix : ").strip().lower()

    match choice:
        case "1":
            order = input("Trier par (t)itre ou par (p)rix ? ").strip().lower()
            # On trie des tuples (clé de tri, indice) : sorted compare d'abord
            # le premier élément, puis le second en cas d'égalité.
            sort_keys: list[tuple[str | Decimal, int]] = []
            for index, (_isbn, book_title, _author, paper_price) in enumerate(catalog):
                if order == "p":
                    sort_keys.append((paper_price, index))
                else:
                    sort_keys.append((book_title.lower(), index))

            print()
            for _key, index in sorted(sort_keys):
                isbn, book_title, author, paper_price = catalog[index]
                stock_label = (
                    f"{stocks[index]} en stock" if stocks[index] else "rupture"
                )
                print(f"{index + 1}. {book_title} - {author}")
                print(f"   {paper_price:.2f} € HT ({stock_label}), ISBN {isbn}")

        case "2":
            raw_number = input(f"Numéro du livre (1 à {len(catalog)}) : ").strip()
            if not raw_number.isdecimal() or not 1 <= int(raw_number) <= len(catalog):
                print("Numéro inconnu.")
                continue
            book_index = int(raw_number) - 1
            book_title = catalog[book_index][1]

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

            if not is_ebook and stocks[book_index] == 0:
                print("Rupture de stock : choisissez la version numérique.")
                continue

            quantity = int(input("Quantité : "))
            while quantity < 1 or (not is_ebook and quantity > stocks[book_index]):
                if quantity < 1:
                    print("La quantité doit être au moins égale à 1.")
                else:
                    print(f"Stock insuffisant : {stocks[book_index]} disponible(s).")
                quantity = int(input("Quantité : "))

            cart.append((book_index, is_ebook, quantity))
            # Les exemplaires papier sont réservés dès l'ajout au panier.
            if not is_ebook:
                stocks[book_index] -= quantity
            print(f"Ajouté : {quantity} x {book_title}.")

        case "3":
            if not cart:
                print("Votre panier est vide.")
            for line_number, (book_index, is_ebook, quantity) in enumerate(cart, 1):
                book_format = "ebook" if is_ebook else "papier"
                line_title = catalog[book_index][1]
                print(f"{line_number}. {line_title} ({book_format}) x {quantity}")

        case "4":
            if not cart:
                print("Votre panier est vide.")
                continue

            # --- Calcul et ticket de caisse ---
            total_excl_vat = Decimal(0)
            paper_excl_vat = Decimal(0)
            print()
            print(SEPARATOR)
            for book_index, is_ebook, quantity in cart:
                book_title = catalog[book_index][1]
                paper_price = catalog[book_index][3]
                if is_ebook:
                    unit_price = (paper_price * (1 - EBOOK_DISCOUNT)).quantize(
                        CENT, rounding=ROUND_HALF_UP
                    )
                else:
                    unit_price = paper_price
                line_total = unit_price * quantity
                total_excl_vat += line_total
                if not is_ebook:
                    paper_excl_vat += line_total

                label = ("[e] " if is_ebook else "") + book_title
                detail = f"{quantity} x {unit_price:.2f}"
                print(
                    f"{label[:LABEL_WIDTH]:<{LABEL_WIDTH}}{detail:>{DETAIL_WIDTH}}"
                    f"{line_total:>{AMOUNT_WIDTH}.2f} €"
                )

            vat = (total_excl_vat * BOOK_VAT_RATE).quantize(
                CENT, rounding=ROUND_HALF_UP
            )
            total_incl_vat = total_excl_vat + vat
            paper_incl_vat = paper_excl_vat * (1 + BOOK_VAT_RATE)

            if paper_excl_vat == 0:
                shipping = Decimal(0)
                shipping_label = "sans objet"
            elif paper_incl_vat >= FREE_SHIPPING_THRESHOLD:
                shipping = Decimal(0)
                shipping_label = "offerts"
            else:
                shipping = SHIPPING_FEE
                shipping_label = f"{SHIPPING_FEE:.2f} €"
            total_to_pay = total_incl_vat + shipping

            summary_width = LABEL_WIDTH + DETAIL_WIDTH
            vat_label = f"TVA ({BOOK_VAT_RATE * 100:.0f} %)"
            print(SEPARATOR)
            print(
                f"{'Montant HT':<{summary_width}}{total_excl_vat:>{AMOUNT_WIDTH}.2f} €"
            )
            print(f"{vat_label:<{summary_width}}{vat:>{AMOUNT_WIDTH}.2f} €")
            print(
                f"{'Montant TTC':<{summary_width}}{total_incl_vat:>{AMOUNT_WIDTH}.2f} €"
            )
            shipping_width = AMOUNT_WIDTH + 2
            print(
                f"{'Frais de port':<{summary_width}}{shipping_label:>{shipping_width}}"
            )
            print(SEPARATOR)
            print(
                f"{'TOTAL À PAYER':<{summary_width}}{total_to_pay:>{AMOUNT_WIDTH}.2f} €"
            )
            print(SEPARATOR)

            confirmation = input("Confirmer la commande ? (o/n) ").strip().lower()
            if confirmation in ("o", "oui"):
                orders_count += 1
                session_total += total_to_pay
                cart.clear()
                print("Commande validée. Merci !")
            else:
                print("Commande non validée : votre panier est conservé.")

        case "5":
            # Les exemplaires papier réservés retournent en stock.
            for book_index, is_ebook, quantity in cart:
                if not is_ebook:
                    stocks[book_index] += quantity
            cart.clear()
            print("Panier vidé.")

        case "6":
            raw_isbn = input("ISBN à vérifier : ")
            candidate = raw_isbn.strip().replace("-", "").replace(" ", "")
            if len(candidate) != ISBN_LENGTH:
                print(
                    f"Un ISBN-13 compte {ISBN_LENGTH} chiffres, pas {len(candidate)}."
                )
            elif not candidate.isdecimal():
                print("Un ISBN-13 ne contient que des chiffres (et des tirets).")
            else:
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
