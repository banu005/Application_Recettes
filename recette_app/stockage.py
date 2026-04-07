import json
import os
from .models import Recette

FICHIER_PAR_DEFAUT = "recettes.json"

def charger_recettes(nom_fichier=FICHIER_PAR_DEFAUT):
    """Charge les recettes depuis un fichier JSON."""
    if not os.path.exists(nom_fichier):
        return []
    
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            donnees = json.load(f)
            return [Recette.from_dict(d) for d in donnees]
    except (json.JSONDecodeError, KeyError):
        # Si le fichier est vide ou corrompu, on renvoie une liste vide
        return []

def sauvegarder_recettes(recettes, nom_fichier=FICHIER_PAR_DEFAUT):
    """Sauvegarde une liste d'objets Recette dans un fichier JSON."""
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        donnees = [r.to_dict() for r in recettes]
        json.dump(donnees, f, indent=4, ensure_ascii=False)
