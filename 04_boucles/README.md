# Module 04 : boucles et débogueur

> **Objectifs du module**
> - Répéter des instructions tant qu'une condition est vraie, avec `while`.
> - Parcourir une suite de nombres ou de caractères avec `for` et `range`.
> - Contrôler une boucle avec `break` et `continue`.
> - Accumuler des résultats : sommes, compteurs, maximums.
> - **Observer un programme en cours d'exécution avec le débogueur** : points d'arrêt, pas à pas, inspection des variables.
>
> **Durée indicative** : 3 h 30
> **Prérequis** : module 03
> **Étape PyBooks** : [04, le menu de la boutique](../fil-rouge/etape-04/)

---

## L'essentiel

### 1. `while` : répéter tant que…

```python
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Partez !")
```
```
3
2
1
Partez !
```

Le principe :
1. Python évalue la condition ;
2. si elle est vraie, il exécute le bloc, puis **revient** à l'étape 1 ;
3. si elle est fausse, il passe à la suite du programme.

Le bloc doit faire **évoluer** quelque chose dont dépend la condition (ici, `countdown -= 1`). Sinon la condition reste vraie pour toujours : c'est une **boucle infinie**.

> ⚠️ **Piège : la boucle infinie.** Le programme ne se termine jamais et semble « figé ». Pour l'arrêter : **`Ctrl+C`** dans le terminal (`KeyboardInterrupt`).

**L'usage typique : redemander une saisie tant qu'elle n'est pas valide.**
```python
quantity = int(input("Quantité (1 à 10) : "))
while quantity < 1 or quantity > 10:
    print("Quantité invalide.")
    quantity = int(input("Quantité (1 à 10) : "))
```

> Démo : [`demos/01_while.py`](demos/01_while.md)

---

### 2. `for` et `range` : répéter un nombre connu de fois

```python
for number in range(5):
    print(number)  # 0, 1, 2, 3, 4
```

`for` donne successivement à la variable `number` chaque valeur produite par `range(5)`, et exécute le bloc pour chacune.

| Appel | Valeurs produites | Remarque |
|---|---|---|
| `range(5)` | 0, 1, 2, 3, 4 | De 0 à 5 **exclu** : 5 valeurs |
| `range(1, 6)` | 1, 2, 3, 4, 5 | De 1 à 6 exclu |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 | Avec un **pas** de 2 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 | Pas négatif : compte à rebours |

> ⚠️ **Piège : la borne de fin est exclue.** `range(1, 10)` s'arrête à **9**. Pour aller de 1 à `n` inclus : `range(1, n + 1)`. Cette « erreur d'une unité » (*off-by-one*) est l'une des plus fréquentes de toute la programmation.

**Parcourir un texte** : `for` fonctionne avec tout ce qui se parcourt, et notamment les chaînes de caractères, lettre par lettre :
```python
for letter in "ISBN":
    print(letter)  # I, S, B, N
```

**`for` ou `while` ?**
- `for` quand on connaît à l'avance **ce qu'on parcourt** : un nombre de répétitions, les caractères d'un texte, et bientôt les éléments d'une liste.
- `while` quand on répète **jusqu'à ce qu'une situation change** : une saisie valide, le choix « quitter » d'un menu.

> Démo : [`demos/02_for_range.py`](demos/02_for_range.md)

---

### 3. Accumuler : sommes, compteurs, maximums

La plupart des boucles **calculent quelque chose au fil des tours**. Le schéma est toujours le même : une variable **initialisée avant** la boucle, et **mise à jour dans** la boucle.

```python
total_pages = 0  # 1. initialiser AVANT la boucle
for day in range(1, 8):
    pages = int(input(f"Pages lues le jour {day} : "))
    total_pages += pages  # 2. accumuler DANS la boucle
print(f"Total de la semaine : {total_pages} pages")  # 3. utiliser APRÈS
```

| Accumulateur | Initialisation | Mise à jour |
|---|---|---|
| Somme | `total = 0` | `total += value` |
| Compteur | `count = 0` | `count += 1` (souvent dans un `if`) |
| Maximum | `best = None` | `if best is None or value > best: best = value` |

> ⚠️ **Piège** : initialiser l'accumulateur **dans** la boucle. Il est alors remis à zéro à chaque tour, et seule la dernière valeur compte.

---

### 4. `break` et `continue`

| Instruction | Effet |
|---|---|
| `break` | **Sort** immédiatement de la boucle |
| `continue` | Passe **directement au tour suivant**, sans exécuter la fin du bloc |

**Le menu « tant que l'utilisateur ne quitte pas »** est le cas d'usage roi de `break` :
```python
while True:  # boucle a priori infinie…
    choice = input("Choix (1, 2 ou Q) : ")
    if choice == "Q":
        break  # … dont on sort explicitement
    print(f"Vous avez choisi {choice}")
print("Au revoir")
```

`continue` permet d'ignorer certains cas sans imbriquer de `if` :
```python
for letter in "Le Petit Prince":
    if letter == " ":
        continue  # on ignore les espaces
    print(letter, end="")  # LePetitPrince
```

