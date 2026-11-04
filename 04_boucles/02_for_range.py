"""La boucle for : range, parcours d'un texte et accumulateurs."""

DAYS_PER_WEEK = 7

# range(5) produit 0, 1, 2, 3, 4 : la fin est exclue.
for number in range(5):
    print(number, end=" ")
print()

# range(début, fin, pas)
for number in range(1, 6):
    print(number, end=" ")
print()
for number in range(0, 10, 2):
    print(number, end=" ")
print()
for number in range(5, 0, -1):
    print(number, end=" ")
print()

# Parcourir un texte caractère par caractère.
for letter in "ISBN":
    print(letter, end="-")
print()

# Accumulateurs : somme, compteur et maximum, sur une semaine de lecture.
total_pages = 0
reading_days = 0
best_day_pages = 0
for day in range(1, DAYS_PER_WEEK + 1):
    pages = day % 3 * 10  # données d'exemple : 10, 20, 0, 10, 20, 0, 10 pages
    total_pages += pages
    if pages > 0:
        reading_days += 1
    best_day_pages = max(best_day_pages, pages)
print(f"Total : {total_pages} pages sur {reading_days} jours de lecture")
print(f"Meilleure journée : {best_day_pages} pages")
print(f"Moyenne : {total_pages / DAYS_PER_WEEK:.1f} pages par jour")
