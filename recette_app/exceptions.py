class ApplicationRecetteError(Exception):
    """Classe de base pour les exceptions de l'application."""
    pass

class RecetteInvalideError(ApplicationRecetteError):
    """Exception levée quand les données d'une recette sont incorrectes."""
    pass

class DoublonRecetteError(ApplicationRecetteError):
    """Exception levée quand on tente d'ajouter une recette déjà existante."""
    pass

class FichierDonneesError(ApplicationRecetteError):
    """Exception levée lors d'un problème avec le stockage des données."""
    pass
