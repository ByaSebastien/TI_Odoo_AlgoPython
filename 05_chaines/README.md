# Module 05 : chaînes de caractères

> **Objectifs du module**
> - Accéder aux caractères d'un texte par leur position (indexation), et en extraire des morceaux (*slicing*).
> - Comprendre qu'un texte est **immuable**.
> - Utiliser les méthodes essentielles : nettoyer, transformer, rechercher, tester.
> - Mettre en forme un texte avec précision grâce au mini-langage des f-strings : largeur, alignement, décimales.
> - Parcourir un texte caractère par caractère pour l'analyser.
>
> **Durée indicative** : 3 h 30
> **Prérequis** : module 04
> **Étape PyBooks** : [05, ISBN et ticket de caisse](../fil-rouge/etape-05/)

---

## L'essentiel

### 1. Écrire un texte

| Écriture | Usage |
|---|---|
| `"texte"` ou `'texte'` | Cas courant. On choisit l'un ou l'autre selon les guillemets contenus dans le texte. |
| `"""texte sur plusieurs lignes"""` | Texte long, docstring |
| `"ligne 1\nligne 2"` | `\n` : retour à la ligne |
| `"colonne\tcolonne"` | `\t` : tabulation |
| `"C:\\Users"` | `\\` : une barre oblique inversée |
| `"Il dit \"oui\""` | `\"` : un guillemet dans un texte délimité par des guillemets |

Le `\` introduit une **séquence d'échappement** : un caractère difficile à écrire directement.

**Opérations de base** :
```python
"Le Petit " + "Prince"  # "Le Petit Prince" : concaténation
"-" * 20  # "--------------------" : répétition
len("Le Petit Prince")  # 15 : nombre de caractères
"Petit" in "Le Petit Prince"  # True : le texte en contient-il un autre ?
```

---

### 2. Indexation et slicing

Chaque caractère a une **position**, appelée **indice**, qui commence à **0** :

```
 caractère :  9   7   8   2   0   7   0   6   1   2   7   5   8
 indice    :  0   1   2   3   4   5   6   7   8   9  10  11  12
 depuis la fin : -13 …                                 -3  -2  -1
```

```python
isbn = "9782070612758"
isbn[0]  # "9" : le premier caractère
isbn[12]  # "8" : le dernier (len - 1)
isbn[-1]  # "8" : le dernier, compté depuis la fin
isbn[13]  # IndexError: string index out of range
```

Le **slicing** extrait un morceau : `texte[début:fin]`, **fin exclue**, comme pour `range`.

| Expression | Résultat | Signification |
|---|---|---|
| `isbn[0:3]` ou `isbn[:3]` | `"978"` | Les 3 premiers caractères |
| `isbn[3:]` | `"2070612758"` | À partir de l'indice 3 |
| `isbn[:-1]` | `"978207061275"` | Tout sauf le dernier : les 12 chiffres « utiles » d'un ISBN |
| `isbn[-1:]` | `"8"` | Le dernier caractère, sous forme de texte |
| `isbn[::2]` | un caractère sur deux | Un troisième nombre : le **pas** |
| `isbn[::-1]` | `"8572160702879"` | Le texte à l'envers |

Contrairement à l'indexation, le slicing ne provoque **jamais** d'erreur : `isbn[5:100]` s'arrête simplement à la fin du texte.

> Démo : [`demos/01_indexation_slicing.py`](demos/01_indexation_slicing.md)

---

### 3. Un texte est immuable

On ne peut **pas** modifier un texte existant :
```python
title = "le Petit Prince"
title[0] = "L"  # TypeError: 'str' object does not support item assignment
```

Toutes les méthodes qui « transforment » un texte en **renvoient un nouveau** ; l'original n'est jamais modifié :
```python
title.capitalize()  # renvoie "Le petit prince"… et le résultat est perdu
print(title)  # le Petit Prince : inchangé !

