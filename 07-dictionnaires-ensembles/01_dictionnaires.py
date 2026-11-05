"""Le dictionnaire : retrouver une valeur par sa clé."""

# Clé : le titre ; valeur : le nombre d'exemplaires en stock.
stocks = {
    "Le Petit Prince": 7,
    "L'Étranger": 3,
    "Dune": 12,
}
print("Dictionnaire :", stocks)

# Lire une valeur par sa clé.
print("Stock de Dune :", stocks["Dune"])

# get : une valeur par défaut si la clé est absente (au lieu d'une KeyError).
print("Stock d'Ulysse (get) :", stocks.get("Ulysse", 0))
print("Ulysse est-il référencé ?", "Ulysse" in stocks)

# Ajouter une clé, modifier une valeur.
stocks["Ulysse"] = 2
stocks["Dune"] -= 1
print("Après ajout et vente :", stocks)

# Une clé est unique : réaffecter remplace la valeur.
stocks["L'Étranger"] = 10
print("Après réapprovisionnement :", stocks)

# Supprimer : pop renvoie la valeur supprimée.
removed_stock = stocks.pop("Ulysse")
print(f"Ulysse retiré (il en restait {removed_stock}) :", stocks)

# in teste les CLÉS, pas les valeurs (le vérificateur de types du module 13
# signale ce test toujours faux ; « type: ignore » le fait taire ici).
print("'Dune' in stocks         :", "Dune" in stocks)
print("11 in stocks             :", 11 in stocks)  # type: ignore[comparison-overlap]
print("11 in stocks.values()    :", 11 in stocks.values())

# Parcourir : clés, valeurs, couples.
print("Clés    :", list(stocks))
print("Valeurs :", list(stocks.values()))
for title, quantity in stocks.items():
    print(f"  {title:<16} {quantity:>3} exemplaire(s)")
print("Stock total :", sum(stocks.values()))
