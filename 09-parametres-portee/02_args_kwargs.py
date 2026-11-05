"""Un nombre variable d'arguments : *args et **kwargs, et le déballage à l'appel."""

from decimal import Decimal


def total(*amounts: Decimal) -> Decimal:
    """Additionne un nombre quelconque de montants."""
    print(f"  amounts reçu : {amounts!r} ({type(amounts).__name__})")
    return sum(amounts, Decimal(0))


def describe_book(title: str, **details: str) -> str:
    """Décrit un livre avec des détails libres (auteur, éditeur…)."""
    print(f"  details reçu : {details!r} ({type(details).__name__})")
    parts = [f"{key} : {value}" for key, value in details.items()]
    return f"{title} ({', '.join(parts)})"


def main() -> None:
    """Point d'entrée de la démonstration."""
    print("Trois montants :")
    print(total(Decimal("7.50"), Decimal("12.50"), Decimal("6.90")))
    print("Aucun montant :")
    print(total())

    print("Détails libres :")
    print(describe_book("Dune", author="Frank Herbert", publisher="Pocket"))

    # À l'appel, * et ** déballent une liste et un dictionnaire.
    prices = [Decimal("7.50"), Decimal("12.50")]
    print("Déballage d'une liste :")
    print(total(*prices))

    details = {"author": "Albert Camus", "year": "1942"}
    print("Déballage d'un dictionnaire :")
    print(describe_book("L'Étranger", **details))


if __name__ == "__main__":
    main()
