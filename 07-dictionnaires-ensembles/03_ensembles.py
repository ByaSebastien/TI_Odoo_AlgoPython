"""Les ensembles : sans doublons, sans ordre, et des opérations ensemblistes."""

# Un ensemble élimine les doublons.
raw_tags = ["roman", "classique", "roman", "français"]
tags = set(raw_tags)
print("Ensemble :", sorted(tags), "-", len(tags), "éléments")

# Attention : {} est un dictionnaire vide ; l'ensemble vide s'écrit set().
print("type({})    :", type({}))
print("type(set()) :", type(set()))

# Ajouter, retirer.
tags.add("jeunesse")
tags.add("roman")  # déjà présent : aucun effet
tags.discard("policier")  # absent : aucune erreur avec discard
print("Après add/discard :", sorted(tags))

# Dédoublonner une liste.
orders = ["Dune", "Ulysse", "Dune", "Dune", "Hamlet"]
distinct_titles = set(orders)
print("Titres distincts commandés :", sorted(distinct_titles))

# Les opérations : les goûts de deux lecteurs.
alice = {"roman", "classique", "policier"}
bruno = {"classique", "sf", "policier"}
print("Union (|)                 :", sorted(alice | bruno))
print("Intersection (&)          :", sorted(alice & bruno))
print("Différence (alice - bruno):", sorted(alice - bruno))
print("Différence symétrique (^) :", sorted(alice ^ bruno))

# Test d'appartenance.
print("'sf' dans les goûts d'Alice ?", "sf" in alice)
