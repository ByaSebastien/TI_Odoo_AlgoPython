"""Support de démonstration du débogueur : l'offre « 3 achetés, le 3e offert ».

Chaque troisième exemplaire d'un même livre est offert. Le programme calcule,
exemplaire par exemplaire, le montant à payer.
"""

from decimal import Decimal

FREE_EVERY = 3

unit_price = Decimal("8.90")
quantity = int(input("Nombre d'exemplaires : "))

total = Decimal(0)
free_copies = 0
for copy_number in range(1, quantity + 1):
    if copy_number % FREE_EVERY == 0:
        free_copies += 1
    else:
        total += unit_price

print(f"Exemplaires offerts : {free_copies}")
print(f"Total à payer : {total:.2f} €")
