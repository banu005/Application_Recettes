from .models import Recette

def detecter_doublon(liste_recettes, nouvelle_recette):
    """
    Indique si une recette est déjà présente dans la liste existante.
    Grâce à la méthode __eq__ de models.py, Python sait qu'il doit 
    comparer les noms de recettes.
    """
    return nouvelle_recette in liste_recettes

def ajouter_recette(liste_recettes, nouvelle_recette):
    """
    Fonction principale pour l'ajout. 
    On vérifie le doublon avant d'ajouter.
    Retourne un tuple (succès, message).
    """
    if detecter_doublon(liste_recettes, nouvelle_recette):
        return False, "Cette recette existe déjà."
    
    # On l'ajoute à la liste des recettes chargée en mémoire
    liste_recettes.append(nouvelle_recette)
    return True, "Recette ajoutée avec succès !"

def lister_par_ingredient(liste_recettes, ingredient_recherche):
    """
    Permet de filtrer les recettes selon un ingrédient.
    """
    resultats = []
    # Mise en minuscule pour une recherche insensible à la casse
    ingredient_recherche = ingredient_recherche.lower()
    
    for recette in liste_recettes:
        # On regarde chaque ingrédient de la recette en cours
        for ing in recette.ingredients:
            # Si le mot recherché est présent dans l'ingrédient
            if ingredient_recherche in ing.lower():
                resultats.append(recette)
                # Dès qu'on en a trouvé un, on passe à la recette suivante
                break
                
    return resultats
