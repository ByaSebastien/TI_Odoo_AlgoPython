"""Indexation et slicing : accéder aux caractères d'un texte par leur position."""

isbn = "9782070612758"

print("Texte      :", isbn)
print("Longueur   :", len(isbn))

# Les indices commencent à 0.
print("isbn[0]    :", isbn[0])
print("isbn[3]    :", isbn[3])
print("isbn[12]   :", isbn[12])

# Les indices négatifs partent de la fin : -1 est le dernier caractère.
print("isbn[-1]   :", isbn[-1])
print("isbn[-2]   :", isbn[-2])

# Le slicing extrait un morceau : [début:fin], fin exclue.
print("isbn[:3]   :", isbn[:3])
print("isbn[3:]   :", isbn[3:])
print("isbn[:-1]  :", isbn[:-1])
print("isbn[3:5]  :", isbn[3:5])

# Un troisième nombre fixe le pas.
print("isbn[::2]  :", isbn[::2])
print("isbn[::-1] :", isbn[::-1])

# Le slicing ne déborde jamais : il s'arrête à la fin du texte.
print("isbn[10:100] :", isbn[10:100])

# Un exemple concret : séparer le préfixe 978 du reste de l'ISBN.
prefix = isbn[:3]
body = isbn[3:-1]
check_digit = isbn[-1]
print(f"Préfixe {prefix}, corps {body}, clé de contrôle {check_digit}")
