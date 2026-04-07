from .models import Recette

def detecter_doublon(liste_recettes, nouvelle_recette):
    """Vérifie si une recette existe déjà dans la liste (par son nom)."""
    return nouvelle_recette in liste_recettes

def ajouter_recette(liste_recettes, nouvelle_recette):
    """Ajoute une recette si ce n'est pas un doublon."""
    if detecter_doublon(liste_recettes, nouvelle_recette):
        return False, "Cette recette existe déjà."
    
    liste_recettes.append(nouvelle_recette)
    return True, "Recette ajoutée avec succès !"

def lister_par_ingredient(liste_recettes, ingredient_recherche):
    """Renvoie une liste des recettes contenant l'ingrédient spécifié."""
    resultats = []
    # On met l'ingrédient en minuscule pour que la recherche ne soit pas sensible à la casse
    ingredient_recherche = ingredient_recherche.lower()
    
    for recette in liste_recettes:
        # On vérifie chaque ingrédient de la recette
        for ing in recette.ingredients:
            if ingredient_recherche in ing.lower():
                resultats.append(recette)
                break # On a trouvé l'ingrédient, pas besoin de vérifier les autres pour cette recette
                
    return resultats
