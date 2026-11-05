"""Définir et appeler des fonctions : paramètres, return, None."""

from decimal import Decimal

VAT_RATE = Decimal("0.06")
CENTS_PER_EURO = 100


def price_with_vat(price: Decimal, vat_rate: Decimal) -> Decimal:
    """Renvoie le prix toutes taxes comprises."""
    return price * (1 + vat_rate)


def greet(name: str) -> None:
    """Affiche un message de bienvenue (et ne renvoie rien)."""
    print(f"Bienvenue, {name} !")


def split_price(total: Decimal) -> tuple[int, int]:
    """Sépare un montant en euros et en centimes."""
    euros = int(total)
    cents = int((total - euros) * CENTS_PER_EURO)
    return euros, cents


def main() -> None:
    """Point d'entrée de la démonstration."""
    # Appel par position, puis par nom.
    print(price_with_vat(Decimal("7.50"), VAT_RATE))
    print(price_with_vat(price=Decimal("12.50"), vat_rate=VAT_RATE))

    # Le résultat peut être stocké, ou utilisé directement dans une expression.
    total = price_with_vat(Decimal("7.50"), VAT_RATE) * 2
    print(f"Deux exemplaires : {total:.2f} €")

    # Une fonction sans return renvoie None (le vérificateur de types du
    # module 13 signale qu'on récupère ce None ; « type: ignore » le fait taire).
    result = greet("Ada")  # type: ignore[func-returns-value]
    print("Valeur renvoyée par greet :", result)

    # Plusieurs valeurs : un tuple, déballé à l'appel.
    euros, cents = split_price(Decimal("12.90"))
    print(f"{euros} euros et {cents} centimes")


if __name__ == "__main__":
    main()
