import unittest
from recette_app.exceptions import ApplicationRecetteError, RecetteInvalideError, DoublonRecetteError

class TestExceptions(unittest.TestCase):
    def test_exceptions_inheritance(self):
        """Vérifie que les exceptions héritent de la classe de base."""
        self.assertTrue(issubclass(RecetteInvalideError, ApplicationRecetteError))
        self.assertTrue(issubclass(DoublonRecetteError, ApplicationRecetteError))

    def test_exception_messages(self):
        """Vérifie que le message d'erreur est bien passé."""
        err = RecetteInvalideError("Donnée invalide")
        self.assertEqual(str(err), "Donnée invalide")

if __name__ == "__main__":
    unittest.main()
