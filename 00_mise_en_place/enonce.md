# PyBooks, étape 00 : la bannière d'accueil

> **Module** : [00, mise en route](../../00-mise-en-route/)
> **Notions utilisées** : `print`, texte et nombres, commentaires, docstring de fichier
> **Durée** : 20 minutes

## Le contexte
Bienvenue dans l'équipe de **PyBooks**, une petite librairie en ligne qui vend des livres papier, des livres numériques et quelques articles cadeaux.
Pendant toute la formation, vous allez construire son application. Première mission : quand on lance le programme, il doit **accueillir le client**.

## Mise en place
1. À la racine de votre projet `formation-python`, créez un dossier **`mon-pybooks`**. C'est votre espace de travail pour tout le fil rouge.
2. Dans ce dossier, créez le fichier **`pybooks.py`**.

Vous lancerez votre programme ainsi, depuis le dossier `formation-python` :
```bash
uv run python mon-pybooks/pybooks.py
```

## Ce qu'il faut faire
Le programme doit afficher **exactement** :

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

Bonne visite !
```

Contraintes :
- Le fichier commence par une **docstring** qui décrit son rôle.
- Le nombre de titres (`1200`) et le délai (`48`) sont écrits comme des **nombres**, pas dans le texte : `print("- Plus de", 1200, "titres en stock")`. Les prochaines étapes les calculeront ; autant les traiter dès maintenant comme des valeurs.
- Une ligne de **commentaire** sépare les deux parties du programme : la bannière et les engagements.

## Vérification
- [ ] La sortie est **identique** à celle attendue, caractère pour caractère, y compris les deux lignes vides.
- [ ] Le fichier a été sauvegardé dans l'éditeur, donc mis en forme automatiquement.

## Pour aller plus loin
Ajoutez sous la bannière une ligne qui affiche le **prix moyen** d'un livre, **calculé** par Python à partir de trois prix : 12,90 €, 8,50 € et 21,00 €. Le résultat sera affiché avec beaucoup de décimales : on apprendra à l'arrondir aux modules 01 et 02.

## Et ensuite ?
À l'étape 01, la bannière accueillera la **fiche d'un livre** : titre, auteur, prix et stock, stockés dans des **variables**.
