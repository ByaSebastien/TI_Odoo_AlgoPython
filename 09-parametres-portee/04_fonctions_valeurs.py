"""Les fonctions sont des valeurs : key=, lambda, table de fonctions."""

from decimal import Decimal

Book = tuple[str, str, Decimal]  # (titre, auteur, prix)

BOOKS: list[Book] = [
    ("Le Petit Prince", "Antoine de Saint-Exupéry", Decimal("7.50")),
    ("L'Étranger", "Albert Camus", Decimal("6.90")),
    ("Dune", "Frank Herbert", Decimal("12.50")),
    ("La Peste", "Albert Camus", Decimal("8.20")),
]


def by_price(book: Book) -> Decimal:
    """Clé de tri : le prix du livre."""
    return book[2]


def show(label: str, books: list[Book]) -> None:
    """Affiche une liste de titres précédée d'un libellé."""
    print(f"{label:<28}: {', '.join(book[0] for book in books)}")


def main() -> None:
    """Point d'entrée de la démonstration."""
    # Une fonction nommée, passée sans parenthèses.
    show("Par prix (fonction)", sorted(BOOKS, key=by_price))

    # La même chose avec une lambda.
    show("Par prix (lambda)", sorted(BOOKS, key=lambda book: book[2]))

    # Plusieurs critères : un tuple. Ici, par auteur, puis par titre.
    show("Par auteur puis titre", sorted(BOOKS, key=lambda book: (book[1], book[0])))

    # Prix décroissant, puis titre croissant : on inverse le critère numérique.
    show("Prix décroissant", sorted(BOOKS, key=lambda book: (-book[2], book[0])))

    # min et max acceptent aussi key=.
    cheapest = min(BOOKS, key=by_price)
    print(f"Le moins cher : {cheapest[0]} ({cheapest[2]} €)")

    # Une fonction se range dans une variable, ou dans un dictionnaire.
    sort_keys = {
        "t": lambda book: book[0].lower(),
        "a": lambda book: book[1],
    }
    for choice in ("t", "a"):
        show(f"Choix {choice!r}", sorted(BOOKS, key=sort_keys[choice]))


if __name__ == "__main__":
    main()
