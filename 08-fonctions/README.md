# Module 08 : fonctions

> **Objectifs du module**
> - Découper un programme en **fonctions** nommées, qui reçoivent des paramètres et renvoient un résultat.
> - Annoter les paramètres et le retour avec des **types**, et documenter chaque fonction par une **docstring**.
> - Séparer le **calcul** (fonctions pures, testables) de l'**affichage** et des saisies.
> - Structurer un script autour d'une fonction `main()`.
> - Écrire ses **premiers tests automatisés** avec pytest.
>
> **Durée indicative** : 4 h 30
> **Prérequis** : module 07
> **Étape PyBooks** : [08, le grand découpage](../fil-rouge/etape-08/)

---

## L'essentiel

### 1. Pourquoi des fonctions ?

À l'étape 07, PyBooks dépassait 250 lignes, et le calcul de la clé d'un ISBN, celui du ticket ou celui des frais de port étaient noyés dans le menu. Une **fonction** donne un **nom** à un morceau de code, pour :
- **le lire** : `if is_valid_isbn(candidate):` se comprend sans lire le calcul ;
- **le réutiliser** : on l'appelle autant de fois qu'on veut, au lieu de copier-coller ;
- **le tester** : on peut vérifier automatiquement qu'il donne le bon résultat ;
- **le modifier en un seul endroit**.

### 2. Définir et appeler une fonction

```python
def price_with_vat(price, vat_rate):
    """Renvoie le prix toutes taxes comprises."""
    return price * (1 + vat_rate)


total = price_with_vat(Decimal("7.50"), Decimal("0.06"))  # appel
```

- `def` définit la fonction, `price` et `vat_rate` sont ses **paramètres** ;
- à l'**appel**, les valeurs transmises (`Decimal("7.50")`…) sont les **arguments** : chaque paramètre reçoit l'argument correspondant ;
- `return` **renvoie** une valeur à l'appelant, et **termine** la fonction ;
- une fonction sans `return` (ou avec un `return` seul) renvoie **`None`**.

Les arguments peuvent être passés **par position** ou **par nom** :
```python
price_with_vat(Decimal("7.50"), Decimal("0.06"))
price_with_vat(price=Decimal("7.50"), vat_rate=Decimal("0.06"))  # plus lisible
```

**Renvoyer plusieurs valeurs** : on renvoie un tuple, que l'appelant déballe.
```python
def split_price(total):
    euros = int(total)
    cents = int((total - euros) * 100)
    return euros, cents


euros, cents = split_price(Decimal("12.90"))
```

**Les variables d'une fonction sont locales** : créées à chaque appel, elles disparaissent à la fin, et n'existent pas en dehors (détails au module 09).

> Démo : [`demos/01_definir_appeler.py`](demos/01_definir_appeler.md)

---

### 3. Annoter les types

À partir de ce module, **chaque fonction est annotée** : on indique le type de chaque paramètre et du résultat.

```python
from decimal import Decimal


def price_with_vat(price: Decimal, vat_rate: Decimal) -> Decimal:
    return price * (1 + vat_rate)
```

| Annotation | Signification |
|---|---|
| `int`, `float`, `str`, `bool`, `Decimal` | Un type simple |
| `list[str]` | Une liste de textes |
| `dict[str, int]` | Un dictionnaire de textes vers des entiers |
| `tuple[int, int]` | Un tuple de deux entiers |
| `set[str]` | Un ensemble de textes |
| `str \| None` | Un texte, **ou** `None` |
| `-> None` | La fonction ne renvoie rien |

Les annotations **ne changent rien à l'exécution** : Python ne les vérifie pas. Elles servent :
- au **lecteur**, qui sait immédiatement ce que la fonction attend ;
- à l'**éditeur**, qui complète mieux et souligne les erreurs ;
- aux **outils de vérification** comme mypy (module 13), qui détectent les incohérences avant l'exécution.

### 4. Documenter : la docstring

La première ligne d'une fonction peut être un texte entre triples guillemets, sa **docstring**. `help(fonction)` l'affiche, et l'éditeur la montre au survol.

```python
def shipping_cost(paper_amount_incl_vat: Decimal) -> Decimal:
    """Calcule les frais de port d'une commande.

    Les frais sont offerts dès que le montant TTC des livres papier atteint
    le seuil de livraison gratuite.

    Args:
        paper_amount_incl_vat: Montant TTC des livres papier de la commande.

    Returns:
        Les frais de port, éventuellement nuls.
    """
```

Le cours suit le **style Google** : une phrase de résumé, puis, si utile, une explication et les sections `Args:`, `Returns:` et `Raises:` (module 10). Une docstring dit **ce que fait** la fonction et **pourquoi**, pas comment elle le fait ligne par ligne.

> Démo : [`demos/02_annotations_docstrings.py`](demos/02_annotations_docstrings.md)

---

### 5. Les valeurs par défaut, et leur piège

