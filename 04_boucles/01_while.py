"""La boucle while : répéter tant qu'une condition est vraie."""

MIN_QUANTITY = 1
MAX_QUANTITY = 10

# Un compte à rebours : la condition dépend de countdown, qui évolue à chaque tour.
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Partez !")

# Redemander une saisie tant qu'elle n'est pas valide.
quantity = int(input(f"Quantité ({MIN_QUANTITY} à {MAX_QUANTITY}) : "))
while quantity < MIN_QUANTITY or quantity > MAX_QUANTITY:
    print("Quantité invalide.")
    quantity = int(input(f"Quantité ({MIN_QUANTITY} à {MAX_QUANTITY}) : "))
print(f"Quantité retenue : {quantity}")

# Combien d'années pour doubler une épargne placée à 3 % par an ?
savings = 1000.0
years = 0
while savings < 2000:
    savings *= 1.03
    years += 1
print(f"Épargne doublée après {years} ans ({savings:.2f} €)")
