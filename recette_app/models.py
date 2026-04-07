class Recette:
    def __init__(self, nom, ingredients, instructions):
        self.nom = nom
        self.ingredients = ingredients  # Liste de chaînes
        self.instructions = instructions

    def to_dict(self):
        """Transforme l'objet en dictionnaire pour le format JSON."""
        return {
            "nom": self.nom,
            "ingredients": self.ingredients,
            "instructions": self.instructions
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un objet Recette à partir d'un dictionnaire."""
        return cls(data["nom"], data["ingredients"], data["instructions"])

    def __eq__(self, other):
        """Permet de comparer deux recettes par leur nom (utile pour les doublons)."""
        if not isinstance(other, Recette):
            return False
        return self.nom.lower() == other.nom.lower()
