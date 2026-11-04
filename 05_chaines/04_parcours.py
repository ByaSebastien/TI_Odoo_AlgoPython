"""Parcourir un texte : analyser ses caractères et construire un nouveau texte."""

VOWELS = "aeiouyàâéèêëîïôùûü"

title = "Les Misérables"

# Compter les voyelles : le texte VOWELS sert d'ensemble de référence.
vowel_count = 0
for character in title.lower():
    if character in VOWELS:
        vowel_count += 1
print(f"« {title} » contient {vowel_count} voyelles.")

# Garder uniquement les chiffres d'une saisie : on construit un nouveau texte.
raw_isbn = "ISBN 978-2-07-061275-8"
digits_only = ""
for character in raw_isbn:
    if character.isdecimal():
        digits_only += character
print(f"Chiffres extraits : {digits_only} ({len(digits_only)} chiffres)")

# Parcourir avec l'indice, quand la position compte : ici, un chiffre sur deux.
even_positions = ""
for index in range(len(digits_only)):
    if index % 2 == 0:
        even_positions += digits_only[index]
print(f"Chiffres aux positions paires : {even_positions}")
print(f"Même résultat avec un slicing : {digits_only[::2]}")

# Additionner les chiffres d'un texte.
digit_sum = 0
for character in digits_only:
    digit_sum += int(character)
print(f"Somme des chiffres : {digit_sum}")