title = title.capitalize()  # ✅ on réaffecte le résultat
```

> ⚠️ **Piège n° 1 des chaînes** : appeler une méthode sans récupérer son résultat. `answer.strip()` seul sur une ligne ne fait **rien** d'utile.

---

### 4. Les méthodes essentielles

On appelle une **méthode** avec un point : `texte.methode(arguments)`.

**Nettoyer et transformer**

| Méthode | Résultat pour `"  Le Petit Prince  "` |
|---|---|
| `.strip()` | `"Le Petit Prince"` : espaces retirés au début et à la fin |
| `.lower()` / `.upper()` | `"  le petit prince  "` / `"  LE PETIT PRINCE  "` |
| `.title()` | `"  Le Petit Prince  "` : une majuscule à chaque mot |
| `.capitalize()` | `"  le petit prince  "` : majuscule au premier caractère, ici un espace ! |
| `.replace("Petit", "Grand")` | `"  Le Grand Prince  "` |

**Rechercher**

| Méthode | Exemple | Résultat |
|---|---|---|
| `.find(sous_texte)` | `"Le Petit Prince".find("Petit")` | `3` : l'indice, ou `-1` si absent |
| `.count(sous_texte)` | `"abracadabra".count("a")` | `5` |
| `.startswith(debut)` | `"LIRE10".startswith("LIRE")` | `True` |
| `.endswith(fin)` | `"photo.png".endswith(".png")` | `True` |

**Tester le contenu**

| Méthode | Vrai si… | Exemples |
|---|---|---|
| `.isdecimal()` | le texte n'est fait **que** de chiffres décimaux, et n'est pas vide | `"123"` ✅, `"12a"` ❌, `""` ❌ |
| `.isalpha()` | uniquement des lettres | `"Zoé"` ✅, `"Zoé 2"` ❌ |
| `.isupper()` / `.islower()` | tout en majuscules / minuscules | |

**Enchaîner les méthodes** : chacune renvoie un texte, sur lequel on peut appeler la suivante.
```python
choice = input("Votre choix : ").strip().lower()  # " Q " devient "q"
```
C'est **le** réflexe pour toute saisie : on la nettoie dès la lecture.

**Comparer sans tenir compte de la casse** : on compare les versions en minuscules, `a.lower() == b.lower()`. Pour un texte international, `.casefold()` est plus complet : `"Straße".casefold()` donne `"strasse"`.

> Démo : [`demos/02_methodes.py`](demos/02_methodes.md)

---

### 5. Mettre en forme avec les f-strings

Après le `:` d'une f-string, un **mini-langage** décrit la mise en forme : `{valeur:[alignement][largeur][,][.précision][type]}`.

| Format | Exemple | Résultat | Signification |
|---|---|---|---|
| `:<15` | `f"{'Titre':<15}"` | `"Titre          "` | Aligné à gauche, sur 15 caractères |
| `:>8` | `f"{'7.50':>8}"` | `"    7.50"` | Aligné à droite |
| `:^9` | `f"{'mid':^9}"` | `"   mid   "` | Centré |
| `:.2f` | `f"{7.5:.2f}"` | `"7.50"` | 2 décimales (module 01) |
| `:>8.2f` | `f"{7.5:>8.2f}"` | `"    7.50"` | Combiné : à droite, 8 caractères, 2 décimales |
| `:,.2f` | `f"{1234567.891:,.2f}"` | `"1,234,567.89"` | Séparateur de milliers |
| `:05d` | `f"{42:05d}"` | `"00042"` | Entier sur 5 chiffres, complété de zéros |
| `!r` | `f"{'abc'!r}"` | `"'abc'"` | Représentation, avec guillemets (module 01) |

La largeur peut elle-même venir d'une variable : `f"{label:<{width}}"`.

C'est ainsi qu'on aligne un ticket de caisse :
```python
print(f"{'Le Petit Prince':<20}{2:>4}{15.00:>10.2f} €")
print(f"{'Marque-page':<20}{1:>4}{2.50:>10.2f} €")
```
```
Le Petit Prince        2     15.00 €
Marque-page            1      2.50 €
```

> Démo : [`demos/03_formatage.py`](demos/03_formatage.md)

---

### 6. Parcourir un texte

Un texte se parcourt avec `for`, caractère par caractère (module 04). Avec un **indice**, quand la position compte :
```python
for index in range(len(isbn)):
    digit = int(isbn[index])
    ...
