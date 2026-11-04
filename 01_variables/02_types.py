"""Les types de base : int, float, str, bool et None."""

year = 1943
average_rating = 4.7
title = "Le Petit Prince"
is_classic = True
sequel = None

print(year, type(year))
print(average_rating, type(average_rating))
print(title, type(title))
print(is_classic, type(is_classic))
print(sequel, type(sequel))

# Un nombre et un texte qui contient des chiffres sont deux choses différentes.
quantity = 7
quantity_text = "7"
print(quantity, type(quantity))
print(quantity_text, type(quantity_text))

# La division / donne toujours un float, même quand le résultat « tombe juste ».
print(10 / 5, type(10 / 5))

# Le texte vide existe : c'est un str qui ne contient aucun caractère.
empty_text = ""
print("Texte vide :", empty_text, type(empty_text))

# Typage dynamique : un même nom peut désigner des valeurs de types différents.
# Possible, mais à éviter : une variable devrait garder un seul type. Le
# vérificateur de types du module 13 le signale ; « type: ignore » le fait taire.
value = 42
print(value, type(value))
value = "quarante-deux"  # type: ignore[assignment]
print(value, type(value))
