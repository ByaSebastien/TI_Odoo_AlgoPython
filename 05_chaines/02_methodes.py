"""Les méthodes de str : nettoyer, rechercher, tester ; l'immuabilité."""

raw_title = "  le petit PRINCE  "

# Nettoyer et transformer : chaque méthode renvoie un NOUVEAU texte.
print(repr(raw_title.strip()))
print(repr(raw_title.strip().lower()))
print(repr(raw_title.strip().title()))

# L'original n'a pas changé : un texte est immuable.
print("Original inchangé :", repr(raw_title))

# Le piège : appeler la méthode sans récupérer le résultat.
title = "le petit prince"
title.title()
print("Sans réaffectation :", title)
title = title.title()
print("Avec réaffectation :", title)

# Remplacer.
isbn_with_dashes = "978-2-07-061275-8"
print("Sans tirets :", isbn_with_dashes.replace("-", ""))

# Rechercher.
print("'Petit' dans le titre :", "Petit" in title)
print("Position de 'Petit'   :", title.find("Petit"))
print("Position de 'Grand'   :", title.find("Grand"))
print("Nombre de 'e'         :", title.count("e"))
print("Commence par 'Le'     :", title.startswith("Le"))

# Tester le contenu.
print("'9782070612758'.isdecimal() :", "9782070612758".isdecimal())
print("'978-2-07'.isdecimal()      :", "978-2-07".isdecimal())
print("'Zoé'.isalpha()             :", "Zoé".isalpha())

# Le réflexe pour toute saisie : nettoyer dès la lecture.
choice = input("Votre choix (Q pour quitter) : ").strip().lower()
if choice == "q":
    print("Vous avez choisi de quitter.")
else:
    print(f"Vous avez choisi : {choice!r}")

# Comparer sans tenir compte de la casse.
answer = "OUI"
print("answer == 'oui'         :", answer == "oui")
print("answer.lower() == 'oui' :", answer.lower() == "oui")
