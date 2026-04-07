import json
import os
from .models import Recette

FICHIER_PAR_DEFAUT = "recettes.json"

def charger_recettes(nom_fichier=FICHIER_PAR_DEFAUT):
    """
    Tente de lire le fichier JSON et de le convertir en liste d'objets Recette.
    Si le fichier n'existe pas, retourne une liste vide [].
    """
    if not os.path.exists(nom_fichier):
        return []
    
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            donnees = json.load(f)
            # Pour chaque dictionnaire dans le JSON, on crée un objet Recette
            return [Recette.from_dict(d) for d in donnees]
    except (json.JSONDecodeError, KeyError):
        # En cas d'erreur (fichier vide ou corrompu), on renvoie une liste vide
        return []

def sauvegarder_recettes(recettes, nom_fichier=FICHIER_PAR_DEFAUT):
    """
    Convertit chaque objet Recette en dictionnaire puis les écrit dans le JSON.
    """
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        # On appelle to_dict() sur chaque objet pour avoir du format standard JSON
        donnees = [r.to_dict() for r in recettes]
        # Sauvegarde proprement avec indentation pour la lisibilité humaine
        json.dump(donnees, f, indent=4, ensure_ascii=False)
