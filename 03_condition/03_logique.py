"""Combiner des conditions (and, or, not) et tester la « truthiness »."""

stock = 0
is_ebook = True
is_member = True
total = 35

# and : les deux conditions doivent être vraies.
print("Membre ET plus de 30 € :", is_member and total >= 30)

# or : au moins une condition vraie.
print("Livre numérique OU en stock :", is_ebook or stock > 0)

# not : l'inverse.
print("Livre papier :", not is_ebook)

# Une combinaison typique : le stock ne compte que pour les livres papier.
if not is_ebook and stock == 0:
    print("Rupture de stock.")
else:
    print("Commande possible.")

# Le piège classique : « answer == "o" or "O" » est toujours vrai.
answer = "n"
wrong_test = answer == "o" or "O"
right_test = answer == "o" or answer == "O"  # noqa: PLR1714  (forme courte : module 06)
print('answer == "o" or "O"             :', bool(wrong_test))
print('answer == "o" or answer == "O"   :', right_test)

# Truthiness : zéro, None et le vide sont faux, tout le reste est vrai.
print("bool(0)       :", bool(0))
print("bool('')      :", bool(""))
print("bool(None)    :", bool(None))
print("bool(' ')     :", bool(" "))
print("bool('0')     :", bool("0"))
print("bool('False') :", bool("False"))

# Usage : tester qu'une saisie n'est pas vide.
name = input("Votre prénom : ")
if not name:
    print("Vous n'avez rien saisi.")
else:
    print(f"Bonjour {name} !")
