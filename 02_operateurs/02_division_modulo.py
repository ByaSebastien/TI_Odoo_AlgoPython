"""Division entière (//) et modulo (%) en situation."""

import math

BOOKS_PER_BOX = 5
MINUTES_PER_HOUR = 60

# Combien de cartons pleins, et combien de livres restent ?
books = 23
full_boxes = books // BOOKS_PER_BOX
remaining_books = books % BOOKS_PER_BOX
print(
    f"{books} livres : {full_boxes} cartons pleins et {remaining_books} livres restants"
)

# Combien de cartons faut-il au total ? (le dernier n'est pas plein)
boxes_needed = math.ceil(books / BOOKS_PER_BOX)
print(f"Cartons nécessaires : {boxes_needed}")

# Convertir des minutes en heures et minutes.
duration = 150
hours = duration // MINUTES_PER_HOUR
minutes = duration % MINUTES_PER_HOUR
print(f"{duration} minutes = {hours} h {minutes} min")

# Le reste d'une division par 2 indique la parité : 0 si pair, 1 si impair.
print("Reste de 1984 / 2 :", 1984 % 2)
print("Reste de 1985 / 2 :", 1985 % 2)

# Le reste d'une division par 10 donne le dernier chiffre.
print("Dernier chiffre de 1984 :", 1984 % 10)
