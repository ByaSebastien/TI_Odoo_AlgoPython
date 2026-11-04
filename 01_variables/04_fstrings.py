"""Afficher proprement : f-strings, deux décimales, sep et end."""

title = "Le Petit Prince"
price = 12.9
quantity = 3

# Une f-string remplace chaque {expression} par sa valeur.
print(f"Livre : {title}")
print(f"{quantity} exemplaires de {title}")

# On peut calculer à l'intérieur des accolades.
print(f"Total : {price * quantity} €")

# :.2f affiche le nombre avec exactement deux décimales (arrondi pour l'affichage).
print(f"Prix unitaire : {price:.2f} €")
print(f"Total : {price * quantity:.2f} €")
print(f"Un tiers : {1 / 3:.2f}")

# La variable n'a pas été modifiée par l'affichage.
print("Valeur réelle de price :", price)

# Sans le f, les accolades sont affichées telles quelles.
print("Prix : {price}")

# sep remplace l'espace entre les éléments, end remplace le retour à la ligne.
print("Titre", "Auteur", "Prix", sep=" | ")
print("Chargement", end="...")
print("terminé")
