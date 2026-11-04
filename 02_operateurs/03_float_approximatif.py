"""Les nombres à virgule (float) sont des approximations."""

# Le cas célèbre.
print("0.1 + 0.2 =", 0.1 + 0.2)

# D'autres calculs « simples » qui ne tombent pas juste.
print("1.1 * 3   =", 1.1 * 3)
print("0.1 * 3   =", 0.1 * 3)

# Trois articles à 0.10 € : le total affiché n'est pas 0.30.
unit_price = 0.10
total = unit_price + unit_price + unit_price
print("Total de trois articles à 0.10 € :", total)

# :.2f masque le problème à l'affichage… mais la valeur reste fausse.
print(f"Total affiché avec :.2f : {total:.2f}")

# round() utilise l'arrondi « bancaire » : vers le pair le plus proche.
print("round(2.5) =", round(2.5))
print("round(3.5) =", round(3.5))

# Et 2.675 est stocké comme 2.67499999... : l'arrondi à 2 décimales surprend.
print("round(2.675, 2) =", round(2.675, 2))
