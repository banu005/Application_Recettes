import unittest
from recette_app.models import Recette
from recette_app.actions import ajouter_recette, lister_par_ingredient, valider_nom, valider_ingredients, valider_instructions
from recette_app.exceptions import (
    RecetteInvalideError,
    NomRecetteInvalideError,
    IngredientInvalideError,
    InstructionsInvalideError,
)


class TestValidations(unittest.TestCase):

    def test_nom_trop_court(self):
        """Test qu'un nom trop court lève NomRecetteInvalideError."""
        with self.assertRaises(NomRecetteInvalideError):
            valider_nom("ab")

    def test_nom_vide(self):
        """Test qu'un nom vide lève NomRecetteInvalideError."""
        with self.assertRaises(NomRecetteInvalideError):
            valider_nom("")

    def test_nom_que_des_chiffres(self):
        """Test qu'un nom composé uniquement de chiffres est refusé."""
        with self.assertRaises(NomRecetteInvalideError):
            valider_nom("123")

    def test_nom_valide(self):
        """Test qu'un nom correct ne lève pas d'exception."""
        valider_nom("Tarte aux pommes")  # Ne doit pas lever d'exception

    def test_ingredient_trop_court(self):
        """Test qu'un ingrédient trop court lève IngredientInvalideError."""
        with self.assertRaises(IngredientInvalideError):
            valider_ingredients(["a"])

    def test_ingredient_que_des_chiffres(self):
        """Test qu'un ingrédient composé de chiffres seuls est refusé."""
        with self.assertRaises(IngredientInvalideError):
            valider_ingredients(["42"])

    def test_ingredients_vide(self):
        """Test qu'une liste vide lève IngredientInvalideError."""
        with self.assertRaises(IngredientInvalideError):
            valider_ingredients([])

    def test_instructions_trop_courtes(self):
        """Test que des instructions trop courtes lèvent InstructionsInvalideError."""
        with self.assertRaises(InstructionsInvalideError):
            valider_instructions("Cuire.")

    def test_instructions_vides(self):
        """Test que des instructions vides lèvent InstructionsInvalideError."""
        with self.assertRaises(InstructionsInvalideError):
            valider_instructions("")


class TestAjouterRecette(unittest.TestCase):

    def setUp(self):
        self.recettes = [Recette("Omelette", ["oeuf", "sel"], "Battre les oeufs et cuire à feu doux.")]

    def test_ajouter_nouvelle_recette(self):
        """Test qu'une nouvelle recette valide est bien ajoutée."""
        nouvelle = Recette("Salade", ["laitue", "tomate"], "Mélanger tous les ingrédients.")
        succes, message = ajouter_recette(self.recettes, nouvelle)
        self.assertTrue(succes)
        self.assertEqual(len(self.recettes), 2)

    def test_ajouter_doublon_retourne_false(self):
        """Test qu'un doublon n'est pas ajouté."""
        doublon = Recette("Omelette", ["oeuf"], "Battre les oeufs et cuire à feu doux.")
        succes, _ = ajouter_recette(self.recettes, doublon)
        self.assertFalse(succes)

    def test_ajouter_doublon_insensible_casse(self):
        """Test que la détection de doublon ignore les majuscules."""
        doublon = Recette("OMELETTE", ["oeuf"], "Battre les oeufs et cuire à feu doux.")
        succes, _ = ajouter_recette(self.recettes, doublon)
        self.assertFalse(succes)

    def test_ajouter_objet_invalide_leve_exception(self):
        """Test qu'un objet non-Recette lève RecetteInvalideError."""
        with self.assertRaises(RecetteInvalideError):
            ajouter_recette(self.recettes, "pas une recette")

    def test_ajouter_recette_nom_invalide(self):
        """Test qu'une recette avec un nom trop court est refusée."""
        mauvaise = Recette("ab", ["oeuf"], "Battre les oeufs et cuire à feu doux.")
        with self.assertRaises(NomRecetteInvalideError):
            ajouter_recette(self.recettes, mauvaise)


class TestListerParIngredient(unittest.TestCase):

    def setUp(self):
        self.recettes = [
            Recette("Omelette", ["oeuf", "sel"], "Battre et cuire à feu doux."),
            Recette("Salade", ["laitue", "tomate"], "Mélanger tous les ingrédients."),
            Recette("Soupe", ["tomate", "oignon"], "Faire mijoter 20 minutes."),
        ]

    def test_recherche_trouve_recettes(self):
        """Test qu'une recherche retourne les bonnes recettes."""
        resultats = lister_par_ingredient(self.recettes, "tomate")
        self.assertEqual(len(resultats), 2)

    def test_recherche_insensible_casse(self):
        """Test que la recherche est insensible à la casse."""
        resultats = lister_par_ingredient(self.recettes, "TOMATE")
        self.assertEqual(len(resultats), 2)

    def test_recherche_aucun_resultat(self):
        """Test qu'une recherche sans résultat retourne une liste vide."""
        resultats = lister_par_ingredient(self.recettes, "chocolat")
        self.assertEqual(resultats, [])

    def test_recherche_ingredient_vide_leve_exception(self):
        """Test qu'un ingrédient vide lève IngredientInvalideError."""
        with self.assertRaises(IngredientInvalideError):
            lister_par_ingredient(self.recettes, "")


if __name__ == "__main__":
    unittest.main()