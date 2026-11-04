# PyBooks, étape 06 : le catalogue et le panier

> **Module** : [06, listes et tuples](../../06-listes-tuples/)
> **Notions utilisées** : listes, tuples, déballage, `enumerate`, `sorted`, `append`, `clear`, `in`
> **Durée** : 1 h 30
> **Point de départ** : votre travail de l'étape 05, dans `formation-python/mon-pybooks/` ; si vous êtes en retard, demandez au formateur le dossier `depart/` de cette étape

## Le contexte
Un seul livre au catalogue, une seule ligne par commande : PyBooks doit maintenant proposer **plusieurs** livres, et permettre de composer un **panier** avant de commander.

## Ce qu'il faut faire

### 1. Le catalogue : une liste de tuples
Le livre du jour est remplacé par un **catalogue** : une liste de tuples `(isbn, titre, auteur, prix papier HT)`.

| ISBN | Titre | Auteur | Prix HT | Stock |
|---|---|---|---|---|
| 9782070612758 | Le Petit Prince | Antoine de Saint-Exupéry | 7.50 | 7 |
| 9782070360024 | L'Étranger | Albert Camus | 6.90 | 3 |
| 9782253004899 | Les Misérables (tome 1) | Victor Hugo | 9.20 | 0 |
| 9782266320320 | Dune | Frank Herbert | 12.50 | 12 |
| 9782253001409 | Le Comte de Monte-Cristo | Alexandre Dumas | 11.90 | 5 |

Les stocks changent au fil de la session : ils ne peuvent pas être rangés dans les tuples, qui sont immuables. Ils sont stockés dans une **liste à part**, `stocks`, **dans le même ordre** que le catalogue.

**Nouvelle règle de prix** : un ebook coûte le prix papier moins `EBOOK_DISCOUNT = Decimal("0.20")` (20 %), arrondi au centime.

### 2. Le menu
```
=== Menu ===
1. Catalogue
2. Ajouter au panier
3. Voir le panier (2 ligne(s))
4. Valider la commande
5. Vider le panier
6. Vérifier un ISBN
Q. Quitter
```

| Option | Comportement |
|---|---|
| **1. Catalogue** | Demande `Trier par (t)itre ou par (p)rix ?`, puis affiche les livres triés. Chaque livre garde **son** numéro (sa position dans le catalogue + 1), quel que soit l'ordre d'affichage : c'est ce numéro qu'on tape pour l'ajouter au panier. |
| **2. Ajouter au panier** | Demande le numéro du livre (refusé s'il n'est pas un nombre entre 1 et 5 : `Numéro inconnu.`), le format, puis la quantité (mêmes règles qu'à l'étape 05). Ajoute la ligne `(indice, is_ebook, quantity)` au panier. Les exemplaires papier sont **réservés** : le stock diminue dès l'ajout. |
| **3. Voir le panier** | Liste numérotée des lignes, ou `Votre panier est vide.` |
| **4. Valider la commande** | Affiche le ticket de **toutes** les lignes, puis demande `Confirmer la commande ? (o/n)`. Si oui : statistiques mises à jour, panier vidé. Sinon, le panier est conservé. |
| **5. Vider le panier** | Les exemplaires papier réservés **retournent en stock**, puis le panier est vidé. |
| **6. Vérifier un ISBN** | Inchangé. |

**Frais de port** : offerts si le montant TTC des livres **papier** atteint 50 €, sans objet si le panier ne contient que des ebooks, 4.90 € sinon.

### 3. Le ticket
```
----------------------------------------
Le Petit Prince       4 x 7.50   30.00 €
[e] Dune             2 x 10.00   20.00 €
----------------------------------------
Montant HT                       50.00 €
TVA (6 %)                         3.00 €
Montant TTC                      53.00 €
Frais de port                     4.90 €
----------------------------------------
TOTAL À PAYER                    57.90 €
----------------------------------------
```
Les ebooks sont signalés par `[e]`, et les titres trop longs sont tronqués à la largeur de la colonne (slicing).

## Scénario de test
| Saisies | Résultat attendu |
|---|---|
| `1`, `p` | Catalogue trié par prix : L'Étranger, Le Petit Prince, Les Misérables, Monte-Cristo, Dune |
| `2`, `1`, `p`, `4` | `Ajouté : 4 x Le Petit Prince.` |
| `2`, `4`, `n`, `2` | `Ajouté : 2 x Dune.` |
| `2`, `3`, `p` | `Rupture de stock : choisissez la version numérique.` |
| `3` | Deux lignes |
| `4`, `n` | Le ticket ci-dessus (**57.90 €** : 31.80 € de papier TTC, sous le seuil), puis `Commande non validée` |
| `4`, `o` | `Commande validée. Merci !` |
| `3` | `Votre panier est vide.` |
| `2`, `2`, `p`, `3` puis `5` | Panier vidé : L'Étranger revient à **3** en stock |
| `1`, `t` | Tri par titre ; Le Petit Prince affiche **3** en stock (7 - 4) |
| `q` | `Merci de votre visite ! 1 commande(s), 57.90 €.` |

## Vérification
- [ ] Le scénario de test donne les résultats attendus.
- [ ] Les numéros des livres sont stables, quel que soit le tri.
- [ ] Vider le panier rend les exemplaires au stock.

## Questions
1. Pour trier par prix, on ne peut pas trier directement la liste `catalog` : le tri comparerait d'abord les ISBN. Comment avez-vous procédé ? (Indice de la solution : une liste de tuples `(clé de tri, indice)`.)
2. Les stocks sont rangés dans une liste **parallèle** au catalogue. Que se passe-t-il si l'on ajoute un livre au catalogue en oubliant d'ajouter son stock ? Ou si l'on trie `catalog` sans trier `stocks` ? (C'est le problème que résout l'étape 07.)
3. Retrouver un livre par son ISBN oblige à parcourir tout le catalogue. Est-ce raisonnable avec 1200 titres ? Et avec un million ?

## Pour aller plus loin
Permettez d'ajouter un livre au panier en tapant directement son **ISBN** (avec ou sans tirets) à la place de son numéro.

## Et ensuite ?
À l'étape 07, le catalogue devient un **dictionnaire** indexé par ISBN : plus de listes parallèles, plus de parcours pour retrouver un livre. Et les ensembles permettront de gérer les catégories.
