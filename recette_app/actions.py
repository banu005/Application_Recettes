from .models import Recette
from .exceptions import (
    DoublonRecetteError,
    RecetteInvalideError,
    NomRecetteInvalideError,
    IngredientInvalideError,
    InstructionsInvalideError,
)

# --- Constantes de validation ---
NOM_MIN_CARACTERES = 3
INGREDIENT_MIN_CARACTERES = 2
INSTRUCTIONS_MIN_CARACTERES = 10


def valider_nom(nom):
    # Vérifie que le nom de la recette est valide. Et lève l'exception NomRecetteInvalideError si ce n'est pas le cas.
    if not nom or not nom.strip():
        raise NomRecetteInvalideError("Le nom de la recette ne peut pas être vide.")
    if len(nom.strip()) < NOM_MIN_CARACTERES:
        raise NomRecetteInvalideError(
            f"Le nom '{nom}' est trop court (minimum {NOM_MIN_CARACTERES} caractères)."
        )
    if nom.strip().isdigit():
        raise NomRecetteInvalideError(
            f"Le nom '{nom}' ne peut pas être composé uniquement de chiffres."
        )


def valider_ingredients(ingredients):
    # Vérifie que la liste d'ingrédients est valide. Et lève l'exception IngredientInvalideError si un ingrédient est invalide.
    if not ingredients:
        raise IngredientInvalideError("La liste d'ingrédients ne peut pas être vide.")
    for ing in ingredients:
        if not ing or not ing.strip():
            raise IngredientInvalideError("Un ingrédient ne peut pas être vide.")
        if len(ing.strip()) < INGREDIENT_MIN_CARACTERES:
            raise IngredientInvalideError(
                f"L'ingrédient '{ing}' est trop court (minimum {INGREDIENT_MIN_CARACTERES} caractères)."
            )
        if ing.strip().isdigit():
            raise IngredientInvalideError(
                f"L'ingrédient '{ing}' ne peut pas être composé uniquement de chiffres."
            )


def valider_instructions(instructions):
    # Vérifie que les instructions sont suffisamment détaillées. Et lève l'exception InstructionsInvalideError si elles sont trop courtes.
    if not instructions or not instructions.strip():
        raise InstructionsInvalideError("Les instructions ne peuvent pas être vides.")
    if len(instructions.strip()) < INSTRUCTIONS_MIN_CARACTERES:
        raise InstructionsInvalideError(
            f"Les instructions sont trop courtes (minimum {INSTRUCTIONS_MIN_CARACTERES} caractères)."
        )

def detecter_doublon(liste_recettes, nouvelle_recette):
    if nouvelle_recette in liste_recettes:
        raise DoublonRecetteError("Cette recette existe déjà.")

def ajouter_recette(liste_recettes, nouvelle_recette):
    if not isinstance(nouvelle_recette, Recette):
        raise RecetteInvalideError("L'objet fourni n'est pas une instance de Recette.")

    valider_nom(nouvelle_recette.nom)
    valider_ingredients(nouvelle_recette.ingredients)
    valider_instructions(nouvelle_recette.instructions)

    detecter_doublon(liste_recettes, nouvelle_recette)  # lève l'exception DoublonRecetteError s'il y a un doublon sur la recette

    liste_recettes.append(nouvelle_recette)
    return True, "Recette ajoutée avec succès !"


def lister_par_ingredient(liste_recettes, ingredient_recherche):
    # Filtre les recettes selon un ingrédient (insensible à la casse). Et lève l'exception IngredientInvalideError si l'ingrédient recherché est vide.
    if not ingredient_recherche or not ingredient_recherche.strip():
        raise IngredientInvalideError("L'ingrédient recherché ne peut pas être vide.")

    resultats = []
    ingredient_recherche = ingredient_recherche.lower()

    for recette in liste_recettes:
        for ing in recette.ingredients:
            if ingredient_recherche in ing.lower():
                resultats.append(recette)
                break

    return resultats