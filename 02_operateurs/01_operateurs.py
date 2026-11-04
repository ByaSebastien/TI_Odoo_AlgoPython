"""Les opérateurs arithmétiques, leurs priorités et l'affectation augmentée."""

# Les sept opérateurs.
print("7 + 2  =", 7 + 2)
print("7 - 2  =", 7 - 2)
print("7 * 2  =", 7 * 2)
print("7 / 2  =", 7 / 2)
print("7 // 2 =", 7 // 2)
print("7 % 2  =", 7 % 2)
print("2 ** 10 =", 2**10)

# Mélanger int et float donne un float.
print("3 * 2.5 =", 3 * 2.5)
print("4 + 1.0 =", 4 + 1.0)

# Priorités : multiplication avant addition, sauf parenthèses.
print("2 + 3 * 4   =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)

# Piège : la puissance passe avant le signe négatif. Si vous tapez -2**2,
# l'outil de mise en forme ruff (module 13) ajoute lui-même les parenthèses
# -(2**2) pour montrer ce que Python calcule réellement.
print("-2 ** 2   =", -(2**2))
print("(-2) ** 2 =", (-2) ** 2)

# Affectation augmentée : mettre à jour une variable à partir d'elle-même.
stock = 10
stock -= 3
print("Stock après la vente de 3 exemplaires :", stock)
stock += 5
print("Stock après une livraison de 5 exemplaires :", stock)
stock *= 2
print("Stock doublé :", stock)
