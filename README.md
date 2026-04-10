# Gestionnaire de Recettes CLI

Application en ligne de commande pour gérer une collection de recettes de cuisine.

## Structure du projet

```
Application_Recettes/
├── recette_app/
│   ├── __init__.py # pour que le dossier soit reconnu comme un package
│   ├── models.py        # Classe Recette
│   ├── actions.py       # Logique métier (ajouter, lister, rechercher)
│   ├── stockage.py      # Lecture/écriture du fichier JSON
│   ├── exceptions.py    # Exceptions
│   └── log.py           # Configuration du logging
├── tests/ # pour les tests
│   ├── __init__.py
│   ├── test_actions.py
│   ├── test_exceptions.py
│   └── test_stockage.py
├── main.py # pour lancer l'application
├── README.md 
├── recettes.json # pour afficher les recettes enregistrées
├── recette_app.log # pour les logs
├── requirements.txt # pour les dépendances
```

## Utilisation de la CLI

J'ajoute la version récente de Python sur la commande python3 car je suis sur linux.

### Ajouter une recette

```bash
python3 main.py add "Tarte aux pommes" --ingredients "pommes, farine, beurre, sucre" --instructions "Préparer la pâte, disposer les pommes, cuire 30min à 180°C."
```

### Lister toutes les recettes

```bash
python3 main.py list
```

### Rechercher par ingrédient

```bash
python3 main.py list --ingredient tomate
```

### Activer le mode verbose (logs détaillés)

```bash
python3 main.py --verbose list
python3 main.py --verbose add "Soupe" --ingredients "oignon, carotte" --instructions "Faire mijoter."
```

### Afficher l'aide

```bash
python3 main.py --help
python3 main.py add --help
python3 main.py list --help
```

## Lancement des tests

```bash
# Tous les tests
python3 -m unittest discover tests

# Un fichier spécifique
python3 -m unittest tests.test_actions
python3 -m unittest tests.test_stockage
python3 -m unittest tests.test_exceptions

# Avec pytest (si installé)
pytest -v # pour les tests en mode verbeux
pytest tests/ # pour les tests en mode normal
pytest --cov=. # pour les tests en mode normal avec couverture de code
```

## Dépendances

Aucune dépendance externe — uniquement la bibliothèque standard Python 3.