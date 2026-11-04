# Module 06 : listes et tuples

> **Objectifs du module**
> - Stocker un nombre variable d'éléments dans une **liste**, et la modifier.
> - Parcourir, agréger (`sum`, `min`, `max`) et trier une liste.
> - Regrouper quelques valeurs liées dans un **tuple**, et les « déballer ».
> - Comprendre qu'une variable désigne une liste sans la copier (**aliasing**), et éviter les pièges qui en découlent.
>
> **Durée indicative** : 3 h 30 (listes et tuples)
> **Prérequis** : module 05
> **Étape PyBooks** : [06, le catalogue et le panier](../fil-rouge/etape-06/)

---

## L'essentiel

### 1. Créer et lire une liste

Une **liste** est une suite **ordonnée** d'éléments, écrite entre crochets :

```python
titles = ["Le Petit Prince", "L'Étranger", "Dune"]
prices = [7.50, 6.90, 12.50]
empty_cart = []
```

Une liste se lit comme un texte (module 05) : même indexation, même slicing, même `len`, même `in`.

```python
titles[0]  # "Le Petit Prince"
titles[-1]  # "Dune"
titles[:2]  # ["Le Petit Prince", "L'Étranger"]
len(titles)  # 3
"Dune" in titles  # True
```

Une liste peut contenir n'importe quoi : des nombres, des textes, d'autres listes, des tuples… En pratique, on y met des éléments **de même nature** : une liste de titres, une liste de prix.

### 2. Une liste est modifiable

Contrairement à un texte, une liste est **mutable** : on peut la modifier sans en créer une nouvelle.

| Opération | Effet |
|---|---|
| `titles[1] = "La Peste"` | Remplace l'élément d'indice 1 |
| `titles.append("Dune")` | Ajoute **à la fin** |
| `titles.insert(0, "Ulysse")` | Insère à l'indice 0 (décale les suivants) |
| `titles.extend(["A", "B"])` | Ajoute **tous** les éléments d'une autre liste |
| `titles.remove("Dune")` | Retire la **première** occurrence (`ValueError` si absente) |
| `titles.pop()` | Retire et **renvoie** le dernier élément |
| `titles.pop(0)` | Retire et renvoie l'élément d'indice 0 |
| `del titles[0]` | Supprime l'élément d'indice 0 |
| `titles.clear()` | Vide la liste |
| `titles.index("Dune")` | Indice de la première occurrence (`ValueError` si absente) |
| `titles.count("Dune")` | Nombre d'occurrences |

> ⚠️ **Piège** : ces méthodes **modifient la liste et renvoient `None`** (sauf `pop`, `index` et `count`). `titles = titles.append("Dune")` remplace donc la liste par `None` ! C'est l'inverse des méthodes de `str`, qui renvoient un nouveau texte.

> Démo : [`demos/01_listes.py`](demos/01_listes.md)

---

### 3. Parcourir, agréger, trier

```python
for title in titles:
    print(title)
```

**Avec l'indice** : `enumerate` fournit, à chaque tour, la position **et** l'élément.
```python
for number, title in enumerate(titles, start=1):
    print(f"{number}. {title}")  # 1. Le Petit Prince, 2. L'Étranger…
```
C'est la façon idiomatique de numéroter, au lieu de `for index in range(len(titles))`.

**Agréger** une liste de nombres :

| Fonction | Résultat |
|---|---|
| `sum(prices)` | La somme (`0` pour une liste vide) |
| `min(prices)` / `max(prices)` | Le plus petit / le plus grand (`ValueError` si la liste est vide) |
| `len(prices)` | Le nombre d'éléments |

**Trier** :

| Écriture | Effet |
|---|---|
| `sorted(titles)` | Renvoie une **nouvelle** liste triée ; l'originale est inchangée |
| `titles.sort()` | Trie la liste **elle-même** (et renvoie `None`) |
| `sorted(titles, reverse=True)` | Ordre décroissant |
| `sorted(titles, key=str.lower)` | Trie selon le résultat de `str.lower` pour chaque élément : sans tenir compte de la casse |
| `sorted(titles, key=len)` | Trie par longueur |

`key=` reçoit une **fonction** appliquée à chaque élément ; le tri se fait sur les résultats. On écrira nos propres fonctions de tri au module 09.

**Découper et assembler du texte** : deux méthodes de `str` font le pont avec les listes.
```python
"Hugo;Camus;Herbert".split(";")  # ["Hugo", "Camus", "Herbert"]
"  le petit   prince ".split()  # ["le", "petit", "prince"] : sans argument, découpe sur les espaces
", ".join(["Hugo", "Camus"])  # "Hugo, Camus"
```

> Démo : [`demos/02_parcours_tri.py`](demos/02_parcours_tri.md)

---

### 4. Les tuples

Un **tuple** est une suite ordonnée **immuable**, écrite entre parenthèses :
```python
book = ("9782070612758", "Le Petit Prince", 7.50)
book[1]  # "Le Petit Prince"
book[1] = "X"  # TypeError: 'tuple' object does not support item assignment
```

**Liste ou tuple ?**

| | Liste | Tuple |
|---|---|---|
| Modifiable | Oui | Non |
| Usage typique | Une **collection** d'éléments de même nature, dont le nombre varie | Un **enregistrement** : quelques valeurs liées, de natures différentes, en nombre fixe |
| Exemple | La liste des titres du catalogue | Un livre : (ISBN, titre, prix) ; une ligne de panier : (ISBN, quantité) |

> ⚠️ **Piège** : `(7)` est simplement le nombre 7 entre parenthèses. Un tuple d'**un** élément s'écrit avec une virgule : `(7,)`. C'est la **virgule** qui fait le tuple, pas les parenthèses : `book = "978…", "Le Petit Prince", 7.50` est aussi un tuple.

