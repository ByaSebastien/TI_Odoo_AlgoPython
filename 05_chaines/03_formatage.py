"""Le mini-langage des f-strings : largeur, alignement, décimales, milliers."""

from decimal import Decimal

LABEL_WIDTH = 20
QUANTITY_WIDTH = 4
AMOUNT_WIDTH = 10

# Alignements sur 12 caractères ; les | montrent les bords.
word = "PyBooks"
print(f"|{word:<12}|  à gauche")
print(f"|{word:>12}|  à droite")
print(f"|{word:^12}|  centré")
print(f"|{word:*^12}|  centré, complété par des *")

# Nombres : décimales, largeur, zéros, milliers.
price = Decimal("7.5")
print(f"|{price:.2f}|")
print(f"|{price:>10.2f}|")
print(f"|{42:05d}|")
print(f"|{1234567.891:,.2f}|")

# Un ticket de caisse : colonnes alignées grâce aux largeurs fixes.
separator = "-" * (LABEL_WIDTH + QUANTITY_WIDTH + AMOUNT_WIDTH + 2)
print(separator)
print(f"{'Article':<{LABEL_WIDTH}}{'Qté':>{QUANTITY_WIDTH}}{'Montant':>{AMOUNT_WIDTH}}")
print(separator)
print(
    f"{'Le Petit Prince':<{LABEL_WIDTH}}"
    f"{2:>{QUANTITY_WIDTH}}"
    f"{Decimal('15.00'):>{AMOUNT_WIDTH}.2f} €"
)
print(
    f"{'Marque-page':<{LABEL_WIDTH}}"
    f"{1:>{QUANTITY_WIDTH}}"
    f"{Decimal('2.50'):>{AMOUNT_WIDTH}.2f} €"
)
print(separator)
print(
    f"{'TOTAL':<{LABEL_WIDTH + QUANTITY_WIDTH}}{Decimal('17.50'):>{AMOUNT_WIDTH}.2f} €"
)
