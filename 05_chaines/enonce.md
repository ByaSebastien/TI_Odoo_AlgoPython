# PyBooks, étape 05 : ISBN et ticket de caisse

> **Module** : [05, chaînes de caractères](../../05-chaines/)
> **Notions utilisées** : `strip`, `lower`, `replace`, `isdecimal`, indexation, parcours avec indice, f-strings avec largeur et alignement
> **Durée** : 1 h 15
> **Point de départ** : votre travail de l'étape 04, dans `formation-python/mon-pybooks/` ; si vous êtes en retard, demandez au formateur le dossier `depart/` de cette étape

## Le contexte
Trois demandes de la libraire :
1. « Les clients tapent ` Q` ou `P ` avec des espaces, et le menu ne les comprend pas. »
2. « Je saisis des ISBN toute la journée, avec des fautes de frappe. Je veux pouvoir les vérifier. »
3. « Le récapitulatif de commande doit ressembler à un vrai ticket de caisse. »

## Ce qu'il faut faire

### 1. Des saisies tolérantes
Le choix du menu et le choix du format sont nettoyés : espaces retirés, minuscules. Les `case` n'ont alors plus besoin de lister les majuscules : `case "q":` suffit.

### 2. Vérifier un ISBN-13
Ajoutez l'option **`4. Vérifier un ISBN`**. Elle demande un ISBN, le nettoie (espaces autour, tirets et espaces intérieurs retirés), puis :
- s'il ne compte pas 13 caractères : `Un ISBN-13 compte 13 chiffres, pas 12.` ;
- s'il contient autre chose que des chiffres : `Un ISBN-13 ne contient que des chiffres (et des tirets).` ;
- sinon, il calcule la **clé de contrôle** et affiche `ISBN 9782070612758 valide.` ou `ISBN 9782070612759 invalide : la clé de contrôle devrait être 8.`

**Calcul de la clé de contrôle d'un ISBN-13**
1. On prend les **12 premiers** chiffres.
2. On les multiplie alternativement par **1** et par **3** : le chiffre d'indice 0 par 1, celui d'indice 1 par 3, celui d'indice 2 par 1…
3. On additionne les résultats : c'est la somme pondérée.
4. La clé vaut `(10 - somme % 10) % 10`.
5. L'ISBN est valide si son **13e** chiffre est égal à la clé.

Exemple avec `9782070612758` :

| Indice | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chiffre | 9 | 7 | 8 | 2 | 0 | 7 | 0 | 6 | 1 | 2 | 7 | 5 |
| Poids | 1 | 3 | 1 | 3 | 1 | 3 | 1 | 3 | 1 | 3 | 1 | 3 |
| Produit | 9 | 21 | 8 | 6 | 0 | 21 | 0 | 18 | 1 | 6 | 7 | 15 |

Somme = 112 ; `112 % 10` = 2 ; `(10 - 2) % 10` = **8**. Le 13e chiffre est 8 : l'ISBN est valide.

> 💡 Pourquoi le second `% 10` ? Si la somme se termine par 0, `10 - 0` vaut 10, alors que la clé doit être un seul chiffre : `10 % 10` ramène à 0.

### 3. Le ticket de caisse
Remplacez le récapitulatif de commande par un ticket de 40 caractères de large :
```
----------------------------------------
Le Petit Prince (papier)      2 x 7.50 €
----------------------------------------
Montant HT                       15.00 €
TVA (6 %)                         0.90 €
Montant TTC                      15.90 €
Frais de port                     4.90 €
----------------------------------------
TOTAL À PAYER                    20.80 €
----------------------------------------
```
- Les largeurs sont des **constantes** : `TICKET_WIDTH = 40`, `LABEL_WIDTH = 28`…
- Les libellés sont alignés à gauche, les valeurs à droite.
- Les lignes de séparation sont construites par répétition : `"-" * TICKET_WIDTH`.
- La bannière utilise elle aussi `TICKET_WIDTH`, et centre le nom de la boutique avec `:^`.

## Tests à réaliser

| Saisie (option 4) | Résultat attendu |
|---|---|
| `978-2-07-061275-8` | `ISBN 9782070612758 valide.` |
| `9782070612759` | `ISBN 9782070612759 invalide : la clé de contrôle devrait être 8.` |
| `978 2 07 061275` | `Un ISBN-13 compte 13 chiffres, pas 12.` |
| `978207061275X` | `Un ISBN-13 ne contient que des chiffres (et des tirets).` |
| `9780306406157` | `ISBN 9780306406157 valide.` |

Et au menu : ` Q ` doit quitter, ` P ` doit être accepté comme format.

## Vérification
- [ ] Les cinq ISBN du tableau donnent le résultat attendu.
- [ ] Les colonnes du ticket sont parfaitement alignées, pour un livre papier comme pour un ebook (`sans objet`).
- [ ] Aucune largeur « magique » dans les f-strings : toutes viennent de constantes.

## Questions
1. Pourquoi convertit-on chaque **caractère** en entier (`int(candidate[index])`) au lieu de convertir tout l'ISBN avec `int(candidate)` ?
2. Le livre du jour a lui-même un ISBN. Pour vérifier qu'il est valide au démarrage, il faudrait **recopier** tout le calcul de la clé. Que pensez-vous de cette duplication ? (Réponse au module 08.)

## Pour aller plus loin
Affichez l'ISBN du livre du jour sous une forme plus lisible : `978-2070612758` (le préfixe, un tiret, puis le reste), grâce au slicing.

## Et ensuite ?
À l'étape 06, le client pourra mettre **plusieurs** livres dans un **panier** : il faudra une structure capable de contenir un nombre variable d'éléments. Ce sont les listes.
