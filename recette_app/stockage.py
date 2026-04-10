import json
import os
from .models import Recette
from .exceptions import FichierDonneesError

FICHIER_PAR_DEFAUT = "recettes.json"


def charger_recettes(nom_fichier=FICHIER_PAR_DEFAUT):
    # Lit le fichier JSON et retourne une liste d'objets Recette. Si le fichier n'existe pas, retourne une liste vide. 
    # Sinon si le fichier est corrompu, on lève l'exception FichierDonneesError.
    if not os.path.exists(nom_fichier):
        return []

    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            donnees = json.load(f)
            return [Recette.from_dict(d) for d in donnees]
    except json.JSONDecodeError as e:
        raise FichierDonneesError(f"Le fichier '{nom_fichier}' est corrompu ou invalide : {e}")
    except KeyError as e:
        raise FichierDonneesError(f"Données manquantes dans '{nom_fichier}' : clé {e} introuvable.")


def sauvegarder_recettes(recettes, nom_fichier=FICHIER_PAR_DEFAUT):
    # Convertit chaque Recette en dictionnaire et écrit dans le JSON.
    # Lève FichierDonneesError en cas d'erreur d'écriture.
    try:
        with open(nom_fichier, 'w', encoding='utf-8') as f:
            donnees = [r.to_dict() for r in recettes]
            json.dump(donnees, f, indent=4, ensure_ascii=False)
    except OSError as e:
        raise FichierDonneesError(f"Impossible d'écrire dans '{nom_fichier}' : {e}")