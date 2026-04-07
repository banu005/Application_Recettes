class Recette:
    """
    Cette classe est le 'plan de construction' d'une recette.
    Elle définit quelles informations (nom, ingrédients, instructions) 
    doit contenir chaque objet Recette que l'on crée.
    """
    def __init__(self, nom, ingredients, instructions):
        # On initialise les attributs de la recette avec les valeurs reçues
        self.nom = nom
        self.ingredients = ingredients  # Doit être une liste []
        self.instructions = instructions

    def to_dict(self):
        """
        Convertit l'objet Recette en un dictionnaire Python standard.
        C'est indispensable pour pouvoir l'enregistrer au format JSON plus tard.
        """
        return {
            "nom": self.nom,
            "ingredients": self.ingredients,
            "instructions": self.instructions
        }

    @classmethod
    def from_dict(cls, data):
        """
        Prend un dictionnaire (lu depuis le fichier JSON) et 
        recrée un véritable objet Recette avec.
        """
        return cls(data["nom"], data["ingredients"], data["instructions"])

    def __eq__(self, other):
        """
        Définit comment Python doit comparer deux recettes entre elles.
        Ici, on décide que deux recettes sont identiques si elles ont le même nom
        (sans tenir compte des majuscules/minuscules).
        """
        if not isinstance(other, Recette):
            return False
        return self.nom.lower() == other.nom.lower()