> 💡 `while True` avec un `break` est parfaitement idiomatique en Python, à condition que la sortie soit **évidente** à la lecture.

> Démo : [`demos/03_break_continue.py`](demos/03_break_continue.md)

---

### 5. Les boucles imbriquées

Une boucle peut en contenir une autre : la boucle intérieure s'exécute **entièrement** à chaque tour de la boucle extérieure.

```python
for row in range(1, 4):
    for column in range(1, 4):
        print(row * column, end="\t")  # \t : tabulation
    print()  # retour à la ligne après chaque rangée
```
```
1	2	3
2	4	6
3	6	9
```

`break` ne fait sortir **que** de la boucle la plus intérieure.

---

### 6. Le débogueur : voir le programme s'exécuter

Avec des boucles, on ne peut plus deviner l'état d'un programme en lisant le code ligne à ligne : la même ligne s'exécute des dizaines de fois, avec des valeurs différentes. Ajouter des `print` partout est le réflexe du débutant, mais il faut deviner à l'avance quoi afficher, relancer à chaque nouvelle hypothèse, puis tout retirer.

Un **débogueur** suspend le programme à l'endroit choisi, et permet d'**examiner** librement son état, puis d'avancer **pas à pas**.

#### Dans PyCharm

1. **Poser un point d'arrêt** : cliquez dans la marge, sur le numéro de la ligne (ou `Ctrl+F8`, curseur sur la ligne). Un **point rouge** apparaît. Un second clic le retire.
2. **Lancer en mode débogage** : clic droit dans l'éditeur → **Debug '…'**, suivi du nom du fichier (ou l'icône en forme d'insecte, à côté de ▶, en haut de la fenêtre). La fenêtre **Debug** s'ouvre en bas. Les questions du programme (`input`) s'affichent dans son onglet **Console** : c'est là qu'on tape les réponses.
3. Le programme s'arrête **avant** d'exécuter la ligne marquée, surlignée en bleu. Explorez :
   - le panneau **Variables** (onglet *Threads & Variables*) : la valeur de chaque variable, à cet instant ;
   - les **valeurs affichées en gris** au bout des lignes de l'éditeur, et le **survol** d'une variable ;
   - **Evaluate Expression** (`Alt+F8`) : tapez une expression (`total * 2`, `quantity > stock`), puis *Evaluate* ; elle est calculée dans le contexte suspendu.
4. **Avancer** :

| Action | Raccourci | Effet |
|---|---|---|
| *Resume Program* | `F9` | Continue jusqu'au prochain point d'arrêt (donc au tour de boucle suivant) |
| *Step Over* | `F8` | Exécute la ligne courante, puis s'arrête à la suivante |
| *Step Into* | `F7` | Entre **dans** la fonction appelée à la ligne courante (utile à partir du module 08) |
| *Step Out* | `Shift+F8` | Termine la fonction en cours et s'arrête à la ligne qui l'a appelée |
| *Stop* | `Ctrl+F2` | Termine le programme |

5. **Point d'arrêt conditionnel** : clic droit sur le point rouge → champ **Condition**, par exemple `day == 5` → *Done*. Le programme ne s'arrête que lorsque la condition est vraie : indispensable dans une boucle de 1 000 tours.

> ⚠️ Le bouton ▶ (*Run*) **ignore** les points d'arrêt : pour déboguer, il faut lancer avec *Debug*.

> 💡 Chaque lancement crée une **configuration d'exécution**, dont le nom apparaît en haut de la fenêtre, à côté de ▶. *Run → Edit Configurations…* permet de la modifier ; c'est là, dans le champ *Script parameters*, qu'on donnera des arguments au programme au module 12.

> 💡 La démarche d'un bon débogage : **formuler une hypothèse** (« je pense que `total` est faux au 3e tour »), puis poser le point d'arrêt qui la confirme ou l'infirme. On ne pose pas des points d'arrêt au hasard.

> 🔎 **VS Code, si vous l'utilisez**
> Le débogueur est fourni par l'extension *Python* (installée au module 00). Créez d'abord, dans le dossier `formation-python`, le fichier `.vscode/launch.json`, qui décrit comment lancer un programme en mode débogage :
> ```json
> {
>   "version": "0.2.0",
>   "configurations": [
>     {
>       "name": "Python : fichier courant",
>       "type": "debugpy",
>       "request": "launch",
>       "program": "${file}",
>       "console": "integratedTerminal",
>       "cwd": "${workspaceFolder}",
>       "env": { "PYTHONUTF8": "1" }
>     },
>     {
>       "name": "Python : fichier courant avec arguments",
>       "type": "debugpy",
>       "request": "launch",
>       "program": "${file}",
>       "args": "${command:pickArgs}",
>       "console": "integratedTerminal",
>       "cwd": "${workspaceFolder}",
>       "env": { "PYTHONUTF8": "1" }
>     }
>   ]
> }
> ```
> - `"program": "${file}"` : le fichier ouvert dans l'éditeur ;
> - `"cwd": "${workspaceFolder}"` : le programme est lancé depuis le dossier du projet, comme avec `uv run` ;
> - `"console": "integratedTerminal"` : les saisies se font dans le **terminal**, pas dans la console de débogage ;
> - la seconde configuration demande les arguments à passer au programme (module 12).
>
> Ensuite : `F9` pose un point d'arrêt, `F5` lance (choisissez **« Python : fichier courant »**) puis continue, `F10` passe à la ligne suivante, `F11` entre dans une fonction, `Shift+F11` en sort, `Shift+F5` arrête. Le panneau **Variables** est à gauche ; la **console de débogage** évalue une expression. Point conditionnel : clic droit sur le point rouge → *Edit Breakpoint…* → *Expression*.