**Le déballage (*unpacking*)** : on affecte chaque élément d'un tuple (ou d'une liste) à une variable, en une ligne.
```python
isbn, title, price = book  # autant de variables que d'éléments
first, second = second, first  # échange de deux valeurs (module 01, approfondissement)
```
Il s'utilise naturellement dans un `for` qui parcourt une liste de tuples :
```python
cart = [("Le Petit Prince", 2), ("Dune", 1)]
for title, quantity in cart:
    print(f"{quantity} x {title}")
```

**Le retour du `or` du module 03** : avec un tuple, la forme courte est enfin disponible.
```python
if answer in ("o", "oui"):       # au lieu de answer == "o" or answer == "oui"
```

> Démo : [`demos/03_tuples.py`](demos/03_tuples.md)

---

### 5. L'aliasing : deux noms, une seule liste

```python
cart = ["Dune"]
saved_cart = cart  # ⚠️ ne copie PAS la liste
saved_cart.append("Ulysse")
print(cart)  # ['Dune', 'Ulysse'] : cart a « changé » aussi !
```

Rappel du module 01 : une variable est une **étiquette** collée sur un objet. `saved_cart = cart` colle une deuxième étiquette sur **la même** liste. Avec un objet immuable (texte, nombre), cela n'a aucune conséquence visible ; avec une liste, toute modification par un nom est visible par l'autre.

Pour obtenir une **copie** indépendante :
```python
saved_cart = cart.copy()  # ou list(cart), ou cart[:]
```

`==` compare le **contenu**, `is` teste s'il s'agit du **même objet** :
```python
cart == cart.copy()  # True : même contenu
cart is cart.copy()  # False : deux listes distinctes
```

> ⚠️ **Piège : modifier une liste pendant qu'on la parcourt.**
> ```python
> titles = ["A", "B", "C", "D"]
> for title in titles:
>     if title in ("B", "C"):
>         titles.remove(title)
> print(titles)        # ['A', 'C', 'D'] : "C" a été sauté !
> ```
> En retirant `"B"`, les éléments suivants se décalent, et la boucle saute le suivant. Règle : on ne modifie pas une liste qu'on est en train de parcourir. On construit une **nouvelle** liste avec les éléments à garder (module 07, compréhensions), ou l'on parcourt une copie : `for title in titles.copy():`.

> Démo : [`demos/04_aliasing.py`](demos/04_aliasing.md)

---

## 🔎 Approfondissement

### Le déballage étendu
```python
first, *others = [
    "Dune",
    "Ulysse",
    "Hamlet",
]  # first = "Dune", others = ["Ulysse", "Hamlet"]
*others, last = ["Dune", "Ulysse", "Hamlet"]  # last = "Hamlet"
```

### `zip` : parcourir plusieurs listes en parallèle
```python
for title, price in zip(titles, prices, strict=True):
    print(title, price)
```
`strict=True` (Python 3.10+) lève une erreur si les listes n'ont pas la même longueur, au lieu de s'arrêter silencieusement à la plus courte.

### Le piège de la liste de listes
`grid = [[0] * 3] * 3` crée **trois références** à la **même** liste intérieure : modifier `grid[0][0]` modifie les trois lignes. Cf. l'approfondissement A2 sur le modèle objet.

### Complexité
Ajouter ou retirer **à la fin** d'une liste (`append`, `pop()`) est immédiat, quelle que soit sa taille. Insérer ou retirer **au début** (`insert(0, …)`, `pop(0)`) oblige à décaler tous les éléments : c'est lent pour de très grandes listes. Pour une file d'attente, la bibliothèque standard propose `collections.deque`.

### `match` sur des séquences
```python
match command.split():
    case ["ajouter", isbn]:
        ...
    case ["ajouter", isbn, quantity]:
        ...
    case ["quitter"]:
        ...
```
`match` reconnaît la **forme** d'une liste et en extrait directement les éléments.

---

## Démos du module

| # | Démo | Notion |
|---|---|---|
| 01 | [listes](demos/01_listes.md) | Créer, lire, modifier une liste |
| 02 | [parcours_tri](demos/02_parcours_tri.md) | `for`, `enumerate`, `sum`/`min`/`max`, tri, `split`/`join` |
| 03 | [tuples](demos/03_tuples.md) | Tuples, déballage, listes de tuples |
| 04 | [aliasing](demos/04_aliasing.md) | Références, copies, modification pendant un parcours |

## Exercices d'entraînement (facultatifs)

| # | Exercice | Difficulté |
|---|---|---|
| 01 | [Ma liste de lecture](exercices/exo01_liste_lecture/enonce.md) | ★ |
| 02 | [Les notes des lecteurs](exercices/exo02_notes_lecteurs/enonce.md) | ★★ |
| 03 | [Le panier fantôme](exercices/exo03_panier_fantome/enonce.md) (piège) | ★★ |

## Fil rouge

➡️ **[Étape 06 de PyBooks : le catalogue et le panier](../fil-rouge/etape-06/enonce.md)**

## À retenir

- Liste : `[a, b, c]`, ordonnée, **modifiable**. `append`, `insert`, `remove`, `pop`… modifient la liste et renvoient `None`.
- `for x in liste`, `for i, x in enumerate(liste, start=1)`.
- `sorted(liste)` renvoie une nouvelle liste ; `liste.sort()` trie sur place. `key=` choisit le critère.
- Tuple : `(a, b, c)`, **immuable**, pour un enregistrement de quelques valeurs liées. `(x,)` pour un seul élément.
- Déballage : `isbn, title, price = book` ; `for title, quantity in cart`.
- `b = a` ne copie pas une liste : `b = a.copy()`. Ne jamais modifier une liste qu'on parcourt.
