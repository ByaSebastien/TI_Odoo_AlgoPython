# Module 03 : conditions

> **Objectifs du module**
> - Comparer des valeurs et obtenir des booléens.
> - Combiner des conditions avec `and`, `or` et `not`.
> - Faire prendre des décisions à un programme avec `if`, `elif` et `else`.
> - Comprendre l'**indentation**, qui délimite les blocs.
> - Choisir entre plusieurs cas avec `match`.
>
> **Durée indicative** : 3 h
> **Prérequis** : module 02
> **Étape PyBooks** : [03, les règles de la boutique](../fil-rouge/etape-03/)

---

## L'essentiel

### 1. Les comparaisons

Une comparaison produit un **booléen** : `True` ou `False`.

| Opérateur | Signification | Exemple | Résultat |
|---|---|---|---|
| `==` | égal à | `stock == 0` | `False` si `stock` vaut 7 |
| `!=` | différent de | `stock != 0` | `True` |
| `<`, `>` | strictement inférieur, supérieur | `7 < 10` | `True` |
| `<=`, `>=` | inférieur ou égal, supérieur ou égal | `total >= 50` | selon `total` |

```python
quantity = 3
stock = 7
is_available = quantity <= stock  # True : un booléen, qu'on peut stocker
```

> ⚠️ **Piège** : `=` affecte, `==` compare. `if stock = 0:` est une erreur de syntaxe.

**Comparaisons enchaînées** : `1 <= quantity <= 10` signifie « entre 1 et 10 », comme en mathématiques.

**Comparer des textes** : `==` compare caractère par caractère, en tenant compte des majuscules : `"oui" == "Oui"` vaut `False`. `<` et `>` suivent l'ordre des codes des caractères : `"Zoé" < "adam"`, parce que toutes les majuscules passent avant les minuscules. Ce n'est donc **pas** l'ordre du dictionnaire (module 05).

> ⚠️ **Piège** : `"10" < "9"` vaut `True`. Ce sont des **textes**, comparés caractère par caractère : `"1"` vient avant `"9"`. Une saisie doit être convertie **avant** d'être comparée.

**Les nombres à virgule** : à cause de leur imprécision (module 02), `0.1 + 0.2 == 0.3` vaut `False`. Pour les montants, on utilise `Decimal`, qui se compare exactement. Pour les mesures, on utilise `math.isclose(a, b)`.

> Démo : [`demos/01_comparaisons.py`](demos/01_comparaisons.md)

---

### 2. `if`, `elif`, `else`

```python
total = Decimal("62.40")

if total >= FREE_SHIPPING_THRESHOLD:
    shipping = Decimal(0)
    print("Livraison offerte !")
else:
    shipping = SHIPPING_FEE

print(f"Frais de port : {shipping:.2f} €")
```

- `if condition:` exécute le **bloc** qui suit seulement si la condition est vraie.
- `else:` (facultatif) exécute son bloc dans le cas contraire.
- Un **bloc** est l'ensemble des lignes **indentées de 4 espaces** sous la ligne qui se termine par `:`. Le bloc s'arrête à la première ligne qui revient à l'indentation précédente : ici, le dernier `print` s'exécute dans tous les cas.

Pour plus de deux cas, `elif` (contraction de *else if*) enchaîne les conditions :

```python
if quantity <= 0:
    print("Quantité invalide.")
elif quantity > stock:
    print("Stock insuffisant.")
elif quantity >= BULK_QUANTITY:
    print("Commande en gros : un conseiller vous contactera.")
else:
    print("Commande acceptée.")
```

Python teste les conditions **dans l'ordre**, et n'exécute que le **premier** bloc dont la condition est vraie. Les suivantes ne sont même pas évaluées.

> ⚠️ **Piège : l'ordre des `elif`**. Du plus spécifique au plus général. Si l'on teste `total >= 20` avant `total >= 50`, un total de 60 € tombe dans le premier cas, et le second n'est jamais atteint.

Des blocs peuvent être **imbriqués** : un `if` à l'intérieur d'un autre `if`, avec 4 espaces de plus. Au-delà de deux niveaux, le code devient difficile à lire : on cherche alors à combiner les conditions avec `and`, ou à réordonner les tests.

> Démo : [`demos/02_if_elif_else.py`](demos/02_if_elif_else.md)

---

### 3. Combiner des conditions : `and`, `or`, `not`

| Opérateur | Vrai si… | Exemple |
|---|---|---|
| `a and b` | les **deux** sont vraies | `is_member and total >= 30` |
| `a or b` | **au moins une** est vraie | `is_ebook or is_gift_card` |
| `not a` | `a` est fausse | `not is_ebook` |

Priorité : `not`, puis `and`, puis `or`. En cas de doute : des parenthèses.

```python
if not is_ebook and quantity > stock:
    print("Stock insuffisant.")
```

> ⚠️ **Piège classique** :
> ```python
> if answer == "o" or "O":     # ❌ toujours vrai !
> ```
> Python lit `(answer == "o") or ("O")`, et le texte `"O"`, non vide, est considéré comme **vrai**. La bonne écriture : `if answer == "o" or answer == "O":`. Au module 06, on découvrira une forme plus courte : `if answer in ("o", "O"):`.

### 4. Vrai ou faux ? La « truthiness »

