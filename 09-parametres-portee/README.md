# Module 09 : paramètres, portée et fonctions comme valeurs

> **Objectifs du module**
> - Concevoir des signatures de fonctions claires : arguments nommés obligatoires, paramètres facultatifs.
> - Accepter un nombre variable d'arguments avec `*args` et `**kwargs`.
> - Comprendre la **portée** des variables : locale, globale, et pourquoi éviter `global`.
> - Manipuler les fonctions comme des valeurs : les passer en argument, écrire des `lambda`, trier avec `key=`.
>
> **Durée indicative** : 3 h
> **Prérequis** : module 08
> **Étape PyBooks** : [09, codes promo et options de commande](../fil-rouge/etape-09/)

---

## L'essentiel

### 1. Positionnel ou nommé : rendre les appels lisibles

```python
create_order(cart, True, False, "LIRE10")  # ❌ que signifient True et False ?
create_order(cart, gift_wrap=True, express=False, promo_code="LIRE10")  # ✅
```

On peut **imposer** le passage par nom avec un `*` dans la signature : tous les paramètres qui le suivent sont **keyword-only**.

```python
def create_order(
    cart: Cart, *, gift_wrap: bool = False, promo_code: str | None = None
) -> Order: ...


create_order(cart, gift_wrap=True)  # ✅
create_order(cart, True)  # ❌ TypeError : gift_wrap doit être nommé
```

> 💡 Règle pratique : un paramètre **booléen** ou une **option** est presque toujours keyword-only. `sorted(titles, reverse=True)` en est un exemple de la bibliothèque standard.

À l'inverse, un `/` rend les paramètres qui le précèdent **positional-only** : ils ne peuvent pas être nommés à l'appel. C'est surtout utile aux auteurs de bibliothèques ; vous le croiserez dans la documentation (`len(obj, /)`).

**L'ordre dans une signature** : `def f(positionnels, /, normaux, *, nommés_uniquement)`, et dans chaque groupe, les paramètres sans valeur par défaut avant ceux qui en ont une.

> Démo : [`demos/01_parametres.py`](demos/01_parametres.md)

---

### 2. Un nombre variable d'arguments : `*args` et `**kwargs`

```python
def total(*amounts: Decimal) -> Decimal:
    """Additionne un nombre quelconque de montants."""
    return sum(amounts, Decimal(0))


total(Decimal("7.50"), Decimal("12.50"), Decimal("6.90"))
```

| Syntaxe | Dans la signature | Reçoit |
|---|---|---|
| `*args` | `def f(*args)` | Les arguments **positionnels** en trop, dans un **tuple** |
| `**kwargs` | `def f(**kwargs)` | Les arguments **nommés** en trop, dans un **dictionnaire** |

Les noms `args` et `kwargs` sont une convention : on peut (et souvent on doit) les nommer selon leur sens, comme `*amounts`.

**À l'appel**, `*` et `**` font l'inverse : ils **déballent** une liste ou un dictionnaire en arguments séparés.
```python
prices = [Decimal("7.50"), Decimal("12.50")]
total(*prices)  # équivaut à total(prices[0], prices[1])

options = {"gift_wrap": True, "promo_code": "LIRE10"}
create_order(cart, **options)  # équivaut à create_order(cart, gift_wrap=True, …)
```

> 💡 `**kwargs` dans une signature est puissant mais opaque : le lecteur ne sait plus quels arguments sont acceptés. On le réserve aux fonctions qui **transmettent** leurs options à une autre fonction.

> Démo : [`demos/02_args_kwargs.py`](demos/02_args_kwargs.md)

---

### 3. La portée des variables

Une variable créée **dans** une fonction est **locale** : elle n'existe que pendant l'appel, et n'est pas visible de l'extérieur. Une variable créée au niveau du fichier est **globale** : elle est visible depuis toutes les fonctions du fichier.

Quand Python rencontre un nom, il le cherche dans cet ordre, la règle **LEGB** :
1. **L**ocal : la fonction en cours ;
2. **E**nclosing : la fonction englobante, quand une fonction est définie dans une autre (approfondissement A4) ;
3. **G**lobal : le fichier ;
4. **B**uilt-in : les noms intégrés de Python (`print`, `len`, `list`…).

**Lire** une variable globale depuis une fonction fonctionne : c'est ainsi que les fonctions utilisent les constantes. **Modifier** une variable globale, en revanche, crée un piège :

```python
orders_count = 0


def record_order() -> None:
    orders_count += 1  # ❌ UnboundLocalError
```
```
UnboundLocalError: cannot access local variable 'orders_count' where it is not associated with a value
```
Parce qu'elle est **affectée** dans la fonction, Python considère `orders_count` comme **locale** sur toute la fonction. L'instruction `+= 1` veut alors lire une variable locale qui n'a pas encore de valeur.

Le mot-clé `global orders_count` permettrait de modifier la globale… mais c'est une **mauvaise pratique** : n'importe quelle fonction peut modifier l'état du programme, et le code devient impossible à suivre et à tester. La bonne solution : **passer** l'état en paramètre et **renvoyer** le résultat.