```
Et on **construit** un nouveau texte en partant d'un texte vide et en concaténant :
```python
digits_only = ""
for character in "978-2-07-061275-8":
    if character.isdecimal():
        digits_only += character  # "9782070612758"
```

> Démo : [`demos/04_parcours.py`](demos/04_parcours.md)

---

## 🔎 Approfondissement

### `isdigit` ou `isdecimal` ?
`"²".isdigit()` vaut `True` : l'exposant 2 est considéré comme un chiffre… mais `int("²")` échoue. Pour valider qu'une saisie est un nombre entier, `isdecimal()` est le bon test.

### `split` et `join`
`"a,b,c".split(",")` découpe un texte en une **liste** de morceaux, et `", ".join(...)` fait l'inverse. Ces deux méthodes, indispensables, sont présentées au module 06 avec les listes.

### Unicode, `ord` et `chr`
Un `str` Python est une suite de caractères **Unicode** : toutes les écritures du monde, les symboles, les emojis. Chaque caractère a un numéro : `ord("A")` vaut `65`, `chr(233)` vaut `"é"`. Pour stocker ou transmettre un texte, on le convertit en **octets** (`bytes`) avec un encodage : `"é".encode("utf-8")` donne `b'\xc3\xa9'` (2 octets), et `.decode("utf-8")` fait l'inverse. C'est la clé des problèmes d'accents vus au module 00 (et au module 11, avec les fichiers).

### Les anciens formatages
Vous croiserez dans du code existant `"%s a %d ans" % ("Ada", 36)` (le plus ancien) et `"{} a {} ans".format("Ada", 36)`. Ils fonctionnent toujours, mais les f-strings sont plus lisibles : utilisez-les pour tout nouveau code.

### Les t-strings (Python 3.14)
Python 3.14 introduit les **template strings** (PEP 750) : `t"Bonjour {name}"`. Contrairement à une f-string, une t-string ne produit **pas** un texte, mais un objet `Template` qui conserve séparément les parties fixes (`.strings`) et les valeurs insérées (`.values`). Une bibliothèque peut ainsi traiter les valeurs **avant** de construire le texte final : échapper du HTML pour éviter une injection, ou préparer une requête SQL sûre. C'est un outil pour les auteurs de bibliothèques ; vous l'utiliserez à travers elles, notamment avec les frameworks web.

### Les chaînes brutes
`r"C:\Users\nouveau"` : avec le préfixe `r` (*raw*), les `\` ne sont pas interprétés. C'est utile pour les chemins Windows et les expressions régulières (approfondissement A7).

---

## Démos du module

| # | Démo | Notion |
|---|---|---|
| 01 | [indexation_slicing](demos/01_indexation_slicing.md) | Indices, indices négatifs, slicing |
| 02 | [methodes](demos/02_methodes.md) | Nettoyer, rechercher, tester ; immuabilité |
| 03 | [formatage](demos/03_formatage.md) | Largeur, alignement, décimales, milliers |
| 04 | [parcours](demos/04_parcours.md) | Parcourir, filtrer, construire un texte |

## Exercices d'entraînement (facultatifs)

| # | Exercice | Difficulté |
|---|---|---|
| 01 | [Initiales et nom d'auteur](exercices/exo01_initiales/enonce.md) | ★ |
| 02 | [Valider un code promo](exercices/exo02_code_promo/enonce.md) | ★★ |
| 03 | [Les méthodes qui ne font rien](exercices/exo03_immuabilite/enonce.md) (piège) | ★★ |

## Fil rouge

➡️ **[Étape 05 de PyBooks : ISBN et ticket de caisse](../fil-rouge/etape-05/enonce.md)**

## À retenir

- Indices à partir de **0** ; `texte[-1]` est le dernier caractère ; `texte[début:fin]` exclut la fin.
- Un texte est **immuable** : les méthodes renvoient un **nouveau** texte, qu'il faut récupérer.
- Toute saisie se nettoie : `input(...).strip().lower()`.
- `in`, `.find()`, `.startswith()` pour chercher ; `.isdecimal()` pour valider des chiffres.
- f-strings : `:<15` (gauche), `:>8` (droite), `:^9` (centré), `:.2f`, `:,` (milliers).
