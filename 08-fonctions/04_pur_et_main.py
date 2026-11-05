"""Séparer le calcul (fonctions pures) de l'interface (saisie, affichage)."""

from decimal import ROUND_HALF_UP, Decimal

VAT_RATE = Decimal("0.06")
CENT = Decimal("0.01")
LABEL_WIDTH = 16


# --- Calcul : des fonctions pures, testables ---


def line_total(unit_price: Decimal, quantity: int) -> Decimal:
    """Renvoie le montant HT d'une ligne de commande."""
    return unit_price * quantity


def vat_amount(amount_excl_vat: Decimal) -> Decimal:
    """Renvoie la TVA d'un montant HT, arrondie au centime."""
    return (amount_excl_vat * VAT_RATE).quantize(CENT, rounding=ROUND_HALF_UP)


def format_receipt(amount_excl_vat: Decimal) -> str:
    """Construit le texte d'un reçu, sans l'afficher."""
    vat = vat_amount(amount_excl_vat)
    lines = [
        f"{'Montant HT':<{LABEL_WIDTH}}{amount_excl_vat:>8.2f} €",
        f"{'TVA':<{LABEL_WIDTH}}{vat:>8.2f} €",
        f"{'Montant TTC':<{LABEL_WIDTH}}{amount_excl_vat + vat:>8.2f} €",
    ]
    return "\n".join(lines)


# --- Interface : saisies et affichages ---


def ask_quantity() -> int:
    """Demande une quantité au moins égale à 1."""
    quantity = int(input("Quantité : "))
    while quantity < 1:
        print("La quantité doit être au moins égale à 1.")
        quantity = int(input("Quantité : "))
    return quantity


def main() -> None:
    """Point d'entrée : enchaîne saisie, calcul et affichage."""
    quantity = ask_quantity()
    amount = line_total(Decimal("7.50"), quantity)
    print(format_receipt(amount))


if __name__ == "__main__":
    main()
