from decimal import Decimal, ROUND_HALF_UP

print(3 * 3)
print(3 ** 3)
print(9 / 2)
print(9 // 2)
print(9 % 2)

print("A" * 15)
print([0] * 10)

print("A" * 2 * 2)

price = 0.1
price2 = 0.2

# price, price2 = 0.1, 0.2

print(price + price2)

CENT = Decimal("0.01")

vat = Decimal("15.79") * Decimal("0.06")

print(vat)

vat = vat.quantize(CENT,ROUND_HALF_UP)

print(vat)