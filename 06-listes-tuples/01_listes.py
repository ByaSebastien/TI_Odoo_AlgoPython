"""Créer, lire et modifier une liste."""

titles = ["Le Petit Prince", "L'Étranger", "Dune"]

# Lire : comme un texte (indices, slicing, len, in).
print("Liste      :", titles)
print("Premier    :", titles[0])
print("Dernier    :", titles[-1])
print("Deux premiers :", titles[:2])
print("Nombre     :", len(titles))
print("'Dune' présent :", "Dune" in titles)

# Modifier : une liste est mutable.
titles[1] = "La Peste"
print("Après remplacement :", titles)

titles.append("Ulysse")
print("Après append       :", titles)

titles.insert(0, "Hamlet")
print("Après insert       :", titles)

titles.remove("Dune")
print("Après remove       :", titles)

last = titles.pop()
print(f"pop() a retiré {last!r} :", titles)

print("Indice de 'La Peste' :", titles.index("La Peste"))

# Le piège : append modifie la liste et renvoie None. Le vérificateur de types
# (module 13) détecte cette erreur ; « type: ignore » le fait taire ici.
result = titles.append("Dune")  # type: ignore[func-returns-value]
print("Valeur renvoyée par append :", result)
print("La liste, elle, a bien changé :", titles)

# Une liste vide est « fausse » dans une condition.
cart: list[str] = []
if not cart:
    print("Le panier est vide.")

