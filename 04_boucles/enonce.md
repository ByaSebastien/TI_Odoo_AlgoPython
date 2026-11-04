# PyBooks, étape 04 : le menu de la boutique

> **Module** : [04, boucles et débogueur](../../04-boucles-debogueur/)
> **Notions utilisées** : `while True`, `break`, `continue`, saisies validées en boucle, accumulateurs, débogueur
> **Durée** : 1 h 15
> **Point de départ** : votre travail de l'étape 03, dans `formation-python/mon-pybooks/` ; si vous êtes en retard, demandez au formateur le dossier `depart/` de cette étape

## Le contexte
Aujourd'hui, PyBooks s'arrête après une seule commande, et la moindre faute de frappe oblige à tout relancer. Une vraie boutique reste ouverte : le client navigue, commande plusieurs fois, puis s'en va.

## Ce qu'il faut faire

### 1. Le menu
Après la bannière (affichée une seule fois), le programme affiche **en boucle** :
```
=== Menu ===
1. Voir le livre du jour
2. Commander
3. Récapitulatif de la session
Q. Quitter
Votre choix :
```
- `1` : la fiche du livre (comme à l'étape 03, avec le stock **actuel**) ;
- `2` : une commande ;
- `3` : le récapitulatif ;
- `q` ou `Q` : quitter ;
- autre : `Choix inconnu : 'x'.`, puis le menu réapparaît.

### 2. Des saisies redemandées au lieu d'annuler
- **Format** : tant que la réponse n'est ni `p`, ni `P`, ni `n`, ni `N`, afficher `Format inconnu : 'x'.` et reposer la question.
- **Rupture** : si le client choisit le papier alors que le stock vaut 0, afficher `Rupture de stock : choisissez la version numérique.` et revenir au menu.
- **Quantité** : tant qu'elle est inférieure à 1, ou supérieure au stock pour un livre papier, afficher le message adapté et reposer la question.

### 3. La boutique a une mémoire
- Après une commande papier, le **stock diminue** de la quantité commandée.
- Le programme compte les **commandes passées** et cumule le **montant total** de la session.
- Le récapitulatif (`3`) affiche ces deux informations et le stock restant.
- En quittant : `Merci de votre visite ! 2 commande(s), 74.70 €.`

## Scénario de test
| Saisie | Effet attendu |
|---|---|
| `1` | Fiche : 7 exemplaires en stock |
| `2`, `x`, `p`, `0`, `9`, `7` | Format inconnu, puis papier ; quantité 0 refusée, 9 refusée (stock), 7 acceptée : **55.65 €**, port offert |
| `1` | Fiche : **rupture** |
| `2`, `p` | `Rupture de stock : choisissez la version numérique.` |
| `2`, `n`, `3` | Ebook × 3 : **19.05 €** |
| `3` | 2 commandes, **74.70 €**, stock 0 |
| `z` | `Choix inconnu : 'z'.` |
| `q` | `Merci de votre visite ! 2 commande(s), 74.70 €.` |

## Au débogueur
1. Posez un point d'arrêt sur la ligne `orders_count += 1` : cliquez dans la marge, à gauche de la ligne.
2. Lancez en mode débogage (clic droit dans `pybooks.py` → *Debug 'pybooks'*) et jouez le scénario de test : les saisies se tapent dans l'onglet *Console* du débogueur.
3. À chaque arrêt, relevez dans le panneau des variables : `stock`, `orders_count`, `session_total`, `total_to_pay`.
4. Transformez-le en point d'arrêt **conditionnel** qui ne s'arrête que pour les commandes papier (clic droit sur le point rouge, champ *Condition*) : quelle expression utilisez-vous ?

## Vérification
- [ ] Le scénario de test donne exactement les résultats attendus.
- [ ] La bannière n'est affichée qu'**une** fois.
- [ ] Les accumulateurs (`orders_count`, `session_total`) sont initialisés **avant** la boucle du menu.

## Questions
1. Dans le `case "2"`, que fait exactement le `continue` après le message de rupture ? Et le `break` à l'intérieur du `match` du format ?
2. Votre programme dépasse probablement les 120 lignes, et le calcul d'une commande est enfoui dans le menu. Imaginez qu'on veuille calculer une commande **ailleurs** (un devis par e-mail, par exemple) : que faudrait-il faire aujourd'hui ? (Réponse au module 08.)
3. Le client tape `deux` comme quantité : que se passe-t-il ? Tout le travail de la session est-il perdu ? (Réponse au module 10.)

## Pour aller plus loin
Ajoutez une option `4. Réapprovisionner` (réservée à la libraire), qui demande un nombre d'exemplaires et l'ajoute au stock. Refusez un nombre négatif ou nul.

## Et ensuite ?
À l'étape 05, PyBooks apprend à manipuler du texte : valider un ISBN-13 avec sa clé de contrôle, nettoyer les saisies (` P ` devient `p`), et imprimer un ticket de caisse bien aligné.
