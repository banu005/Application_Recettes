from .models import Recette
from .exceptions import DoublonRecetteError, RecetteInvalideError


def detecter_doublon(liste_recettes, nouvelle_recette):
    """
    Indique si une recette est déjà présente dans la liste existante.
    Grâce à la méthode __eq__ de models.py, Python compare les noms.
    """
    return nouvelle_recette in liste_recettes


def ajouter_recette(liste_recettes, nouvelle_recette):
    """
    Ajoute une recette après validation.
    Lève DoublonRecetteError si la recette existe déjà.
    Retourne un tuple (succès, message) pour rester compatible avec main.py.
    """
    if not isinstance(nouvelle_recette, Recette):
        raise RecetteInvalideError("L'objet fourni n'est pas une instance de Recette.")

    if detecter_doublon(liste_recettes, nouvelle_recette):
        return False, "Cette recette existe déjà."

    liste_recettes.append(nouvelle_recette)
    return True, "Recette ajoutée avec succès !"


def lister_par_ingredient(liste_recettes, ingredient_recherche):
    """
    Filtre les recettes selon un ingrédient (insensible à la casse).
    Lève RecetteInvalideError si l'ingrédient recherché est vide.
    """
    if not ingredient_recherche or not ingredient_recherche.strip():
        raise RecetteInvalideError("L'ingrédient recherché ne peut pas être vide.")

    resultats = []
    ingredient_recherche = ingredient_recherche.lower()

    for recette in liste_recettes:
        for ing in recette.ingredients:
            if ingredient_recherche in ing.lower():
                resultats.append(recette)
                break

    return resultats