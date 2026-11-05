"""Les compréhensions : construire une liste, un dictionnaire ou un ensemble."""

from decimal import ROUND_HALF_UP, Decimal

VAT_RATE = Decimal("0.06")
CENT = Decimal("0.01")
CHEAP_THRESHOLD = Decimal("10")

books = [
    ("Le Petit Prince", "Antoine de Saint-Exupéry", Decimal("7.50")),
    ("L'Étranger", "Albert Camus", Decimal("6.90")),
    ("Dune", "Frank Herbert", Decimal("12.50")),
    ("La Peste", "Albert Camus", Decimal("8.20")),
]

# Avec une boucle…
titles_loop: list[str] = []
for title, _author, _price in books:
    titles_loop.append(title)
print("Boucle        :", titles_loop)

# … et avec une compréhension de liste : même résultat.
titles = [title for title, _author, _price in books]
print("Compréhension :", titles)

# Une transformation : les prix TTC.
prices_incl_vat = [
    (price * (1 + VAT_RATE)).quantize(CENT, rounding=ROUND_HALF_UP)
    for _title, _author, price in books
]
print("Prix TTC :", [str(price) for price in prices_incl_vat])

# Un filtre : les livres à moins de 10 €.
cheap_titles = [title for title, _author, price in books if price < CHEAP_THRESHOLD]
print("Moins de 10 € :", cheap_titles)

# Une compréhension de dictionnaire : titre -> prix.
price_by_title = {title: price for title, _author, price in books}
print("Dictionnaire :", {title: str(price) for title, price in price_by_title.items()})

# Une compréhension d'ensemble : les auteurs, sans doublons.
authors = {author for _title, author, _price in books}
print("Auteurs :", sorted(authors))

# Retirer des éléments sans modifier la liste parcourue (module 06).
out_of_stock = {"Dune", "La Peste"}
available = [title for title in titles if title not in out_of_stock]
print("Disponibles :", available)
