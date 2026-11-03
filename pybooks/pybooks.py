"""PyBooks : présente le livre du jour et calcule le montant de la commande."""

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
unit_price = Decimal("7.50")
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
unit_price_incl_vat = (unit_price * (1 + BOOK_VAT_RATE)).quantize(
    CENT, rounding=ROUND_HALF_UP
)
print("--- Livre du jour ---")
print(f"Titre    : {title}")
print(f"Auteur   : {author}")
print(f"ISBN     : {isbn}")
print(f"Prix HT  : {unit_price:.2f} €")
print(f"Prix TTC : {unit_price_incl_vat:.2f} €")
print(f"En stock : {stock} exemplaire(s)")
print()

# --- Commande ---
quantity = int(input("Combien d'exemplaires souhaitez-vous ? "))

amount_excl_vat = unit_price * quantity
vat = (amount_excl_vat * BOOK_VAT_RATE).quantize(CENT, rounding=ROUND_HALF_UP)
amount_incl_vat = amount_excl_vat + vat
# Pour l'instant, les frais de port sont toujours facturés (gratuité : étape 03).
total_to_pay = amount_incl_vat + SHIPPING_FEE

print()
print("--- Votre commande ---")
print(f"Montant HT    : {amount_excl_vat:.2f} €")
print(f"TVA ({BOOK_VAT_RATE * 100:.0f} %)     : {vat:.2f} €")
print(f"Montant TTC   : {amount_incl_vat:.2f} €")
print(f"Frais de port : {SHIPPING_FEE:.2f} €")
print(f"Total à payer : {total_to_pay:.2f} €")