Une condition n'est pas forcément un booléen : toute valeur peut être testée. Sont considérés comme **faux** :
- `False` et `None` ;
- le zéro : `0`, `0.0`, `Decimal(0)` ;
- les éléments **vides** : `""`, et bientôt les listes et dictionnaires vides.

**Tout le reste est vrai**, y compris `" "` (un espace), `"0"` et `"False"`, qui sont des textes non vides.

```python
name = input("Votre prénom : ")
if not name:
    print("Vous n'avez rien saisi.")
```

**Tester `None`** : on écrit `if value is None:` (et `is not None`), plutôt que `== None`. La différence entre `is` et `==` est détaillée dans l'approfondissement A2.

> Démo : [`demos/03_logique.py`](demos/03_logique.md)

---

### 5. L'expression conditionnelle

Pour choisir **une valeur** selon une condition, en une ligne :

```python
label = "numérique" if is_ebook else "papier"
```

On la lit : « `"numérique"` si `is_ebook`, sinon `"papier"` ». À réserver aux cas simples : dès qu'il y a plus de deux cas, ou des instructions à exécuter, on revient à `if`.

---

### 6. `match` : choisir parmi plusieurs valeurs

Quand on compare **une même valeur** à plusieurs possibilités, `match` est plus lisible qu'une suite de `elif` :

```python
choice = input("Votre choix : ")

match choice:
    case "1":
        print("Catalogue")
    case "2":
        print("Panier")
    case "q" | "Q":  # | signifie « ou »
        print("Au revoir")
    case _:  # _ attrape tous les autres cas
        print("Choix inconnu")
```

- Le premier `case` qui correspond est exécuté, puis on sort du `match`. Il n'y a pas d'enchaînement vers le cas suivant.
- `case _:` est le cas « par défaut ». Sans lui, une valeur inattendue ne déclenche rien.

`match` sait faire bien plus (déstructurer des listes, des dictionnaires, des objets). Ces possibilités seront présentées au fil des modules 06, 07 et 18.

> Démo : [`demos/04_match.py`](demos/04_match.md)

---

## 🔎 Approfondissement

### `and` et `or` renvoient un opérande
`and` et `or` ne renvoient pas forcément `True` ou `False`, mais **l'une des deux valeurs** :
- `a or b` renvoie `a` si `a` est vrai, sinon `b` ;
- `a and b` renvoie `a` si `a` est faux, sinon `b`.

D'où un idiome courant pour une valeur par défaut :
```python
name = input("Prénom : ") or "lecteur anonyme"
```
Ils sont aussi **paresseux** (« court-circuit ») : si `a` suffit à décider, `b` n'est pas évalué. `stock == 0 or 100 / stock > 5` ne provoque donc jamais de division par zéro.

### Comparer un `Decimal` et un `float`
`Decimal("0.1") == 0.1` vaut `False` : le `float` 0.1 n'est pas exactement 0,1. Encore une raison de ne jamais mélanger les deux.

### `match` : captures et gardes
```python
match quantity:
    case 0:
        print("Rien à commander")
    case n if n > stock:  # capture dans n, avec une garde
        print(f"Seulement {stock} disponibles, pas {n}")
    case _:
        print("OK")
```

### Pourquoi l'indentation ?
De nombreux langages délimitent les blocs par des accolades `{ }` et indentent par convention. Python fait de l'indentation **la** règle : un code mal indenté ne peut pas tromper le lecteur, puisqu'il ne fonctionnerait pas.

---

## Démos du module

| # | Démo | Notion |
|---|---|---|
| 01 | [comparaisons](demos/01_comparaisons.md) | Opérateurs de comparaison, textes, `float` |
| 02 | [if_elif_else](demos/02_if_elif_else.md) | Blocs, `elif`, ordre des conditions |
| 03 | [logique](demos/03_logique.md) | `and`, `or`, `not`, truthiness |
| 04 | [match](demos/04_match.md) | `match` / `case`, `|`, `_` |

## Exercices d'entraînement (facultatifs)

| # | Exercice | Difficulté |
|---|---|---|
| 01 | [Année bissextile](exercices/exo01_bissextile/enonce.md) | ★ |
| 02 | [Tarifs de livraison](exercices/exo02_tarifs_livraison/enonce.md) | ★★ |
| 03 | [Les conditions qui mentent](exercices/exo03_conditions_piege/enonce.md) (piège) | ★★ |

## Fil rouge

➡️ **[Étape 03 de PyBooks : les règles de la boutique](../fil-rouge/etape-03/enonce.md)**

## À retenir

- Une comparaison (`==`, `!=`, `<`, `<=`, `>`, `>=`) donne un booléen. `=` affecte, `==` compare.
- Un bloc est défini par son **indentation** de 4 espaces, après une ligne terminée par `:`.
- `if` / `elif` / `else` : seul le **premier** bloc vrai s'exécute. On ordonne les cas du plus spécifique au plus général.
- `and`, `or`, `not` ; et `x == "a" or x == "b"`, jamais `x == "a" or "b"`.
- Sont faux : `False`, `None`, `0`, `""` et les collections vides. Tout le reste est vrai.
- `match` / `case` pour comparer une valeur à plusieurs possibilités ; `case _:` pour le cas par défaut.
