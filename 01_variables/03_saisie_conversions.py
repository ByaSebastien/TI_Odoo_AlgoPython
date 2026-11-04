"""Saisir une valeur avec input, puis la convertir dans le bon type."""

# input renvoie toujours un texte (str).
name = input("Votre prénom : ")
raw_age = input("Votre âge : ")
print("Type de la saisie :", type(raw_age))

# Sans conversion, * 2 répète le texte au lieu de multiplier.
print("Sans conversion :", raw_age * 2)

# Avec conversion, on obtient un vrai nombre.
age = int(raw_age)
print("Avec conversion :", age * 2)
print(f"{name}, dans 10 ans, vous aurez {age + 10} ans.")

# Les autres conversions.
print(float("12.5"), type(float("12.5")))
print(str(42), type(str(42)))

# int() appliqué à un float tronque : la partie décimale est supprimée.
print(int(12.9))
