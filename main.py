import sys
from recette_app.models import Recette
from recette_app.actions import ajouter_recette, lister_par_ingredient
from recette_app.stockage import charger_recettes, sauvegarder_recettes
from recette_app.log import configurer_logging

def afficher_menu():
    """Affiche les options disponibles dans la console."""
    print("\n--- Gestionnaire de Recettes CLI ---")
    print("1. Ajouter une recette")
    print("2. Lister les recettes par ingrédient")
    print("3. Afficher toutes les recettes")
    print("4. Quitter")
    return input("Choisissez une option (1-4) : ")

def main():
    # Initialisation
    logger = configurer_logging()
    logger.info("Démarrage de l'application.")
    recettes = charger_recettes()

    while True:
        choix = afficher_menu()

        if choix == "1":
            nom = input("Nom de la recette : ").strip()
            ingredients_str = input("Ingrédients (séparés par des virgules) : ")
            ingredients = [i.strip() for i in ingredients_str.split(",") if i.strip()]
            instructions = input("Instructions de préparation : ").strip()

            nouvelle_recette = Recette(nom, ingredients, instructions)
            succes, message = ajouter_recette(recettes, nouvelle_recette)
            
            if succes:
                print(f"\n[OK] {message}")
                sauvegarder_recettes(recettes)
                logger.info(f"Nouvelle recette ajoutée : {nom}")
            else:
                print(f"\n[ERREUR] {message}")
                logger.warning(f"Échec de l'ajout de recette : {nom} (doublon)")

        elif choix == "2":
            ingredient = input("Entrez l'ingrédient à rechercher : ").strip()
            resultats = lister_par_ingredient(recettes, ingredient)
            
            if resultats:
                print(f"\nRecettes contenant '{ingredient}' :")
                for r in resultats:
                    print(f"- {r.nom}")
            else:
                print(f"\nAucune recette trouvée avec l'ingrédient '{ingredient}'.")

        elif choix == "3":
            if not recettes:
                print("\nAucune recette enregistrée pour le moment.")
            else:
                print("\nListe complète des recettes :")
                for r in recettes:
                    print(f"--- {r.nom} ---")
                    print(f"Ingrédients : {', '.join(r.ingredients)}")
                    print(f"Instructions : {r.instructions}\n")

        elif choix == "4":
            print("\nMerci d'avoir utilisé le gestionnaire de recettes. Au revoir !")
            logger.info("Fermeture de l'application.")
            sys.exit(0)

        else:
            print("\nOption invalide. Veuillez choisir entre 1 et 4.")

if __name__ == "__main__":
    main()
