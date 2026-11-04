"""Parcourir, agréger et trier une liste ; split et join."""

titles = ["dune", "Le Petit Prince", "L'Étranger", "Ulysse"]
ratings = [4, 5, 3, 5, 4, 2]

# Parcourir.
for title in titles:
    print("-", title)

# Numéroter avec enumerate (à partir de 1).
for number, title in enumerate(titles, start=1):
    print(f"{number}. {title}")

# Agréger.
print("Nombre de notes :", len(ratings))
print("Somme  :", sum(ratings))
print("Minimum:", min(ratings))
print("Maximum:", max(ratings))
print(f"Moyenne: {sum(ratings) / len(ratings):.2f}")

# sorted renvoie une nouvelle liste ; l'originale ne change pas.
print("sorted(titles)          :", sorted(titles))
print("titles inchangée        :", titles)

# Le tri distingue les majuscules : key=str.lower trie sans en tenir compte.
print("sorted(key=str.lower)   :", sorted(titles, key=str.lower))
print("sorted(key=len)         :", sorted(titles, key=len))
print("sorted(reverse=True)    :", sorted(ratings, reverse=True))

# sort() trie la liste elle-même.
ratings.sort()
print("ratings après sort()    :", ratings)

# split et join : le pont entre texte et liste.
authors_text = "Hugo;Camus;Herbert"
authors = authors_text.split(";")
print("split(';') :", authors)
messy_title = "  le petit   prince "
print("split()    :", messy_title.split())
print("join       :", ", ".join(authors))
