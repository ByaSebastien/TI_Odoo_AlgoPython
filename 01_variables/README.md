# Module 01 : variables et types simples

> **Objectifs du module**
> - Stocker des valeurs dans des **variables** bien nommées.
> - Connaître les types de base : nombres entiers, nombres à virgule, texte, booléens et `None`.
> - Afficher des résultats lisibles avec `print` et les **f-strings**.
> - Demander une information à l'utilisateur avec `input`, et la **convertir**.
>
> **Durée indicative** : 3 h
> **Prérequis** : module 00
> **Étape PyBooks** : [01, la fiche d'un livre](../fil-rouge/etape-01/)

---

## L'essentiel

### 1. Qu'est-ce qu'une variable ?

Une **variable** est un **nom** qui désigne une **valeur**. On la crée par une **affectation**, avec le signe `=` :

```python
title = "Le Petit Prince"
price = 12.90
stock = 7
```

On lit `title = "Le Petit Prince"` ainsi : « le nom `title` désigne désormais le texte *Le Petit Prince* ».
Ensuite, partout où l'on écrit le nom, Python utilise la valeur :

```python
print(title)  # Le Petit Prince
print(price * 2)  # 25.8
```

> ⚠️ **Piège** : en Python, `=` **n'est pas** l'égalité mathématique, c'est l'**affectation** : « donne ce nom à cette valeur ». Pour **comparer** deux valeurs, on utilisera `==`, au module 03.

**Réaffecter** une variable, c'est lui faire désigner une nouvelle valeur. L'ancienne est oubliée :

```python
stock = 7
stock = 6  # un exemplaire vendu
print(stock)  # 6
stock = stock - 1  # on calcule d'abord la droite (6 - 1), puis on affecte
print(stock)  # 5
```

L'instruction `stock = stock - 1` choque souvent au début : elle est absurde en mathématiques, mais parfaitement logique en programmation. Python **calcule d'abord** l'expression de droite avec l'ancienne valeur, **puis** affecte le résultat au nom de gauche.

Utiliser une variable qui n'a jamais reçu de valeur provoque une erreur :
```
NameError: name 'stok' is not defined. Did you mean: 'stock'?
```

> Démo : [`demos/01_variables.py`](demos/01_variables.md)

---

### 2. Bien nommer ses variables

**Les règles** (sinon, erreur de syntaxe) :
- lettres, chiffres et `_` uniquement ;
- **pas de chiffre au début** : `book2` est valide, `2book` ne l'est pas ;
- Python distingue les **majuscules et minuscules** : `price` et `Price` sont deux variables différentes ;
- pas de **mot réservé** du langage : `if`, `for`, `class`, `True`, `None`… (35 au total, voir l'approfondissement).

**Les conventions du cours** (voir [CONVENTIONS.md](../CONVENTIONS.md)) :

| Convention | Exemple |
|---|---|
| Variables en `snake_case` : minuscules, mots séparés par `_` | `unit_price`, `book_title` |
| Noms **en anglais** et **explicites** | `quantity` plutôt que `q` ou `qte` |
| **Constantes** en `UPPER_SNAKE_CASE` | `VAT_RATE = 0.06` |
| Ne jamais réutiliser un nom de Python | pas de variable nommée `print`, `input`, `type`, `str`… |

**Les constantes.** Une valeur qui ne doit pas changer pendant le programme, et qui a un **sens métier**, devient une constante nommée en majuscules, en tête de fichier :

```python
VAT_RATE = 0.06
FREE_SHIPPING_THRESHOLD = 50

price_with_vat = price * (1 + VAT_RATE)  # ✅ on comprend ce qui est calculé
price_with_vat = price * 1.06  # ❌ « nombre magique » : d'où vient 1.06 ?
```

Python n'empêche pas de modifier une constante : les majuscules sont une **convention**, que tout développeur respecte.

> ⚠️ **Piège** : nommer une variable `input` ou `print` « casse » la fonction du même nom pour la suite du programme. Après `print = "bonjour"`, l'instruction `print("x")` provoque `TypeError: 'str' object is not callable`.

---

### 3. Les types de base

Toute valeur a un **type**, qui détermine ce qu'on peut faire avec elle. La fonction `type()` l'indique :

| Type | Nom | Exemples | Remarques |
|---|---|---|---|
| `int` | nombre entier | `7`, `-3`, `1200` | Aussi grand qu'on veut |
| `float` | nombre à virgule | `12.90`, `0.06`, `-1.5` | Le séparateur est le **point** |
| `str` | texte (*string*, chaîne de caractères) | `"Le Petit Prince"`, `'abc'`, `""` | Entre guillemets ; `""` est le texte vide |
| `bool` | booléen | `True`, `False` | Avec une **majuscule** |
| `NoneType` | absence de valeur | `None` | Avec une **majuscule** |

```python
>>> type(7)
<class 'int'>
>>> type(12.90)
<class 'float'>
>>> type("7")
<class 'str'>
>>> type(True)
<class 'bool'>
>>> type(None)
<class 'NoneType'>
```

Quelques points essentiels :
- `7` et `"7"` sont **différents** : un nombre et un texte qui contient le caractère 7.
- Une division `/` donne **toujours** un `float` : `10 / 5` vaut `2.0`.
- `None` signifie « pas de valeur » : par exemple, un livre qui n'a **pas encore** de date de parution. Ce n'est ni `0`, ni `""`.
- Les booléens servent à exprimer un état vrai ou faux : `is_ebook = True`. Ils prennent tout leur sens au module 03, avec les conditions.

**Typage dynamique et fort.** En Python, le type est porté par la **valeur**, pas par la variable : un même nom peut désigner un entier, puis un texte. On dit que le typage est **dynamique**. En revanche, Python refuse les mélanges hasardeux : `"Total : " + 12` est une erreur (`TypeError`), et non `"Total : 12"`. On dit que le typage est **fort**.

> 💡 Même si Python l'autorise, changer le type d'une variable en cours de route rend le code difficile à suivre. Une variable garde **un seul type** : c'est une bonne pratique, que les outils de vérification du module 13 imposeront.

> Démo : [`demos/02_types.py`](demos/02_types.md)

---

### 4. Afficher : `print` et les f-strings

Rappel du module 00 : `print` affiche ses éléments séparés par un espace, puis passe à la ligne.
Deux options permettent d'ajuster ce comportement :

```python
print("A", "B", "C", sep=" | ")  # A | B | C        (séparateur personnalisé)
print("Chargement", end="...")  # pas de retour à la ligne, mais "..." à la place
print("terminé")  # Chargement...terminé
```

Pour construire un texte avec des valeurs, on utilise une **f-string** : un texte précédé de la lettre `f`, dans lequel chaque expression entre **accolades** est remplacée par sa valeur.

```python
title = "Le Petit Prince"
price = 12.9

print(f"{title} coûte {price} €")  # Le Petit Prince coûte 12.9 €
print(f"Deux exemplaires : {price * 2} €")  # on peut calculer dans les accolades
```

Pour afficher un nombre avec **exactement deux décimales**, on ajoute `:.2f` après l'expression :

```python
print(f"Prix : {price:.2f} €")  # Prix : 12.90 €
print(f"Un tiers : {1 / 3:.2f}")  # Un tiers : 0.33
```

`:.2f` signifie : « nombre à virgule (`f`), avec 2 chiffres après la virgule (`.2`) ». La valeur est **arrondie pour l'affichage**, mais la variable n'est pas modifiée.

> ⚠️ **Piège** : oublier le `f` devant les guillemets. `print("Prix : {price}")` affiche littéralement `Prix : {price}`.

> Démo : [`demos/04_fstrings.py`](demos/04_fstrings.md)

---

### 5. Saisir : `input` et les conversions

`input` affiche un message, attend que l'utilisateur tape quelque chose puis appuie sur Entrée, et **renvoie le texte saisi** :

```python
name = input("Votre prénom : ")
print(f"Bonjour {name} !")
```
```
Votre prénom : Ada
Bonjour Ada !
```

> ⚠️ **Piège majeur** : `input` renvoie **toujours** un texte (`str`), même si l'utilisateur tape un nombre.
> ```python
> quantity = input("Quantité : ")   # l'utilisateur tape 3
> print(quantity * 2)               # affiche 33 : le texte "3" répété deux fois !
> ```

Pour obtenir un nombre, il faut **convertir** le texte :

| Conversion | Exemple | Résultat |
|---|---|---|
| `int(texte)` | `int("3")` | `3` |
| `float(texte)` | `float("12.5")` | `12.5` |
| `str(valeur)` | `str(42)` | `"42"` |
| `int(nombre_à_virgule)` | `int(12.9)` | `12` : la partie décimale est **tronquée**, pas arrondie |

```python
quantity = int(input("Quantité : "))  # on convertit dès la saisie
print(quantity * 2)  # 6
```

Si le texte ne représente pas un nombre valide, la conversion échoue :
```
>>> int("trois")
ValueError: invalid literal for int() with base 10: 'trois'
>>> int("12.5")
ValueError: invalid literal for int() with base 10: '12.5'
```
Pour l'instant, le programme s'arrête sur cette erreur. Au module 10, nous apprendrons à la gérer pour redemander une saisie correcte.

> 💡 `float()` exige un **point** : `float("12,5")` échoue. Pensez-y dans les messages de saisie : `"Prix (ex. 12.90) : "`.

> Démo : [`demos/03_saisie_conversions.py`](demos/03_saisie_conversions.md)

---

## 🔎 Approfondissement

### Une variable est une étiquette, pas une boîte
On représente souvent une variable comme une « boîte » qui contient une valeur. L'image exacte, en Python, est celle d'une **étiquette** collée sur un objet : `a = b` ne copie rien, il colle une deuxième étiquette sur le **même** objet. La fonction `id()` donne l'identité d'un objet :
```python
>>> a = "Python"
>>> b = a
>>> id(a) == id(b)
True
```
Cette distinction ne change rien pour les nombres et les textes, mais devient **cruciale** avec les listes (module 06). Elle est développée dans l'approfondissement [A2, modèle objet et mémoire](../approfondissements/).

### Affectations multiples
```python
title, author = "Le Petit Prince", "Saint-Exupéry"  # deux variables en une ligne
first, second = second, first  # échange de deux valeurs
```
Le mécanisme (le « déballage ») est expliqué au module 06.

### Les mots réservés
`help("keywords")` dans le REPL affiche les 35 mots réservés de Python 3.14. Quatre autres mots (`match`, `case`, `type`, `_`) sont des **mots-clés contextuels** : réservés seulement dans certaines constructions, on peut les utiliser comme noms ailleurs… mais c'est déconseillé.

### `print` ou représentation ?
Dans le REPL, `>>> title` affiche `'Le Petit Prince'`, avec des guillemets, alors que `print(title)` affiche `Le Petit Prince`. Le REPL montre la **représentation** de la valeur : la forme qu'on écrirait dans le code. Dans une f-string, `!r` produit cette représentation, et `=` affiche aussi le nom de l'expression, ce qui est très pratique pour déboguer :
```python
>>> price = 12.9
>>> print(f"{title!r}")
'Le Petit Prince'
>>> print(f"{price=}")
price=12.9
```

### `int` sans limite
Un `int` Python n'a pas de taille maximale : `2 ** 200` donne un nombre exact de 61 chiffres. Seule la mémoire de l'ordinateur limite sa taille.

---

## Démos du module

| # | Démo | Notion |
|---|---|---|
| 01 | [variables](demos/01_variables.md) | Affectation, réaffectation, constantes |
| 02 | [types](demos/02_types.md) | `int`, `float`, `str`, `bool`, `None`, `type()` |
| 03 | [saisie_conversions](demos/03_saisie_conversions.md) | `input`, `int()`, `float()`, `str()` |
| 04 | [fstrings](demos/04_fstrings.md) | f-strings, `:.2f`, `sep`, `end` |

## Exercices d'entraînement (facultatifs)

| # | Exercice | Difficulté |
|---|---|---|
| 01 | [Temps de lecture](exercices/exo01_temps_lecture/enonce.md) | ★ |
| 02 | [L'addition qui concatène](exercices/exo02_addition_piege/enonce.md) (piège) | ★ |

## Fil rouge

➡️ **[Étape 01 de PyBooks : la fiche d'un livre](../fil-rouge/etape-01/enonce.md)**

## À retenir

- `name = value` **affecte** une valeur à un nom ; l'expression de droite est calculée en premier.
- Noms en `snake_case`, en anglais, explicites ; constantes en `UPPER_SNAKE_CASE`.
- Cinq types de base : `int`, `float`, `str`, `bool`, `None`. `type(valeur)` donne le type.
- f-string : `f"Prix : {price:.2f} €"`.
- `input` renvoie **toujours** un `str` : on convertit avec `int()` ou `float()`.
