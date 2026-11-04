"""Contrôler une boucle : break, continue et le menu while True."""

title = "Le Petit Prince"

# continue : on ignore les espaces et on passe au caractère suivant.
letters_count = 0
for letter in title:
    if letter == " ":
        continue
    letters_count += 1
print(f"« {title} » contient {letters_count} lettres (espaces exclus).")

# break : on s'arrête au premier caractère cherché.
position = 0
for letter in title:
    if letter == "P":
        break
    position += 1
print(f"Premier « P » à la position {position}.")

# Le menu : while True, dont on sort explicitement avec break.
while True:
    print("1. Bonjour   2. Heure d'ouverture   Q. Quitter")
    choice = input("Votre choix : ")
    if choice == "Q" or choice == "q":  # noqa: PLR1714  (forme courte : module 06)
        break
    match choice:
        case "1":
            print("Bonjour et bienvenue !")
        case "2":
            print("Ouvert du lundi au samedi, de 9 h à 18 h.")
        case _:
            print("Choix inconnu.")
print("Au revoir !")
