"""Variables : affectation, réaffectation et constantes."""

# Une constante : une valeur fixe qui a un sens, nommée en majuscules.
DAILY_GOAL = 30

# Affectation : le nom de gauche désigne la valeur de droite.
pages_read = 12
print("Pages lues :", pages_read)

# Réaffectation : le nom désigne une nouvelle valeur, l'ancienne est oubliée.
pages_read = 20
print("Pages lues :", pages_read)

# La droite est calculée d'abord (20 + 5), puis le résultat est affecté.
pages_read = pages_read + 5
print("Pages lues :", pages_read)

# Une variable peut être calculée à partir d'autres variables.
pages_left = DAILY_GOAL - pages_read
print("Pages restantes pour l'objectif du jour :", pages_left)

# La valeur est copiée au moment du calcul : modifier pages_read ensuite
# ne met PAS à jour pages_left.
pages_read = 30
print("Pages lues :", pages_read)
print("Pages restantes (non recalculées) :", pages_left)
