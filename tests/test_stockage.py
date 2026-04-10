import unittest
import os
import json
from recette_app.models import Recette
from recette_app.stockage import charger_recettes, sauvegarder_recettes

class TestStockage(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_recettes.json"
        self.recettes = [Recette("Tarte", ["pommes"], "Cuire.")]

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_sauvegarde_et_chargement(self):
        """Test que la sauvegarde et le chargement JSON fonctionnent ensemble."""
        sauvegarder_recettes(self.recettes, self.test_file)
        chargees = charger_recettes(self.test_file)
        self.assertEqual(len(chargees), 1)
        self.assertEqual(chargees[0].nom, "Tarte")

    def test_charger_fichier_inexistant(self):
        """Test que charger un fichier inexistant renvoie une liste vide."""
        chargees = charger_recettes("fichier_fantome.json")
        self.assertEqual(chargees, [])

if __name__ == "__main__":
    unittest.main()
