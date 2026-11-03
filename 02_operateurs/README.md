# Module 02 : nombres et opérateurs

> **Objectifs du module**
> - Maîtriser les opérateurs arithmétiques, dont `//`, `%` et `**`, et leurs priorités.
> - Mettre à jour une variable avec les opérateurs d'affectation augmentée (`+=`, `-=`…).
> - Comprendre pourquoi `0.1 + 0.2` ne donne pas `0.3`.
> - Calculer **juste** avec de l'argent grâce à `Decimal`, et arrondir correctement au centime.
>
> **Durée indicative** : 3 h
> **Prérequis** : module 01
> **Étape PyBooks** : [02, le prix TTC au centime près](../fil-rouge/etape-02/)

---

## L'essentiel

### 1. Les opérateurs arithmétiques

| Opérateur | Opération | Exemple | Résultat |
|---|---|---|---|
| `+` | addition | `7 + 2` | `9` |
| `-` | soustraction | `7 - 2` | `5` |
| `*` | multiplication | `7 * 2` | `14` |
| `/` | division | `7 / 2` | `3.5` (toujours un `float`) |
| `//` | division entière | `7 // 2` | `3` |
| `%` | modulo : reste de la division entière | `7 % 2` | `1` |
| `**` | puissance | `2 ** 10` | `1024` |

**Mélanger `int` et `float`** : le résultat est un `float`. `3 * 2.5` vaut `7.5`, et `4 + 1.0` vaut `5.0`.

**Diviser par zéro** est une erreur : `ZeroDivisionError: division by zero`.

### 2. Les priorités

Comme en mathématiques, de la plus forte à la plus faible :

1. les **parenthèses** `( )` ;
2. la puissance `**` ;
3. le signe négatif `-x` ;
4. `*`, `/`, `//`, `%`, de gauche à droite ;
5. `+`, `-`, de gauche à droite.

```python
2 + 3 * 4  # 14 : la multiplication d'abord
(2 + 3) * 4  # 20 : les parenthèses d'abord
```

> 💡 En cas de doute, **ajoutez des parenthèses**. Elles ne coûtent rien et rendent l'intention évidente.

> ⚠️ **Piège** : `-2 ** 2` vaut `-4`, et non `4` : la puissance passe avant le signe. On écrit `(-2) ** 2`.

### 3. Division entière et modulo

`//` et `%` vont ensemble : ils répondent à « combien de fois, et combien en reste-t-il ? ».

```python
books = 23
BOOKS_PER_BOX = 5

full_boxes = books // BOOKS_PER_BOX  # 4 cartons pleins
remaining = books % BOOKS_PER_BOX  # 3 livres restants
```

Usages typiques :
- convertir des unités : `150` minutes donnent `150 // 60 = 2` heures et `150 % 60 = 30` minutes ;
- savoir si un nombre est pair : `n % 2` vaut `0` pour un nombre pair ;
- obtenir le dernier chiffre d'un nombre : `1984 % 10` vaut `4`.

> Démo : [`demos/02_division_modulo.py`](demos/02_division_modulo.md)

### 4. L'affectation augmentée

Mettre à jour une variable à partir de sa propre valeur est si fréquent qu'il existe des raccourcis :

| Écriture courte | Équivalent |
|---|---|
| `stock -= 1` | `stock = stock - 1` |
| `total += price` | `total = total + price` |
| `amount *= 2` | `amount = amount * 2` |
| `pages //= 2` | `pages = pages // 2` |

> ⚠️ **Piège** : `++` et `--` n'existent **pas** en Python. Écrire `stock++` est une erreur de syntaxe, et `++stock` est accepté… mais ne fait **rien** (c'est deux fois le signe `+`). On écrit `stock += 1`.

> Démo : [`demos/01_operateurs.py`](demos/01_operateurs.md)

---

### 5. Les nombres à virgule sont approximatifs

```python
>>> 0.1 + 0.2
0.30000000000000004
```

Ce n'est pas un bug de Python : **tous** les langages donnent ce résultat. L'ordinateur stocke les `float` en **binaire**, et `0.1` n'a pas de représentation exacte en binaire, de même que 1/3 n'a pas d'écriture décimale exacte (0,3333…). Python stocke donc la valeur la plus proche possible, et les minuscules écarts s'accumulent dans les calculs.

Conséquences :
- pour des **mesures** (distances, températures, statistiques), l'écart est négligeable : `float` convient parfaitement ;
- pour de l'**argent**, c'est inacceptable : une facture doit tomber juste **au centime**.

**Arrondir un `float` avec `round()` ?** La fonction existe, mais elle réserve deux surprises :
```python
>>> round(2.5)        # arrondi « bancaire » : vers le nombre pair le plus proche
2
>>> round(3.5)
4
>>> round(2.675, 2)   # 2.675 est stocké comme 2.67499999…
2.67
```

> Démo : [`demos/03_float_approximatif.py`](demos/03_float_approximatif.md)

---

### 6. `Decimal` : calculer juste avec de l'argent

Le type **`Decimal`** calcule en **base 10**, exactement comme on le fait à la main. Il fait partie de la bibliothèque standard, mais il faut l'**importer** en tête de fichier :

```python
from decimal import Decimal
```
Cette ligne signifie « depuis le module `decimal`, rends disponible `Decimal` ». Les imports sont étudiés en détail au module 12 ; pour l'instant, retenez simplement qu'ils se placent **en haut du fichier**.