Un paramètre peut avoir une **valeur par défaut**, utilisée si l'argument n'est pas fourni :
```python
def format_price(amount: Decimal, currency: str = "€") -> str:
    return f"{amount:.2f} {currency}"


format_price(Decimal("7.5"))  # '7.50 €'
format_price(Decimal("7.5"), "$")  # '7.50 $'
```

> ⚠️ **Piège majeur : une valeur par défaut mutable.**
> ```python
> def add_title(title: str, titles: list[str] = []) -> list[str]:   # ❌
>     titles.append(title)
>     return titles
>
> add_title("Dune")      # ['Dune']
> add_title("Ulysse")    # ['Dune', 'Ulysse'] !!!
> ```
> La valeur par défaut est créée **une seule fois**, quand Python lit le `def`, et non à chaque appel. Tous les appels partagent donc **la même** liste. La forme correcte :
> ```python
> def add_title(title: str, titles: list[str] | None = None) -> list[str]:   # ✅
>     if titles is None:
>         titles = []
>     titles.append(title)
>     return titles
> ```

> Démo : [`demos/03_valeur_defaut.py`](demos/03_valeur_defaut.md)

---

### 6. Fonctions pures et effets de bord

Une fonction **pure** calcule un résultat **uniquement** à partir de ses paramètres, et ne fait **rien d'autre** : pas d'affichage, pas de saisie, pas de modification de variables extérieures. Le même appel donne toujours le même résultat.

| Fonction pure | Fonction à effet de bord |
|---|---|
| `price_with_vat(price, rate)` | `print_ticket(cart)` : affiche |
| `is_valid_isbn(isbn)` | `ask_quantity()` : lit une saisie |
| `format_ticket(cart) -> str` | `add_to_cart(cart, …)` : modifie le panier reçu |

**La règle de conception** : on garde le maximum de logique dans des fonctions pures, et l'on concentre les saisies et les affichages dans quelques fonctions « d'interface ». Le calcul devient alors **testable**, et réutilisable ailleurs : une API web, plus tard, appellera exactement les mêmes fonctions de calcul.

> 💡 Une fonction qui **renvoie** un texte est plus réutilisable qu'une fonction qui l'**affiche** : `print(format_ticket(cart))` affiche, mais le même texte peut aussi être écrit dans un fichier ou envoyé par e-mail.

### 7. La structure d'un script : `main()`

À partir de maintenant, tout script suit la structure professionnelle décrite dans [CONVENTIONS.md](../CONVENTIONS.md) :

```python
"""Rôle du fichier."""

from decimal import Decimal  # 1. imports

VAT_RATE = Decimal("0.06")  # 2. constantes


def price_with_vat(price: Decimal) -> Decimal:  # 3. fonctions
    """Renvoie le prix TTC."""
    return price * (1 + VAT_RATE)


def main() -> None:  # 4. le programme principal
    """Point d'entrée du script."""
    print(price_with_vat(Decimal("7.50")))


if __name__ == "__main__":  # 5. on lance main() si le fichier est exécuté
    main()
```

La dernière ligne signifie : « lance `main()` seulement si ce fichier est **exécuté** directement ». S'il est **importé** par un autre fichier, par exemple par un fichier de tests, ses fonctions deviennent disponibles **sans** que le programme ne démarre. Le mécanisme (`__name__`) est expliqué au module 12.

> Démo : [`demos/04_pur_et_main.py`](demos/04_pur_et_main.md)

---

### 8. Les premiers tests automatisés

Tester « à la main », c'est relancer le programme et vérifier à l'œil. C'est lent, et on finit par ne plus le faire. Un **test automatisé** est une petite fonction qui appelle notre code et **vérifie** le résultat.

Le cours utilise **pytest**, l'outil de référence.

> 🧰 **Mise en place : installer pytest.** pytest ne fait pas partie de Python : c'est une **bibliothèque** à ajouter au projet. Dans le dossier `formation-python` :
> ```bash
> uv add --dev pytest
> ```
> ```
> Resolved 7 packages in 188ms
> Installed 6 packages in 442ms
>  + pytest==9.1.1
>  …
> ```
> uv télécharge pytest (et les quelques bibliothèques dont il a besoin), l'installe dans le `.venv` du projet, et **modifie votre `pyproject.toml`** :
> ```toml
> [project]
> name = "formation-python"
> version = "0.1.0"
> requires-python = ">=3.14"
> dependencies = []
>
> [dependency-groups]
> dev = [
>     "pytest>=9.1.1",
> ]
> ```
> - `[dependency-groups]` regroupe les outils **du développeur** : `--dev` les range dans le groupe `dev`. Ils servent à écrire le programme, pas à le faire fonctionner, c'est pourquoi `dependencies` reste vide.
> - `"pytest>=9.1.1"` : la version installée devient la **version minimale** acceptée. Vos numéros peuvent être plus récents.
> - `uv.lock` est mis à jour avec la version exacte de chaque bibliothèque installée.
>
> Relancez `uv run python outils/verifier_poste.py` : la ligne pytest passe à `[OK]`.

