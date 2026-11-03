"""PyBooks : accueille le client et présente le livre du jour."""

# --- Constantes de la boutique ---
SHOP_NAME = "PyBooks"
FREE_SHIPPING_THRESHOLD = 50
CATALOG_SIZE = 1200
SHIPPING_DELAY_HOURS = 48

# --- Livre du jour ---
title = "Le Petit Prince"
author = "Antoine de Saint-Exupéry"
isbn = "9782070612758"
unit_price = 7.50
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
print(f"Prix HT  : {unit_price:.2f} €")
print(f"En stock : {stock} exemplaire(s)")
print()

# --- Commande ---
quantity = int(input("Combien d'exemplaires souhaitez-vous ? "))
amount_excl_vat = unit_price * quantity
print(f"Montant HT : {amount_excl_vat:.2f} €")
