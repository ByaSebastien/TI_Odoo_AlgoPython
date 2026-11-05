# Module 07 : dictionnaires, ensembles et compréhensions

> **Objectifs du module**
> - Associer des **clés** à des **valeurs** avec un dictionnaire, et retrouver une valeur instantanément.
> - Compter, regrouper et imbriquer des données avec des dictionnaires.
> - Éliminer les doublons et comparer des collections avec les **ensembles**.
> - Écrire des **compréhensions** pour construire une liste, un dictionnaire ou un ensemble en une ligne.
>
> **Durée indicative** : 3 h
> **Prérequis** : module 06
> **Étape PyBooks** : [07, le catalogue indexé par ISBN](../fil-rouge/etape-07/)

---

## L'essentiel

### 1. Le dictionnaire : des clés et des valeurs

Une liste retrouve un élément par sa **position**. Un **dictionnaire** retrouve une **valeur** par sa **clé** :

```python
stocks = {
    "9782070612758": 7,  # clé : l'ISBN ; valeur : le stock
    "9782266320320": 12,
}
```

| Opération | Exemple | Effet |
|---|---|---|
| Lire | `stocks["9782070612758"]` | `7` ; `KeyError` si la clé est absente |
| Lire avec défaut | `stocks.get(isbn, 0)` | La valeur, ou `0` si la clé est absente |
| Ajouter ou modifier | `stocks[isbn] = 5` | Crée la clé si elle n'existe pas, sinon remplace la valeur |
| Supprimer | `del stocks[isbn]` / `stocks.pop(isbn)` | `pop` renvoie la valeur supprimée |
| Tester une clé | `isbn in stocks` | `True` si la **clé** existe (pas la valeur !) |
| Taille | `len(stocks)` | Nombre de couples clé-valeur |

**Pourquoi c'est si utile** : retrouver une valeur par sa clé est **immédiat**, quelle que soit la taille du dictionnaire. Avec une liste, il faut parcourir les éléments un par un : avec un million de livres, la différence est énorme.

**Les règles des clés** :
- une clé est **unique** : réaffecter une clé existante remplace sa valeur ;
- une clé doit être **immuable** : un texte, un nombre, un tuple… mais pas une liste (`TypeError: cannot use 'list' as a dict key`) ;
- les valeurs, elles, peuvent être n'importe quoi.

Un dictionnaire conserve l'**ordre d'insertion** des clés (garanti depuis Python 3.7).

> ⚠️ **Piège** : `stocks["inconnu"]` provoque une `KeyError`, qui arrête le programme. Si la clé peut manquer, testez avec `in`, ou utilisez `get` avec une valeur par défaut.

> Démo : [`demos/01_dictionnaires.py`](demos/01_dictionnaires.md)

---

### 2. Parcourir un dictionnaire

```python
for isbn in stocks:  # les clés
    ...
for quantity in stocks.values():  # les valeurs
    ...
for isbn, quantity in stocks.items():  # les couples (clé, valeur), à déballer
    print(f"{isbn} : {quantity}")
```

`.items()` est la forme la plus utilisée : on dispose à la fois de la clé et de la valeur.

> ⚠️ **Piège** : ajouter ou supprimer des clés **pendant** le parcours d'un dictionnaire provoque `RuntimeError: dictionary changed size during iteration`. Comme pour les listes, on construit un nouveau dictionnaire, ou l'on parcourt une copie : `for isbn in list(stocks):`.

### 3. Deux schémas incontournables

**Compter** :
```python
counts = {}
for category in ["roman", "sf", "roman", "classique", "roman"]:
    counts[category] = counts.get(category, 0) + 1
# {'roman': 3, 'sf': 1, 'classique': 1}
```
`get(category, 0)` renvoie le compte actuel, ou 0 la première fois.

**Regrouper** :
```python
titles_by_author = {}
for title, author in books:
    if author not in titles_by_author:
        titles_by_author[author] = []
    titles_by_author[author].append(title)
```

**Imbriquer** : une valeur peut être une liste, un tuple, un autre dictionnaire…
```python
catalog = {
    "9782070612758": ("Le Petit Prince", "Antoine de Saint-Exupéry", Decimal("7.50")),
}
title, author, price = catalog["9782070612758"]
```

> Démo : [`demos/02_compter_regrouper.py`](demos/02_compter_regrouper.md)

---

### 4. Les ensembles

Un **ensemble** (`set`) est une collection **sans doublons** et **sans ordre** :

```python
categories = {"roman", "classique", "roman"}  # {'roman', 'classique'}
empty = set()  # ⚠️ {} est un dictionnaire vide !
```

| Opération | Effet |
|---|---|
| `categories.add("sf")` | Ajoute (sans effet si déjà présent) |
| `categories.discard("sf")` | Retire, sans erreur si absent (`remove` lève une `KeyError`) |
| `"sf" in categories` | Test d'appartenance **immédiat**, comme pour les clés d'un dictionnaire |
| `set(une_liste)` | Élimine les doublons d'une liste (l'ordre est perdu) |

Et les opérations de la théorie des ensembles :

| Opération | Écriture | Résultat pour `{"roman", "classique"}` et `{"classique", "sf"}` |
|---|---|---|
| Union | `a \| b` | `{"roman", "classique", "sf"}` |
| Intersection | `a & b` | `{"classique"}` |
| Différence | `a - b` | `{"roman"}` |
| Différence symétrique | `a ^ b` | `{"roman", "sf"}` |

