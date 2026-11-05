"""Deux schémas incontournables : compter et regrouper ; dictionnaires imbriqués."""

from decimal import Decimal

sold_categories = ["roman", "sf", "roman", "classique", "roman", "sf"]

# Compter les occurrences.
counts: dict[str, int] = {}
for category in sold_categories:
    counts[category] = counts.get(category, 0) + 1
print("Ventes par catégorie :", counts)

# Regrouper : une clé, une liste de valeurs.
books = [
    ("Les Misérables", "Victor Hugo"),
    ("L'Étranger", "Albert Camus"),
    ("Notre-Dame de Paris", "Victor Hugo"),
    ("La Peste", "Albert Camus"),
    ("Dune", "Frank Herbert"),
]
titles_by_author: dict[str, list[str]] = {}
for title, author in books:
    if author not in titles_by_author:
        titles_by_author[author] = []
    titles_by_author[author].append(title)

for author, titles in titles_by_author.items():
    print(f"{author} : {', '.join(titles)}")

# Imbriquer : la valeur est un tuple (titre, auteur, prix).
catalog = {
    "9782070612758": ("Le Petit Prince", "Antoine de Saint-Exupéry", Decimal("7.50")),
    "9782266320320": ("Dune", "Frank Herbert", Decimal("12.50")),
}
isbn = "9782266320320"
if isbn in catalog:
    title, author, price = catalog[isbn]
    print(f"{isbn} : {title} de {author}, {price} €")
