"""Les tuples : des enregistrements immuables, et le déballage."""

from decimal import Decimal

# Un tuple regroupe quelques valeurs liées : ici, un livre.
book = ("9782070612758", "Le Petit Prince", Decimal("7.50"))
print("Tuple :", book)
print("Titre :", book[1])

# Le déballage : une variable par élément.
isbn, title, price = book
print(f"{title} ({isbn}) : {price} €")

# Un tuple d'un seul élément exige une virgule.
not_a_tuple = 7
single = (7,)
print(type(not_a_tuple), type(single))

# C'est la virgule qui fait le tuple, pas les parenthèses.
point = 3, 4
print("point =", point, type(point))

# Une liste de tuples : le panier, ligne par ligne.
cart = [
    ("Le Petit Prince", 2, Decimal("7.50")),
    ("Dune", 1, Decimal("12.50")),
]
total = Decimal(0)
for item_title, quantity, unit_price in cart:
    line_total = quantity * unit_price
    total += line_total
    print(f"{quantity} x {item_title:<16} {line_total:>7.2f} €")
print(f"{'Total':<20} {total:>7.2f} €")

# La forme courte du test « or » du module 03.
answer = "oui"
if answer in ("o", "oui"):
    print("Réponse positive.")

# Un tuple ne se modifie pas : pour « changer » une ligne, on la remplace.
cart[1] = ("Dune", 3, Decimal("12.50"))
print("Ligne remplacée :", cart[1])
