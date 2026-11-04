"""Les comparaisons produisent des booléens."""

import math
from decimal import Decimal

stock = 7
quantity = 3

# Chaque comparaison donne True ou False.
print("quantity == stock :", quantity == stock)
print("quantity != stock :", quantity != stock)
print("quantity < stock  :", quantity < stock)
print("quantity >= stock :", quantity >= stock)

# Un booléen peut être stocké dans une variable.
is_available = quantity <= stock
print("Disponible :", is_available)

# Comparaison enchaînée : « entre 1 et 10 ».
print("1 <= quantity <= 10 :", 1 <= quantity <= 10)

# Les textes se comparent caractère par caractère, majuscules comprises.
answer = "Oui"
print('answer == "oui" :', answer == "oui")
first_name = "Zoé"
second_name = "adam"
print('"Zoé" < "adam"   :', first_name < second_name)

# Deux textes de chiffres ne se comparent pas comme des nombres.
small_text = "10"
big_text = "9"
print('"10" < "9" :', small_text < big_text)
print("10 < 9     :", int(small_text) < int(big_text))

# Les float sont approximatifs : on ne teste pas leur égalité stricte.
computed = 0.1 + 0.2
print("0.1 + 0.2 == 0.3 :", computed == 0.3)
print("math.isclose     :", math.isclose(computed, 0.3))

# Les Decimal se comparent exactement.
print("Decimal('50') >= Decimal('50.00') :", Decimal("50") >= Decimal("50.00"))
