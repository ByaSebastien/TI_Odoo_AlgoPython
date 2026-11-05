"""La portée des variables : locale, globale, et les pièges associés."""

SHOP_NAME = "PyBooks"  # globale : lisible depuis toutes les fonctions
orders_count = 0


def welcome() -> str:
    """Lit une constante globale : aucun problème."""
    return f"Bienvenue chez {SHOP_NAME}"


def compute_discount() -> int:
    """Crée une variable locale, invisible à l'extérieur."""
    local_rate = 10
    return local_rate


def record_order_wrong() -> None:
    """Version FAUSSE : modifier une globale sans la déclarer."""
    orders_count += 1  # noqa: F823, F841  (erreur volontaire)


def record_order(count: int) -> int:
    """Version correcte : l'état entre en paramètre et ressort en résultat."""
    return count + 1


def main() -> None:
    """Point d'entrée de la démonstration."""
    print(welcome())
    print("Remise :", compute_discount())
    print("local_rate existe-t-il ici ?", "local_rate" in globals())

    try:
        record_order_wrong()
    except UnboundLocalError as error:
        print("UnboundLocalError :", error)

    count = record_order(orders_count)
    count = record_order(count)
    print("Commandes enregistrées :", count)

    # Masquer un nom intégré : list ne désigne plus la fonction list().
    list = ["Dune", "Ulysse"]
    try:
        list("abc")  # type: ignore[operator]
    except TypeError as error:
        print("TypeError :", error)


if __name__ == "__main__":
    main()
