"""Les valeurs par défaut, et le piège de la valeur par défaut mutable."""

from decimal import Decimal


def format_price(amount: Decimal, currency: str = "€") -> str:
    """Formate un montant avec deux décimales et une devise (euro par défaut)."""
    return f"{amount:.2f} {currency}"


def add_title_wrong(title: str, titles: list[str] = []) -> list[str]:  # noqa: B006
    """Version FAUSSE : la liste par défaut est partagée entre tous les appels."""
    titles.append(title)
    return titles


def add_title(title: str, titles: list[str] | None = None) -> list[str]:
    """Ajoute un titre à une liste, ou à une nouvelle liste si aucune n'est fournie."""
    if titles is None:
        titles = []
    titles.append(title)
    return titles


def main() -> None:
    """Point d'entrée de la démonstration."""
    print(format_price(Decimal("7.5")))
    print(format_price(Decimal("7.5"), "$"))
    print(format_price(Decimal("7.5"), currency="CHF"))

    print("--- Version fausse ---")
    print(add_title_wrong("Dune"))
    print(add_title_wrong("Ulysse"))  # surprise : Dune est toujours là
    print(add_title_wrong("Hamlet"))

    print("--- Version correcte ---")
    print(add_title("Dune"))
    print(add_title("Ulysse"))
    print(add_title("Hamlet", ["Macbeth"]))


if __name__ == "__main__":
    main()