#### Dans le terminal : `breakpoint()`

Sans éditeur (sur un serveur, par exemple), on peut écrire `breakpoint()` à l'endroit voulu du code : le programme s'y arrête et ouvre **pdb**, le débogueur en ligne de commande (invite `(Pdb)`). Les commandes de base :

| Commande | Effet |
|---|---|
| `p total` | Affiche la valeur de `total` |
| `n` | Ligne suivante |
| `c` | Continue jusqu'au prochain arrêt |
| `q` | Quitte (arrête le programme) |

> ⚠️ Un `breakpoint()` oublié **bloque** le programme en attente d'une commande. Il ne doit jamais rester dans du code rendu ([CONVENTIONS.md](../CONVENTIONS.md), section 8).

> Démo : [`demos/04_debogueur.py`](demos/04_debogueur.md)

---

## 🔎 Approfondissement

### Le `else` des boucles
Une boucle peut avoir un bloc `else`, exécuté seulement si la boucle s'est terminée **sans `break`** :
```python
for attempt in range(3):
    code = input("Code promo : ")
    if code == "LIRE10":
        print("Code accepté")
        break
else:
    print("Trop de tentatives")
```
C'est l'outil idéal pour « chercher, et réagir si l'on n'a rien trouvé ». Sa lisibilité est discutée : beaucoup d'équipes préfèrent une variable booléenne `found`.

### L'opérateur morse `:=`
L'**expression d'affectation** affecte une variable **à l'intérieur** d'une condition :
```python
while (answer := input("Commande (vide pour finir) : ")) != "":
    print(f"Commande : {answer}")
```
Elle évite de répéter l'`input` avant et dans la boucle. À utiliser avec modération : la lisibilité prime.

### pdb en détail
| Commande | Effet |
|---|---|
| `s` | Entre **dans** la fonction appelée à la ligne courante (utile au module 08) |
| `l` / `ll` | Affiche le code autour de la ligne courante / toute la fonction |
| `b 12` | Pose un point d'arrêt à la ligne 12 ; `b 12, day == 5` : point conditionnel |
| `display total` | Réaffiche `total` à chaque arrêt, si sa valeur a changé |
| `interact` | Ouvre un REPL complet avec les variables du moment |

- `uv run python -m pdb script.py` lance un script sous pdb dès sa première ligne.
- La variable d'environnement `PYTHONBREAKPOINT=0` désactive tous les `breakpoint()` sans toucher au code.
- Depuis Python 3.14, `q` demande une confirmation, car quitter pdb arrête le programme.

---

## Démos du module

| # | Démo | Notion |
|---|---|---|
| 01 | [while](demos/01_while.md) | `while`, saisie validée, boucle infinie |
| 02 | [for_range](demos/02_for_range.md) | `for`, `range`, parcours d'un texte, accumulateurs |
| 03 | [break_continue](demos/03_break_continue.md) | `break`, `continue`, menu `while True` |
| 04 | [debogueur](demos/04_debogueur.md) | Points d'arrêt, pas à pas, variables, point conditionnel |

## Exercices d'entraînement (facultatifs)

| # | Exercice | Difficulté |
|---|---|---|
| 01 | [Statistiques de lecture](exercices/exo01_statistiques_lecture/enonce.md) | ★ |
| 02 | [Le juste prix](exercices/exo02_juste_prix/enonce.md) | ★★ |
| 03 | [Le compteur qui ne compte pas](exercices/exo03_bug_boucle/enonce.md) (piège, au débogueur) | ★★ |

## Fil rouge

➡️ **[Étape 04 de PyBooks : le menu de la boutique](../fil-rouge/etape-04/enonce.md)**

## À retenir

- `while condition:` répète tant que la condition est vraie ; le bloc doit la faire évoluer. `Ctrl+C` arrête une boucle infinie.
- `for x in range(debut, fin, pas):` ; la **fin est exclue**.
- `for letter in texte:` parcourt les caractères.
- Accumulateur : initialisé **avant** la boucle, mis à jour **dedans**, utilisé **après**.
- `break` sort de la boucle ; `continue` passe au tour suivant ; `while True` + `break` pour un menu.
- Débogueur (PyCharm) : point d'arrêt dans la marge, *Debug*, `F8` ligne suivante, `F7` entrer dans une fonction, `F9` continuer, panneau Variables, `Alt+F8` pour évaluer, point d'arrêt conditionnel.