> 💡 Un ensemble n'a pas d'ordre : on ne peut pas écrire `categories[0]`, et l'ordre d'affichage peut varier. Pour un affichage stable : `sorted(categories)`.

> Démo : [`demos/03_ensembles.py`](demos/03_ensembles.md)

---

### 5. Les compréhensions

Construire une collection à partir d'une autre est si fréquent que Python offre une syntaxe dédiée, la **compréhension** :

```python
# Avec une boucle
prices_incl_vat = []
for price in prices:
    prices_incl_vat.append(price * (1 + VAT_RATE))

# Avec une compréhension : même résultat
prices_incl_vat = [price * (1 + VAT_RATE) for price in prices]
```

On la lit : « la liste des `price * (1 + VAT_RATE)` pour chaque `price` de `prices` ».

**Avec un filtre** :
```python
cheap_titles = [title for title, price in books if price < 10]
```

**Les trois formes** :

| Forme | Syntaxe | Produit |
|---|---|---|
| Liste | `[expr for x in source if condition]` | une liste |
| Dictionnaire | `{key: value for x in source if condition}` | un dictionnaire |
| Ensemble | `{expr for x in source if condition}` | un ensemble |

```python
stocks_by_title = {title: stock for title, stock in rows}
authors = {author for _title, author in books}
```

**Une compréhension remplace aussi la suppression pendant un parcours** (module 06) :
```python
titles = [title for title in titles if title not in out_of_stock]
```

> 💡 Une compréhension doit rester **lisible**. Dès qu'elle déborde sur plusieurs lignes, imbrique plusieurs `for`, ou a besoin de commentaires, une boucle classique est préférable.

> Démo : [`demos/04_comprehensions.py`](demos/04_comprehensions.md)

---

## 🔎 Approfondissement

### `defaultdict` et `Counter`
Le module `collections` simplifie les deux schémas de la section 3 :
```python
from collections import Counter, defaultdict

counts = Counter(["roman", "sf", "roman"])  # Counter({'roman': 2, 'sf': 1})
counts.most_common(1)  # [('roman', 2)]

titles_by_author = defaultdict(list)  # valeur par défaut : une liste vide
titles_by_author["Hugo"].append("Les Misérables")  # pas besoin de tester la clé
```

### Fusionner des dictionnaires
`defaults | user_settings` crée un nouveau dictionnaire : en cas de clé commune, c'est la valeur de droite qui l'emporte. `settings |= other` met à jour sur place.

### `frozenset` et hashabilité
Une clé de dictionnaire, ou un élément d'ensemble, doit être **hashable** : sa valeur ne doit jamais changer, car Python calcule à partir d'elle une empreinte (le *hash*) qui sert à le retrouver instantanément. C'est pourquoi les listes, les dictionnaires et les ensembles ne peuvent pas être des clés. `frozenset` est la version immuable, donc hashable, d'un ensemble.

### `match` sur des dictionnaires
```python
match order:
    case {"isbn": isbn, "quantity": quantity} if quantity > 0:
        ...
```

### Compréhensions imbriquées et expressions génératrices
`[x * y for x in range(3) for y in range(3)]` imbrique deux boucles. Et `sum(price for price in prices)`, sans crochets, est une **expression génératrice** : elle produit les valeurs une à une sans construire de liste en mémoire (approfondissement A3).

🆕 **Nouveauté 3.15** : on peut déballer dans une compréhension : `[*sous_liste for sous_liste in listes]` aplatit une liste de listes.

---

## Démos du module

| # | Démo | Notion |
|---|---|---|
| 01 | [dictionnaires](demos/01_dictionnaires.md) | Créer, lire, modifier, parcourir un dictionnaire |
| 02 | [compter_regrouper](demos/02_compter_regrouper.md) | Compter, regrouper, imbriquer |
| 03 | [ensembles](demos/03_ensembles.md) | `set`, doublons, opérations ensemblistes |
| 04 | [comprehensions](demos/04_comprehensions.md) | Compréhensions de liste, de dictionnaire, d'ensemble |

## Exercices d'entraînement (facultatifs)

| # | Exercice | Difficulté |
|---|---|---|
| 01 | [L'inventaire](exercices/exo01_inventaire/enonce.md) | ★ |
| 02 | [Les mots les plus fréquents](exercices/exo02_frequence_mots/enonce.md) | ★★ |
| 03 | [Le programme qui plante trois fois](exercices/exo03_pieges_dict/enonce.md) (piège) | ★★ |

## Fil rouge

➡️ **[Étape 07 de PyBooks : le catalogue indexé par ISBN](../fil-rouge/etape-07/enonce.md)**

## À retenir

- Dictionnaire : `{clé: valeur}` ; `d[clé]` (ou `KeyError`), `d.get(clé, défaut)`, `clé in d`, `for clé, valeur in d.items()`.
- Les clés sont uniques et immuables ; l'ordre d'insertion est conservé.
- Compter : `counts[k] = counts.get(k, 0) + 1`.
- Ensemble : `{a, b}` ou `set()` (jamais `{}`), sans doublons, sans ordre ; `|`, `&`, `-`.
- Compréhensions : `[expr for x in source if condition]`, et leurs variantes `{k: v …}` et `{expr …}`.
- Ne jamais ajouter ou supprimer des clés pendant le parcours d'un dictionnaire.