**Règle n° 1 : créer un `Decimal` à partir d'un texte**, jamais d'un `float` :
```python
Decimal("0.1")  # ✅ Decimal('0.1')  : exactement 0,1
Decimal(0.1)  # ❌ Decimal('0.1000000000000000055511151231257827021181583404541015625')
```
Un `float` est déjà imprécis : le convertir en `Decimal` conserve l'imprécision. Les entiers ne posent aucun problème : `Decimal(2)`.

**Les calculs sont exacts :**
```python
>>> Decimal("0.1") + Decimal("0.2")
Decimal('0.3')
>>> Decimal("7.50") * 2
Decimal('15.00')
```

**Règle n° 2 : arrondir au centime avec `quantize`**, en précisant la règle d'arrondi :
```python
from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")

vat = Decimal("15.00") * Decimal("0.06")  # Decimal('0.9000')
vat = vat.quantize(CENT, rounding=ROUND_HALF_UP)  # Decimal('0.90')
```
- `quantize(CENT)` arrondit au même nombre de décimales que `CENT`, soit 2 ;
- `ROUND_HALF_UP` est l'arrondi « commercial » : 0,125 donne 0,13. Sans cette option, `Decimal` utilise l'arrondi bancaire (0,125 donne 0,12).

**Règle n° 3 : ne pas mélanger `Decimal` et `float`.** `Decimal("1.5") + 1.5` provoque une `TypeError`. Les `int` sont acceptés.

`Decimal` s'affiche normalement avec `print` et dans les f-strings : `f"{amount:.2f} €"` fonctionne.

> Démo : [`demos/04_decimal.py`](demos/04_decimal.md)

---

### 7. Quelques fonctions utiles

| Fonction | Rôle | Exemple |
|---|---|---|
| `abs(x)` | valeur absolue | `abs(-3)` → `3` |
| `round(x, n)` | arrondi à `n` décimales (voir les pièges ci-dessus) | `round(3.14159, 2)` → `3.14` |
| `min(a, b, …)` / `max(a, b, …)` | plus petite / plus grande valeur | `max(3, 7, 5)` → `7` |

Le module `math` en fournit d'autres, après `import math` :

| Fonction | Rôle | Exemple |
|---|---|---|
| `math.ceil(x)` | arrondi à l'entier **supérieur** | `math.ceil(4.1)` → `5` |
| `math.floor(x)` | arrondi à l'entier **inférieur** | `math.floor(4.9)` → `4` |
| `math.sqrt(x)` | racine carrée | `math.sqrt(16)` → `4.0` |

> 💡 `math.ceil` répond à « combien de cartons faut-il pour 23 livres, 5 par carton ? » : `math.ceil(23 / 5)` donne `5`.

**Lisibilité des grands nombres** : `1_000_000` est identique à `1000000`. Les `_` sont ignorés par Python, mais aident le lecteur.

---

## 🔎 Approfondissement

### Le modulo des nombres négatifs
Python garantit que `a == (a // b) * b + a % b`, et le reste a **le signe du diviseur** :
```python
>>> -7 // 2     # arrondi vers moins l'infini, pas vers zéro
-4
>>> -7 % 2
1
```
D'autres langages (C, Java, JavaScript) donnent `-3` et `-1`. Attention en portant du code.

### `divmod`
`divmod(150, 60)` renvoie les deux résultats d'un coup : `(2, 30)`. Le résultat est un tuple (module 06).

### Les puissances en chaîne
`2 ** 3 ** 2` vaut `512` : `**` se calcule **de droite à gauche**, donc `2 ** 9`.

### IEEE 754 et `math.isclose`
Les `float` suivent la norme IEEE 754 (double précision : environ 15 à 17 chiffres significatifs). Pour comparer deux `float`, on ne teste jamais l'égalité stricte : on utilise `math.isclose(a, b)`. La comparaison est vue au module 03.

### Fractions et notation scientifique
- `from fractions import Fraction` : `Fraction(1, 3) + Fraction(1, 6)` donne `Fraction(1, 2)`, exactement.
- `1e3` vaut `1000.0` (un `float`), `2.5e-3` vaut `0.0025`.

---

## Démos du module

| # | Démo | Notion |
|---|---|---|
| 01 | [operateurs](demos/01_operateurs.md) | Opérateurs, priorités, `+=` |
| 02 | [division_modulo](demos/02_division_modulo.md) | `//` et `%` en situation |
| 03 | [float_approximatif](demos/03_float_approximatif.md) | Imprécision des `float`, pièges de `round` |
| 04 | [decimal](demos/04_decimal.md) | `Decimal`, `quantize`, `ROUND_HALF_UP` |

## Exercices d'entraînement (facultatifs)

| # | Exercice | Difficulté |
|---|---|---|
| 01 | [Durée d'un livre audio](exercices/exo01_duree_audio/enonce.md) | ★ |
| 02 | [Rendre la monnaie](exercices/exo02_rendu_monnaie/enonce.md) | ★★ |
| 03 | [La facture qui ne tombe pas juste](exercices/exo03_facture_float/enonce.md) (piège) | ★★ |

## Fil rouge

➡️ **[Étape 02 de PyBooks : le prix TTC au centime près](../fil-rouge/etape-02/enonce.md)**

## À retenir

- `/` donne toujours un `float` ; `//` et `%` donnent le quotient et le reste de la division entière.
- En cas de doute sur les priorités : des parenthèses.
- `x += 1`, jamais `x++`.
- Les `float` sont **approximatifs** : parfaits pour des mesures, **interdits pour l'argent**.
- Argent : `Decimal("12.90")` (créé à partir d'un **texte**), puis `quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)`.