```python
def record_order(orders_count: int) -> int:
    return orders_count + 1


orders_count = record_order(orders_count)
```

> ⚠️ **Piège : masquer un nom intégré.** Une variable nommée `list`, `sum`, `input` ou `type` **cache** la fonction du même nom pour tout le reste de sa portée. Après `list = ["Dune"]`, l'appel `list("abc")` provoque `TypeError: 'list' object is not callable`.

> Démo : [`demos/03_portee.py`](demos/03_portee.md)

---

### 4. Les fonctions sont des valeurs

Une fonction est un objet comme un autre : on peut la ranger dans une variable, une liste, un dictionnaire, ou la passer en argument.

```python
def by_price(book: Book) -> Decimal:
    return book[2]


sorted(books, key=by_price)  # sorted appelle by_price sur chaque livre
```
On écrit `key=by_price`, **sans parenthèses** : on transmet la fonction elle-même, pas le résultat d'un appel.

**`lambda`** crée une petite fonction anonyme, le temps d'une expression :
```python
sorted(books, key=lambda book: book[2])  # par prix
sorted(books, key=lambda book: (book[1], book[0]))  # par auteur, puis par titre
max(books, key=lambda book: book[2])  # le livre le plus cher
```
`lambda paramètres: expression` équivaut à une fonction qui renvoie `expression`. Elle ne contient qu'**une** expression, sans instruction. Dès que la logique se complique, une fonction nommée, avec sa docstring, est plus lisible.

**Trier selon plusieurs critères** : la clé renvoie un **tuple**, comparé élément par élément. Pour inverser un seul critère numérique, on prend son opposé : `key=lambda book: (-book[2], book[0])` trie par prix **décroissant**, puis par titre.

**Une table de fonctions** remplace une longue suite de `if` :
```python
SORT_KEYS = {
    "t": lambda isbn: CATALOG[isbn][0].lower(),
    "p": lambda isbn: CATALOG[isbn][2],
}
sorted(CATALOG, key=SORT_KEYS[choice])
```

> Démo : [`demos/04_fonctions_valeurs.py`](demos/04_fonctions_valeurs.md)

---

## 🔎 Approfondissement

### `nonlocal` et les closures
Une fonction définie **dans** une autre peut lire les variables de la fonction englobante (le « E » de LEGB), et les modifier avec `nonlocal`. C'est le principe des **closures**, à la base des **décorateurs** (approfondissement A4).

### `functools.partial` et le module `operator`
```python
from functools import partial
from operator import itemgetter

price_with_book_vat = partial(price_with_vat, vat_rate=Decimal("0.06"))
sorted(books, key=itemgetter(2))  # équivaut à key=lambda book: book[2]
```

### Annoter une fonction passée en argument
```python
from collections.abc import Callable


def apply_to_prices(
    prices: list[Decimal], operation: Callable[[Decimal], Decimal]
) -> list[Decimal]:
    return [operation(price) for price in prices]
```
`Callable[[Decimal], Decimal]` signifie « une fonction qui reçoit un `Decimal` et renvoie un `Decimal` ».

### Le piège de la liaison tardive
```python
multipliers = [lambda x: x * factor for factor in range(3)]
[m(10) for m in multipliers]  # [20, 20, 20] et non [0, 10, 20] !
```
Une `lambda` lit `factor` **au moment de son appel**, quand la boucle est terminée et que `factor` vaut 2.

---

## Démos du module

| # | Démo | Notion |
|---|---|---|
| 01 | [parametres](demos/01_parametres.md) | Positionnel, nommé, keyword-only, positional-only |
| 02 | [args_kwargs](demos/02_args_kwargs.md) | `*args`, `**kwargs`, déballage à l'appel |
| 03 | [portee](demos/03_portee.md) | LEGB, `UnboundLocalError`, masquage |
| 04 | [fonctions_valeurs](demos/04_fonctions_valeurs.md) | Fonctions en argument, `lambda`, `key=`, table de fonctions |

## Exercices d'entraînement (facultatifs)

| # | Exercice | Difficulté |
|---|---|---|
| 01 | [Statistiques à la demande](exercices/exo01_statistiques/enonce.md) | ★ |
| 02 | [Le classement des ventes](exercices/exo02_classement/enonce.md) | ★★ |
| 03 | [Le compteur fantôme](exercices/exo03_portee_piege/enonce.md) (piège) | ★★ |

## Fil rouge

➡️ **[Étape 09 de PyBooks : codes promo et options de commande](../fil-rouge/etape-09/enonce.md)**

## À retenir

- Les options et booléens sont **keyword-only** : `def f(x, *, option=False)`.
- `*args` reçoit un tuple, `**kwargs` un dictionnaire ; à l'appel, `*liste` et `**dico` déballent.
- LEGB : local, englobant, global, intégré. Affecter une variable dans une fonction la rend **locale**.
- Pas de `global` : on passe l'état en paramètre et on renvoie le résultat.
- Une fonction est une valeur : `key=fonction`, sans parenthèses ; `lambda x: expression` pour les cas simples.