**`discount.py`** (le code testé) :
```python
def discounted_price(price: Decimal, rate: Decimal) -> Decimal:
    """Applique une remise et arrondit au centime."""
    return (price * (1 - rate)).quantize(CENT, rounding=ROUND_HALF_UP)
```

**`test_discount.py`** (les tests, dans le même dossier) :
```python
from decimal import Decimal

from discount import discounted_price


def test_ten_percent_discount() -> None:
    assert discounted_price(Decimal("20.00"), Decimal("0.10")) == Decimal("18.00")


def test_result_is_rounded_to_the_cent() -> None:
    assert discounted_price(Decimal("7.45"), Decimal("0.10")) == Decimal("6.71")
```

- Le fichier de tests s'appelle `test_<sujet>.py`, et chaque test est une fonction `test_<comportement>()`.
- `from discount import discounted_price` **importe** la fonction depuis le fichier voisin `discount.py` (module 12).
- `assert condition` vérifie que la condition est vraie. Sinon, le test **échoue**.

On lance les tests d'un dossier :
```bash
uv run pytest 08-fonctions/demos/05_tests
```
```
..                                                                   [100%]
2 passed in 0.02s
```
Dans PyCharm, on peut aussi faire un clic droit sur le dossier → *Run 'pytest in 05_tests'* : les résultats s'affichent dans une fenêtre dédiée, test par test.

Quand un test échoue, pytest montre précisément la valeur obtenue et la valeur attendue :
```
>       assert discounted_price(Decimal("7.45"), Decimal("0.10")) == Decimal("6.70")
E       AssertionError: assert Decimal('6.71') == Decimal('6.70')
```

> 💡 Un bon test vérifie **un** comportement, et son nom le décrit. On teste en priorité les **cas limites** : la valeur exactement au seuil, la liste vide, le zéro… C'est là que se cachent les bugs (souvenez-vous des exercices pièges des modules 03 et 04).

> Démo : [`demos/05_tests/`](demos/05_tests/05_tests.md)

---

## 🔎 Approfondissement

### Les clauses de garde
Plutôt que d'imbriquer des `if`, on traite d'abord les cas particuliers, en sortant tôt de la fonction :
```python
def shipping_cost(paper_amount: Decimal) -> Decimal:
    if paper_amount == 0:
        return Decimal(0)  # pas de livre papier
    if paper_amount >= FREE_SHIPPING_THRESHOLD:
        return Decimal(0)  # port offert
    return SHIPPING_FEE
```

### La récursivité
Une fonction peut s'appeler elle-même. C'est élégant pour certains problèmes (parcourir une arborescence de dossiers), mais Python limite la profondeur d'appel (environ 1000 niveaux par défaut) : pour une simple répétition, une boucle est préférable.

### Les fonctions sont des valeurs
Une fonction est un objet comme un autre : on peut la ranger dans une variable, la passer en argument (c'est ce que fait `sorted(…, key=str.lower)`), ou la renvoyer. C'est l'objet du module 09 et de l'approfondissement A4.

### Les doctests
Les exemples écrits dans une docstring au format du REPL (`>>> appel` puis le résultat attendu) peuvent être exécutés par le module `doctest`, ou par `pytest --doctest-modules`. La documentation devient alors un test, qui ne peut plus mentir.

---

## Démos du module

| # | Démo | Notion |
|---|---|---|
| 01 | [definir_appeler](demos/01_definir_appeler.md) | `def`, paramètres, `return`, `None`, plusieurs valeurs |
| 02 | [annotations_docstrings](demos/02_annotations_docstrings.md) | Annotations de type, docstrings, `help` |
| 03 | [valeur_defaut](demos/03_valeur_defaut.md) | Valeurs par défaut, piège du mutable |
| 04 | [pur_et_main](demos/04_pur_et_main.md) | Calcul pur, affichage, `main()` |
| 05 | [tests](demos/05_tests/05_tests.md) | pytest : écrire, lancer, lire un échec |

## Exercices d'entraînement (facultatifs)

| # | Exercice | Difficulté |
|---|---|---|
| 01 | [Une boîte à outils de conversion](exercices/exo01_conversions/enonce.md) | ★ |
| 02 | [L'ISBN-10](exercices/exo02_isbn10/enonce.md) | ★★ |
| 03 | [Les fonctions qui mentent](exercices/exo03_fonctions_piege/enonce.md) (piège) | ★★ |

## Fil rouge

➡️ **[Étape 08 de PyBooks : le grand découpage](../fil-rouge/etape-08/enonce.md)**

## À retenir

- `def nom(param: type) -> type_retour:` ; `return` renvoie une valeur et termine la fonction ; sans `return`, la fonction renvoie `None`.
- Annotations et docstring (style Google) sur **chaque** fonction.
- Jamais de valeur par défaut mutable : `param: list[str] | None = None`.
- Le calcul dans des fonctions **pures** ; les saisies et affichages à part.
- Structure : imports, constantes, fonctions, `main()`, `if __name__ == "__main__": main()`.
- Tests : `test_<sujet>.py`, fonctions `test_<comportement>()`, `assert` ; `uv run pytest dossier`.
