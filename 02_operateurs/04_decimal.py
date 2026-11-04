"""Decimal : calculer juste avec de l'argent, et arrondir au centime."""

from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")

# Créé à partir d'un texte : la valeur est exacte.
print("Decimal('0.1') + Decimal('0.2') =", Decimal("0.1") + Decimal("0.2"))

# Créé à partir d'un float : l'imprécision du float est conservée.
print("Decimal(0.1) =", Decimal(0.1))  # noqa: RUF032  (erreur volontaire)

# Les calculs conservent les décimales significatives.
unit_price = Decimal("7.50")
line_total = unit_price * 2
print("7.50 x 2 =", line_total)

# Une multiplication peut produire plus de deux décimales.
vat = line_total * Decimal("0.06")
print("TVA brute :", vat)

# quantize arrondit au même nombre de décimales que CENT, soit 2.
print("TVA arrondie au centime :", vat.quantize(CENT, rounding=ROUND_HALF_UP))

# La règle d'arrondi compte : 0.125 donne 0.13 en arrondi commercial…
amount = Decimal("0.125")
print("0.125 arrondi commercial :", amount.quantize(CENT, rounding=ROUND_HALF_UP))
# … mais 0.12 avec l'arrondi par défaut (bancaire).
print("0.125 arrondi par défaut :", amount.quantize(CENT))

# Les f-strings acceptent les Decimal.
print(f"Total : {line_total:.2f} €")

# Les entiers se mélangent sans problème aux Decimal.
print("Decimal('9.99') * 3 =", Decimal("9.99") * 3)
