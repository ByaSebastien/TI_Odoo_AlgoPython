"""PyBooks : présente le livre du jour et applique les règles de la boutique."""

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
print()

# --- Fiche du livre ---
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
print()

# --- Choix du format ---
format_choice = input("Format : (p)apier ou (n)umérique ? ")
is_valid_format = True
is_ebook = False
match format_choice:
    case "p" | "P":
        is_ebook = False
    case "n" | "N":
        is_ebook = True
    case _:
        is_valid_format = False

if not is_valid_format:
    print(f"Format inconnu : {format_choice!r}. Commande annulée.")
else:
    quantity = int(input("Combien d'exemplaires souhaitez-vous ? "))

    if quantity <= 0:
        print("La quantité doit être au moins égale à 1. Commande annulée.")
    elif not is_ebook and quantity > stock:
        print(f"Stock insuffisant : {stock} exemplaire(s) disponible(s).")
    else:
        unit_price = ebook_price if is_ebook else paper_price
        amount_excl_vat = unit_price * quantity
        vat = (amount_excl_vat * BOOK_VAT_RATE).quantize(CENT, rounding=ROUND_HALF_UP)
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
