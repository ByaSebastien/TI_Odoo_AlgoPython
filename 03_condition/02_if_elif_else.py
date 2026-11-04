"""Prendre des décisions avec if, elif et else."""

from decimal import Decimal

FREE_SHIPPING_THRESHOLD = Decimal("50")
SHIPPING_FEE = Decimal("4.90")
SILVER_THRESHOLD = Decimal("100")
GOLD_THRESHOLD = Decimal("200")

total = Decimal(input("Montant de la commande : "))

# if / else : deux cas.
if total >= FREE_SHIPPING_THRESHOLD:
    shipping = Decimal(0)
    print("Livraison offerte !")
else:
    shipping = SHIPPING_FEE
    missing = FREE_SHIPPING_THRESHOLD - total
    print(f"Plus que {missing:.2f} € pour la livraison offerte.")

# Cette ligne n'est plus indentée : elle s'exécute dans tous les cas.
print(f"Frais de port : {shipping:.2f} €")

# if / elif / else : plusieurs cas, du plus spécifique au plus général.
if total >= GOLD_THRESHOLD:
    gift = "un tote bag"
elif total >= SILVER_THRESHOLD:
    gift = "un marque-page"
else:
    gift = "aucun cadeau"
print(f"Cadeau offert : {gift}")
