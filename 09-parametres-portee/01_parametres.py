"""Signatures lisibles : positionnel, nommé, keyword-only, positional-only."""

from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")
GIFT_WRAP_FEE = Decimal("2.50")


def order_total(
    amount: Decimal,
    *,
    discount_rate: Decimal = Decimal(0),
    gift_wrap: bool = False,
) -> Decimal:
    """Calcule le total d'une commande.

    Args:
        amount: Montant des articles.
        discount_rate: Taux de remise, entre 0 et 1 (nommé obligatoirement).
        gift_wrap: Ajoute l'emballage cadeau (nommé obligatoirement).

    Returns:
        Le total, arrondi au centime.
    """
    total = amount * (1 - discount_rate)
    if gift_wrap:
        total += GIFT_WRAP_FEE
    return total.quantize(CENT, rounding=ROUND_HALF_UP)


def initials(first_name: str, last_name: str, /) -> str:
    """Renvoie les initiales (paramètres positional-only)."""
    return f"{first_name[0]}. {last_name[0]}."


def main() -> None:
    """Point d'entrée de la démonstration."""
    print(order_total(Decimal("40")))
    print(order_total(Decimal("40"), discount_rate=Decimal("0.10")))
    print(order_total(Decimal("40"), gift_wrap=True, discount_rate=Decimal("0.10")))

    # Les options keyword-only ne peuvent pas être passées par position.
    try:
        order_total(Decimal("40"), Decimal("0.10"))  # type: ignore[call-arg]
    except TypeError as error:
        print("TypeError :", error)

    # Les paramètres positional-only ne peuvent pas être nommés.
    print(initials("Victor", "Hugo"))
    try:
        initials(first_name="Victor", last_name="Hugo")  # type: ignore[call-arg]
    except TypeError as error:
        print("TypeError :", error)


if __name__ == "__main__":
    main()
