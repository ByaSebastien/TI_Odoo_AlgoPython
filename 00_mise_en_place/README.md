# Module 00 : mise en route

> **Objectifs du module**
> - Installer Python 3.14 et créer son projet de formation.
> - Configurer son éditeur une fois pour toutes.
> - Utiliser l'interpréteur interactif (REPL) comme une calculatrice.
> - Écrire, enregistrer et lancer un premier script.
> - Lire un message d'erreur sans paniquer.
>
> **Durée indicative** : 3 h
> **Prérequis** : aucun
> **Étape PyBooks** : [00, la bannière d'accueil](../fil-rouge/etape-00/)

---

## L'essentiel

### 1. Python en deux minutes

Python est un langage de programmation **généraliste**, réputé pour sa **lisibilité**. On l'utilise partout :
- applications web (Django, FastAPI) ;
- analyse de données et intelligence artificielle ;
- automatisation et scripts ;
- tests et outils de développement.

C'est l'un des langages les plus utilisés au monde.

Une nouvelle version de Python sort chaque année, en octobre. Ce cours utilise **Python 3.14**, une version récente et mature.

Un programme Python, c'est simplement du **texte** enregistré dans un fichier `.py`. Un programme nommé **interpréteur** lit ce texte et exécute les instructions, de haut en bas.

> 🔎 **Approfondissement** : comment Python exécute réellement le code, ses différentes implémentations, son cycle de versions… Voir [A1 : les coulisses de Python](../approfondissements/A1-coulisses-python/).

---

### 2. Installer Python avec uv

Le cours utilise **uv**, un outil qui installe Python et gère tout l'environnement de travail. Il fonctionne de la même façon sur Windows, macOS et Linux, et ne demande pas de droits administrateur.

**Étape 1 : installer uv**, dans un terminal (PowerShell sous Windows, Terminal sous macOS ou Linux) :

| Système | Commande |
|---|---|
| Windows | `winget install --id astral-sh.uv -e` |
| macOS | `brew install uv` |
| Linux, ou macOS sans Homebrew | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |

**Fermez le terminal et rouvrez-en un nouveau**, puis vérifiez :
```bash
uv --version
```

**Étape 2 : installer Python 3.14**
```bash
uv python install 3.14
```

**Étape 3 : créer votre projet.** Tout le travail de la formation se fait dans **un seul dossier, le vôtre**, que vous allez construire au fil des modules. Créez-le où vous voulez, **en dehors** du dossier du cours, par exemple dans vos Documents :
```bash
mkdir formation-python
cd formation-python
uv init --bare
```
`uv init --bare` crée un seul fichier, `pyproject.toml`, la **carte d'identité du projet** :
```toml
[project]
name = "formation-python"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = []
```

| Ligne | Signification |
|---|---|
| `[project]` | Le titre d'une section : ce qui suit décrit le projet |
| `name` | Le nom du projet (celui du dossier, par défaut) |
| `version` | Sa version, que l'on augmente quand on livre une nouvelle version |
| `requires-python` | La version de Python minimale : ici 3.14 ou plus |
| `dependencies` | Les bibliothèques dont le projet a besoin : aucune pour l'instant |

Ce fichier va **grandir avec le cours** : chaque fois qu'un module a besoin d'un nouvel outil, une commande `uv add` l'y ajoute, et le module explique la modification (pytest au module 08, ruff et mypy au module 13…).

Choisissez ensuite la version de Python du projet, puis préparez son environnement :
```bash
uv python pin 3.14
uv sync
```
- `uv python pin 3.14` écrit le fichier `.python-version`, qui contient simplement `3.14`.
- `uv sync` crée le dossier **`.venv`** (l'environnement du projet, avec son propre Python) et le fichier `uv.lock` (la liste exacte de ce qui est installé). Vous comprendrez précisément leur rôle au module 12.

Retenez pour l'instant une seule règle :

> 💡 **Dans ce cours, on lance toujours Python avec `uv run`**, depuis le dossier du projet : `uv run python …`. uv utilise alors automatiquement le Python du projet, avec ses outils.

**L'organisation du projet.** Pour chaque module, créez un dossier du même nom que dans le cours, avec un sous-dossier `demos/` et un sous-dossier `exercices/`. Les commandes du cours fonctionnent alors telles quelles chez vous :
```
formation-python/
├── pyproject.toml
├── .python-version
├── uv.lock
├── .venv/                  ← créé par uv, on n'y touche pas
├── outils/
│   └── verifier_poste.py   ← fourni par le formateur (section 3)
└── 00-mise-en-route/
    ├── demos/
    └── exercices/
```

> ⚠️ **Piège : ne créez pas votre projet à l'intérieur du dossier du cours.** Deux `pyproject.toml` imbriqués se marchent dessus, et uv ne sait plus lequel utiliser.

**Étape 4 : vérifier**, toujours dans le dossier `formation-python` :
```bash
uv run python --version
```
```
Python 3.14.8
```
Le dernier chiffre peut différer : l'important est **3.14**.

> ⚠️ **Piège (Windows) : la commande `python` ouvre le Microsoft Store.**
> Windows fournit un faux `python` qui renvoie vers le Store. Avec `uv run python`, le problème ne se pose pas. Pour le supprimer définitivement : *Paramètres → Applications → Paramètres avancés des applications → Alias d'exécution d'application*, puis désactivez `python.exe` et `python3.exe`.

---

### 3. Régler le poste une fois pour toutes

**Les accents (Windows uniquement).** Par défaut, Python 3.14 sous Windows peut mal afficher ou mal lire les caractères accentués dans certaines situations (`Ã©` au lieu de `é`). Une variable d'environnement règle le problème une fois pour toutes :
1. Menu Démarrer → tapez **« variables d'environnement »** → *Modifier les variables d'environnement pour votre compte*.
2. Dans *Variables utilisateur*, cliquez sur **Nouvelle…**
3. Nom : `PYTHONUTF8`, valeur : `1`.
4. Validez, puis **fermez et rouvrez** vos terminaux et votre éditeur.

Vous comprendrez la cause exacte de ce problème au module 11, avec les fichiers.

> 🆕 **Nouveauté 3.15** : ce réglage devient le comportement par défaut.

**Vérification automatique.** Le formateur vous fournit un petit programme de diagnostic, `verifier_poste.py` : c'est **le seul fichier que vous n'écrivez pas vous-même**. Placez-le dans un dossier `outils/` de votre projet, puis lancez-le depuis le dossier `formation-python` :
```bash
uv run python outils/verifier_poste.py
```
```
[OK] Python 3.14 ou plus
[OK] Environnement virtuel du projet actif
[OK] Mode UTF-8 actif
[..] pytest pas encore installé (normal avant le module 08)
[..] ruff pas encore installé (normal avant le module 13)
[..] mypy pas encore installé (normal avant le module 13)
Le poste est prêt pour la formation.
```
Les lignes `[..]` sont normales : ces outils s'installent plus tard, au module qui en a besoin. Relancez le programme à ce moment-là : elles passeront à `[OK]`. Tant qu'une ligne affiche `[KO]`, demandez de l'aide au formateur.

---

### 4. Configurer l'éditeur

Le cours utilise **PyCharm** (gratuit depuis 2025 : une seule édition, dont les fonctions de base sont libres d'usage, y compris en entreprise). VS Code convient aussi : voir l'encadré plus bas.

**PyCharm**
1. *File → Open…* : ouvrez le **dossier** `formation-python` (pas un fichier isolé).
2. Choisissez l'interpréteur du projet : `Ctrl+Alt+S` (*Settings*) → *Python* → *Interpreter* → *Add Interpreter* → *Add Local Interpreter* → type d'environnement **uv** → sélectionnez l'environnement existant (le `.venv` du projet) → *OK*. En bas à droite de la fenêtre, PyCharm doit afficher **Python 3.14** et le nom du projet.
3. Pour lancer un fichier, utilisez le **terminal intégré** (*View → Tool Windows → Terminal*, ou `Alt+F12`) et la commande `uv run python …` du cours. Le bouton ▶ de PyCharm fonctionne aussi, mais il lance le programme **depuis le dossier du fichier** : les programmes qui lisent ou écrivent des fichiers (à partir du module 11) ne trouveraient pas leurs données. Pour que ▶ se comporte comme `uv run`, réglez une fois pour toutes : *Run → Edit Configurations… → Edit configuration templates… → Python* → *Working directory* : le dossier `formation-python`.
4. La remise en forme automatique : *Settings → Tools → Actions on Save* → cochez **Reformat code**. PyCharm corrige alors l'indentation et les espaces à chaque sauvegarde (`Ctrl+S`). Au module 13, on lui confiera cette tâche avec l'outil **ruff**.

> 💡 PyCharm enregistre ses réglages dans un dossier `.idea/` du projet. N'y touchez pas à la main.

> 🔎 **VS Code, si vous le préférez**
> 1. *Fichier → Ouvrir le dossier…* : le dossier `formation-python`.
> 2. Installez les extensions *Python* (Microsoft), qui installe aussi *Pylance* et le débogueur, et *Ruff* (Astral).
> 3. Créez le fichier `.vscode/settings.json` :
>    ```json
>    {
>      "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
>      "[python]": {
>        "editor.defaultFormatter": "charliermarsh.ruff",
>        "editor.formatOnSave": true
>      },
>      "terminal.integrated.env.windows": { "PYTHONUTF8": "1" },
>      "files.encoding": "utf8",
>      "files.eol": "\n"
>    }
>    ```
>    Sous macOS et Linux, le chemin de l'interpréteur est `${workspaceFolder}/.venv/bin/python`.
> 4. En bas à droite, quand un fichier `.py` est ouvert, VS Code doit afficher **3.14** et **.venv**. Sinon : `Ctrl+Shift+P` → *Python: Select Interpreter*.
>
> L'extension Ruff remet le code en forme à chaque sauvegarde, avec ses réglages par défaut ; on les choisira au module 13.

---

### 5. Le REPL : Python en direct

Le **REPL** (*Read-Eval-Print Loop*, « lire, évaluer, afficher, recommencer ») est un mode où Python exécute chaque ligne dès qu'on appuie sur Entrée. Il est idéal pour **essayer** quelque chose rapidement.

```bash
uv run python
```
```
Python 3.14.8 (…) on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
L'invite `>>>` attend une instruction. Python sert d'abord de **calculatrice** :

```python
>>> 2 + 3
5
>>> 7 * 6
42
>>> 10 / 4
2.5
>>> (12.50 + 7.90) * 2
40.8
```

Et il sait afficher du texte, placé entre guillemets :

```python
>>> print("Bonjour !")
Bonjour !
```

Pour quitter : tapez `exit` puis Entrée.

> 💡 Ce qu'on tape dans le REPL est **perdu** à la fermeture. Le REPL sert à essayer ; un programme s'écrit dans un **fichier**.

> Démo : [`demos/01_premier_script.md`](demos/01_premier_script.md) (partie REPL)

---

### 6. Le premier script

Un **script** est un fichier `.py` qui contient des instructions. Python les exécute **de haut en bas**, une par une.

1. Dans PyCharm, créez le dossier `00-mise-en-route` dans votre projet, puis le fichier `bonjour.py` dedans (clic droit sur le dossier → *New → Python File*).
2. Écrivez :

```python
"""Mon premier programme Python."""

# Une ligne qui commence par # est un commentaire : Python l'ignore.
print("Bonjour !")
print("Je découvre Python.")
print("Deux plus trois font", 2 + 3)
```

3. Enregistrez (`Ctrl+S`).
4. Dans le terminal intégré (`Alt+F12`), depuis le dossier `formation-python`, lancez :

```bash
uv run python 00-mise-en-route/bonjour.py
```
```
Bonjour !
Je découvre Python.
Deux plus trois font 5
```

Ce qu'il faut retenir :
- **`print(...)`** affiche ce qu'on lui donne. Plusieurs éléments séparés par des virgules sont affichés à la suite, séparés par un espace.
- Le **texte** s'écrit entre guillemets : `"Bonjour !"`. Les **nombres** et les calculs s'écrivent sans guillemets : `2 + 3`.
- Le texte entre **triples guillemets** en toute première ligne décrit le rôle du fichier. On l'appelle la **docstring** du fichier : tous les fichiers du cours en ont une.
- **`#`** commence un commentaire, destiné aux humains.

> ⚠️ **Piège** : `print("2 + 3")` affiche `2 + 3`, alors que `print(2 + 3)` affiche `5`. Entre guillemets, c'est du **texte**, pas un calcul.

> Démo : [`demos/01_premier_script.py`](demos/01_premier_script.md)

---

### 7. Lire un message d'erreur

Les erreurs font partie du quotidien de tout développeur, débutant comme expérimenté. Ce qui compte, c'est de savoir les **lire**. Un message d'erreur Python se lit **de bas en haut** :

```
  File "C:\…\bonjour.py", line 3
    print("Bonjour !)
          ^
SyntaxError: unterminated string literal (detected at line 3)
```

| Élément | Où | Ici |
|---|---|---|
| **Le type d'erreur** | dernière ligne, avant les deux-points | `SyntaxError` : le texte n'est pas du Python valide |
| **Le message** | dernière ligne, après les deux-points | le texte (*string*) n'est pas terminé |
| **Le fichier et la ligne** | ligne `File …, line …` | ligne 3 |
| **L'endroit précis** | le `^` sous le code | le guillemet ouvrant |

Les erreurs les plus fréquentes au début :

| Erreur | Cause habituelle |
|---|---|
| `SyntaxError` | Guillemet ou parenthèse non fermé, virgule oubliée… |
| `IndentationError` | Espaces en trop (ou manquants) en début de ligne |
| `NameError: name 'prnt' is not defined` | Faute de frappe dans un nom. Python propose souvent la correction : `Did you mean: 'print'?` |
| `TypeError` | Opération impossible entre deux types, par exemple ajouter un texte et un nombre |

> 💡 Une `SyntaxError` est détectée **avant** que la moindre ligne s'exécute : rien ne s'affiche. Les autres erreurs n'apparaissent qu'**au moment** où Python atteint la ligne fautive : les lignes précédentes, elles, se sont exécutées.

> Démo : [`demos/02_lire_une_erreur.py`](demos/02_lire_une_erreur.md)

---

## 🔎 Approfondissement

Ces sections ne sont pas nécessaires pour la suite immédiate du cours.

### Le REPL moderne (Python 3.13+)
- **Flèche ↑** : rappelle les instructions précédentes, y compris un bloc entier de plusieurs lignes.
- **Tab** : complétion automatique.
- **F1** : aide ; **F2** : historique ; **F3** : mode collage, pour coller un long morceau de code.
- `_` contient le dernier résultat affiché : `>>> 7 * 6` puis `>>> _ + 1` donne `43`.

### Comment le terminal trouve-t-il `python` ?
Quand on tape une commande, le terminal la cherche dans une liste de dossiers : la variable d'environnement **`PATH`**. Il exécute la **première** trouvée. S'il existe plusieurs Python sur la machine, `python` peut donc désigner un autre Python que celui du cours. C'est pour cela qu'on utilise `uv run python`, qui choisit toujours le bon.
Pour voir tous les `python` accessibles : `Get-Command python -All` (PowerShell) ou `which -a python3` (macOS, Linux).

### Autres méthodes d'installation
En entreprise, vous rencontrerez aussi :
- l'installateur de [python.org](https://www.python.org/downloads/) (cochez **« Add python.exe to PATH »** sous Windows) ;
- le gestionnaire d'installation `py install 3.14` de Windows ;
- Homebrew sous macOS (`brew install python@3.14`) ;
- les paquets de la distribution sous Linux.

⚠️ Sous macOS et Linux, **ne modifiez jamais** le Python fourni par le système : le système d'exploitation en dépend.

---

## Démos du module

| # | Démo | Notion |
|---|---|---|
| 01 | [premier_script](demos/01_premier_script.md) | REPL, `print`, texte et nombres, commentaires, ordre d'exécution |
| 02 | [lire_une_erreur](demos/02_lire_une_erreur.md) | Provoquer, lire et corriger les erreurs courantes |

## Exercices d'entraînement (facultatifs)

| # | Exercice | Difficulté |
|---|---|---|
| 01 | [Python comme calculatrice](exercices/exo01_calculatrice/enonce.md) | ★ |
| 02 | [Corriger un script cassé](exercices/exo02_corriger_erreurs/enonce.md) | ★ |

## Fil rouge

➡️ **[Étape 00 de PyBooks : la bannière d'accueil](../fil-rouge/etape-00/enonce.md)**

## À retenir

- On installe Python avec **uv**, et on le lance **toujours** avec `uv run python`.
- Votre projet `formation-python` naît avec `uv init --bare` : son `pyproject.toml` grandira au fil des modules. `uv sync` prépare son environnement, `uv run python outils/verifier_poste.py` vérifie le poste.
- Le **REPL** (`uv run python`) sert à essayer ; un **script** (`uv run python fichier.py`) s'exécute de haut en bas.
- `print(...)` affiche ; le texte se met entre guillemets ; `#` commence un commentaire.
- Un message d'erreur se lit **de bas en haut** : le type, le message, puis la ligne.
