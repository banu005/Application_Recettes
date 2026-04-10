import sys
import argparse
from recette_app.models import Recette
from recette_app.actions import ajouter_recette, lister_par_ingredient
from recette_app.stockage import charger_recettes, sauvegarder_recettes
from recette_app.log import configurer_logging
from recette_app.exceptions import (
    RecetteInvalideError,
    DoublonRecetteError,
    FichierDonneesError,
    NomRecetteInvalideError,
    IngredientInvalideError,
    InstructionsInvalideError,
)


def cmd_ajouter(args, recettes, logger):
    # Commande : ajouter une nouvelle recette.
    ingredients = [i.strip() for i in args.ingredients.split(",") if i.strip()]
    nouvelle_recette = Recette(args.nom.strip(), ingredients, args.instructions.strip())

    succes, message = ajouter_recette(recettes, nouvelle_recette)
    if succes:
        print(f"[OK] {message}")
        sauvegarder_recettes(recettes)
        logger.info(f"Nouvelle recette ajoutée : {args.nom}")
    else:
        raise DoublonRecetteError(f"La recette '{args.nom}' existe déjà.")


def cmd_lister(args, recettes, logger):
    # Commande : lister les recettes, avec filtre optionnel par ingrédient.
    if args.ingredient:
        resultats = lister_par_ingredient(recettes, args.ingredient)
        if resultats:
            print(f"Recettes contenant '{args.ingredient}' :")
            for r in resultats:
                print(f"  - {r.nom}")
        else:
            print(f"Aucune recette trouvée avec l'ingrédient '{args.ingredient}'.")
        logger.info(f"Recherche par ingrédient : '{args.ingredient}' → {len(resultats)} résultat(s)")
    else:
        if not recettes:
            print("Aucune recette enregistrée pour le moment.")
        else:
            print("Liste complète des recettes :")
            for r in recettes:
                print(f"\n--- {r.nom} ---")
                print(f"Ingrédients : {', '.join(r.ingredients)}")
                print(f"Instructions : {r.instructions}")
        logger.info(f"Affichage de toutes les recettes ({len(recettes)} au total)")


def main():
    parser = argparse.ArgumentParser(
        prog="recettes",
        description="Gestionnaire de recettes en ligne de commande."
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Activer le mode verbose (logs détaillés dans la console)"
    )

    subparsers = parser.add_subparsers(dest="commande", help="Commandes disponibles")

    # Sous-commande : add
    parser_add = subparsers.add_parser("add", help="Ajouter une nouvelle recette")
    parser_add.add_argument("nom", help="Nom de la recette (minimum 3 caractères)")
    parser_add.add_argument(
        "--ingredients", "-i",
        required=True,
        help="Ingrédients séparés par des virgules (ex: 'oeuf, sel, poivre')"
    )
    parser_add.add_argument(
        "--instructions", "-inst",
        required=True,
        help="Instructions de préparation (minimum 10 caractères)"
    )

    # Sous-commande : list
    parser_list = subparsers.add_parser("list", help="Afficher les recettes")
    parser_list.add_argument(
        "--ingredient", "-i",
        default=None,
        help="Filtrer par ingrédient (facultatif)"
    )

    args = parser.parse_args()

    logger = configurer_logging(verbose=args.verbose)
    logger.info("Démarrage de l'application.")

    try:
        recettes = charger_recettes()
    except FichierDonneesError as e:
        print(f"[ERREUR] Impossible de charger les données : {e}")
        logger.error(f"Erreur de chargement : {e}")
        sys.exit(1)

    if args.commande == "add":
        try:
            cmd_ajouter(args, recettes, logger)
        except NomRecetteInvalideError as e:
            print(f"[ERREUR] Nom invalide : {e}")
            logger.error(str(e))
            sys.exit(1)
        except IngredientInvalideError as e:
            print(f"[ERREUR] Ingrédient invalide : {e}")
            logger.error(str(e))
            sys.exit(1)
        except InstructionsInvalideError as e:
            print(f"[ERREUR] Instructions invalides : {e}")
            logger.error(str(e))
            sys.exit(1)
        except DoublonRecetteError as e:
            print(f"[ERREUR] Doublon : {e}")
            logger.warning(str(e))
            sys.exit(1)
        except RecetteInvalideError as e:
            print(f"[ERREUR] Recette invalide : {e}")
            logger.error(str(e))
            sys.exit(1)

    elif args.commande == "list":
        try:
            cmd_lister(args, recettes, logger)
        except IngredientInvalideError as e:
            print(f"[ERREUR] Ingrédient invalide : {e}")
            logger.error(str(e))
            sys.exit(1)

    else:
        parser.print_help()

    logger.info("Fermeture de l'application.")


if __name__ == "__main__":
    main()