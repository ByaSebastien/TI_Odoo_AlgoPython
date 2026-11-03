# PyBooks, étape 01 : la fiche d'un livre

> **Module** : [01, variables et types simples](../../01-variables-types/)
> **Notions utilisées** : variables, constantes, types, f-strings, `:.2f`, `input`, `int()`
> **Durée** : 45 minutes
> **Point de départ** : votre travail de l'étape 00, dans `formation-python/mon-pybooks/` ; si vous êtes en retard, demandez au formateur le dossier `depart/` de cette étape

## Le contexte
La bannière est en ligne. La libraire veut maintenant mettre en avant un **livre du jour**, et permettre au client d'indiquer combien d'exemplaires il souhaite.

## Ce qu'il faut faire

### 1. Des constantes pour la boutique
Les valeurs écrites « en dur » dans la bannière deviennent des **constantes**, déclarées en tête du fichier :

| Constante | Valeur |
|---|---|
| `SHOP_NAME` | `"PyBooks"` |
| `FREE_SHIPPING_THRESHOLD` | `50` |
| `CATALOG_SIZE` | `1200` |
| `SHIPPING_DELAY_HOURS` | `48` |

La bannière les utilise dans des **f-strings**. Son affichage ne change pas.

### 2. Le livre du jour
Déclarez des **variables** pour le livre :

| Variable | Valeur | Type attendu |
|---|---|---|
| `title` | Le Petit Prince | `str` |
| `author` | Antoine de Saint-Exupéry | `str` |
| `isbn` | 9782070612758 | `str` (pourquoi pas un `int` ? voir les questions) |
| `unit_price` | 7.50 | `float` |
| `stock` | 7 | `int` |

Puis affichez sa fiche, sous la bannière.

### 3. La commande
Demandez au client le nombre d'exemplaires souhaité, puis affichez le **montant hors taxes**.

## Résultat attendu
Avec une saisie de `2` :
```
========================================
       PyBooks - Librairie en ligne
========================================
Bienvenue !
Livres, ebooks et cadeaux pour lecteurs curieux.

Nos engagements :
- Livraison offerte dès 50 € d'achat
- Plus de 1200 titres en stock
- Expédition sous 48 heures

--- Livre du jour ---
Titre    : Le Petit Prince
Auteur   : Antoine de Saint-Exupéry
ISBN     : 9782070612758
Prix HT  : 7.50 €
En stock : 7 exemplaire(s)

Combien d'exemplaires souhaitez-vous ? 2
Montant HT : 15.00 €
```

## Vérification
- [ ] Aucun nombre « magique » dans les `print` : toutes les valeurs viennent de constantes ou de variables.
- [ ] Les montants s'affichent avec deux décimales.
- [ ] Les noms sont en anglais, en `snake_case` (variables) ou en `UPPER_SNAKE_CASE` (constantes).

## Questions
1. Pourquoi l'ISBN est-il un **texte** et non un nombre ? (Indice : certains ISBN commencent par `0`, et on ne fait jamais de calcul « sur » un ISBN.)
2. Que se passe-t-il si le client tape `deux` ? Et `2.5` ? Notez le nom de l'erreur : on la traitera au module 10.
3. Le client peut-il commander 20 exemplaires alors qu'il n'y en a que 7 en stock ? Que faudrait-il pour l'en empêcher ? (Réponse au module 03.)

## Pour aller plus loin
Ajoutez une variable `is_ebook` (booléen) et affichez `Format : papier` ou… attendez : choisir le texte selon la valeur d'un booléen demande une **condition**, au module 03. Pour l'instant, affichez simplement `Livre numérique : False`.

## Et ensuite ?
À l'étape 02, le montant hors taxes ne suffit plus : il faut calculer le prix **TTC**, au centime près. Vous découvrirez pourquoi un `float` n'est pas fait pour l'argent.
