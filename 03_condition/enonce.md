# PyBooks, étape 02 : le prix TTC au centime près

> **Module** : [02, nombres et opérateurs](../../02-nombres-operateurs/)
> **Notions utilisées** : opérateurs, `Decimal`, `quantize`, `ROUND_HALF_UP`, import
> **Durée** : 45 minutes
> **Point de départ** : votre travail de l'étape 01, dans `formation-python/mon-pybooks/` ; si vous êtes en retard, demandez au formateur le dossier `depart/` de cette étape

## Le contexte
La comptable de PyBooks est formelle : **aucun montant ne doit être calculé avec des `float`**. Elle veut voir, pour chaque commande, le détail HT, TVA et TTC, juste au centime.

## Ce qu'il faut faire

### 1. Passer les montants en `Decimal`
- Importez `Decimal` et `ROUND_HALF_UP` en tête de fichier.
- `unit_price` devient `Decimal("7.50")`, et `FREE_SHIPPING_THRESHOLD` devient `Decimal("50")`.
- Ajoutez les constantes :

| Constante | Valeur | Rôle |
|---|---|---|
| `BOOK_VAT_RATE` | `Decimal("0.06")` | TVA des livres : 6 % |
| `SHIPPING_FEE` | `Decimal("4.90")` | Frais de port |
| `CENT` | `Decimal("0.01")` | Pas d'arrondi |

### 2. Afficher le prix TTC dans la fiche du livre
Prix TTC = prix HT × (1 + taux de TVA), arrondi au centime.

### 3. Détailler la commande
Après la saisie de la quantité, affichez :
- le **montant HT** : prix unitaire HT × quantité ;
- la **TVA** : montant HT × taux, **arrondie au centime** (`ROUND_HALF_UP`) ;
- le **montant TTC** : HT + TVA ;
- les **frais de port** ;
- le **total à payer** : TTC + frais de port.

Pour l'instant, les frais de port sont **toujours** facturés, même au-delà de 50 € : choisir de les offrir demande une condition, à l'étape 03.

Le taux de TVA s'affiche en pourcentage, **calculé** à partir de la constante : `BOOK_VAT_RATE * 100`, avec le format `:.0f` (aucune décimale).

## Résultat attendu
Avec une saisie de `2` (la bannière est inchangée) :
```
--- Livre du jour ---
Titre    : Le Petit Prince
Auteur   : Antoine de Saint-Exupéry
ISBN     : 9782070612758
Prix HT  : 7.50 €
Prix TTC : 7.95 €
En stock : 7 exemplaire(s)

Combien d'exemplaires souhaitez-vous ? 2

--- Votre commande ---
Montant HT    : 15.00 €
TVA (6 %)     : 0.90 €
Montant TTC   : 15.90 €
Frais de port : 4.90 €
Total à payer : 20.80 €
```

Avec `7` : HT 52.50 €, TVA 3.15 €, TTC 55.65 €, total 60.55 €.

## Vérification
- [ ] Aucun `float` ne sert à un montant : tous les `Decimal` sont créés à partir de **textes** (`Decimal("7.50")`) ou d'entiers.
- [ ] La TVA est arrondie avec `ROUND_HALF_UP`.
- [ ] Aucun nombre magique : `0.06`, `4.90` et `0.01` n'apparaissent que dans les constantes.

## Questions
1. Pourquoi calcule-t-on la TVA sur le **montant HT total**, plutôt que de multiplier le prix TTC unitaire déjà arrondi ? Changez temporairement le prix en `Decimal("8.25")` et commandez 3 exemplaires : comparez « 3 × prix TTC affiché » avec le montant TTC calculé par le programme.
2. Avec 7 exemplaires, le montant dépasse 50 € : le client paie pourtant les frais de port. Que manque-t-il au programme ?

## Pour aller plus loin
La libraire envisage un code promo de 10 % sur le montant TTC des articles, hors frais de port. Ajoutez une constante `PROMO_RATE = Decimal("0.10")` et affichez la ligne `Remise (10 %)`, ainsi que le nouveau total. Tous les montants restent arrondis au centime.

## Et ensuite ?
À l'étape 03, PyBooks prend des **décisions** : port offert dès 50 €, refus d'une commande supérieure au stock, TVA différente pour les articles cadeaux.
