# Application_Recettes
application_recettes/
├── main.py               
├── recette_app/
│   ├── __init__.py      # initialise en python pour reconnaitre que le dossier est un package
│   ├── models.py        # les attributs pour une recette
│   ├── actions.py       # les actions de l'utilisateur comme ajouter une recette, lister par ingrédient, détecter les doublons, exporter en JSON
│   ├── stockage.py      # gère uniquement la lecture et l'écriture du fichier recettes.json
│   ├── exceptions.py    # mettre les exceptions
│   └── log.py           # garder une trace
|
├── tests/
│   ├── __init__.py
│   ├── test_actions.py    # Test les fonctionnalités du fichier actions.py
│   └── test_stockage.py   # Test lecture/écriture JSON
│   └── test_exceptions.py   # Test lecture/écriture JSON
├── README.md
├── requirements.txt       #fichier pour ajouter les dépendances utilisés
└── recettes.json          # Le fichier où les données des recettes seront stockées

