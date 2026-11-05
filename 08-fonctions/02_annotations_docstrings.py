"""Annoter et documenter une fonction ; les annotations ne sont pas vérifiées."""

import inspect
from decimal import Decimal

FREE_SHIPPING_THRESHOLD = Decimal("50")
SHIPPING_FEE = Decimal("4.90")


def shipping_cost(paper_amount_incl_vat: Decimal) -> Decimal:
    """Calcule les frais de port d'une commande.

    Les frais sont offerts dès que le montant TTC des livres papier atteint
    le seuil de livraison gratuite.

    Args:
        paper_amount_incl_vat: Montant TTC des livres papier de la commande.

    Returns:
        Les frais de port, éventuellement nuls.
    """
    if paper_amount_incl_vat >= FREE_SHIPPING_THRESHOLD:
        return Decimal(0)
    return SHIPPING_FEE


def count_long_titles(titles: list[str], min_length: int) -> int:
    """Compte les titres d'au moins min_length caractères."""
    return len([title for title in titles if len(title) >= min_length])


def main() -> None:
    """Point d'entrée de la démonstration."""
    print("Port pour 30 € :", shipping_cost(Decimal("30")))
    print("Port pour 60 € :", shipping_cost(Decimal("60")))
    print("Titres longs :", count_long_titles(["Dune", "Le Petit Prince"], 10))

    # La signature et la docstring, telles que help() et l'éditeur les présentent.
    print()
    print(f"shipping_cost{inspect.signature(shipping_cost)}")
    print(inspect.getdoc(shipping_cost))

    # Python ne vérifie pas les annotations à l'exécution : cet appel incorrect
    # (un int au lieu d'un Decimal) fonctionne quand même. L'outil de vérification
    # des types du module 13 le signalerait ; « type: ignore » le fait taire ici.
    print()
    print("Appel avec un int :", shipping_cost(60))  # type: ignore[arg-type]


if __name__ == "__main__":
    main()
