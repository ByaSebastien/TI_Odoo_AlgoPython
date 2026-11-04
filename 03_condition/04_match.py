"""Choisir parmi plusieurs valeurs avec match / case."""

print("1. Voir le catalogue")
print("2. Voir le panier")
print("3. Passer commande")
print("Q. Quitter")

choice = input("Votre choix : ")

match choice:
    case "1":
        print("Affichage du catalogue…")
    case "2":
        print("Affichage du panier…")
    case "3":
        print("Passage de la commande…")
    case "q" | "Q":
        print("Au revoir !")
    case _:
        print(f"Choix inconnu : {choice!r}")
