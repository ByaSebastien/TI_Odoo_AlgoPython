"""Aliasing : deux noms pour une même liste, et comment l'éviter."""

# b = a ne copie pas : les deux noms désignent la même liste.
cart = ["Dune"]
saved_cart = cart
saved_cart.append("Ulysse")
print("cart       :", cart)
print("saved_cart :", saved_cart)
print("Même objet :", cart is saved_cart)

# Une vraie copie est indépendante.
snapshot = cart.copy()
# snapshot = [*cart]
# snapshot = cart[:]
snapshot.append("Hamlet")
print("cart       :", cart)
print("snapshot   :", snapshot)
print("Même contenu au départ ? ", cart == cart.copy())
print("Même objet ?             ", cart is cart.copy())

# Avec un texte (immuable), le partage d'étiquette n'a pas de conséquence.
title = "Dune"
other_title = title
other_title += " (tome 1)"
print("title       :", title)
print("other_title :", other_title)

# Le piège : modifier une liste pendant qu'on la parcourt.
titles = ["A", "B", "C", "D"]
for item in titles:
    if item in ("B", "C"):
        titles.remove(item)
print("Après suppression pendant le parcours :", titles)

# La solution : construire une nouvelle liste avec les éléments à garder.
titles = ["A", "B", "C", "D"]
kept: list[str] = []
for item in titles:
    if item not in ("B", "C"):
        kept.append(item)
print("Nouvelle liste construite :", kept)
