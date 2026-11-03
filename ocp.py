class MaClasse:

    def __new__(cls):
        print("__new__ : Création et allocation de l'objet en mémoire")
        instance = super().__new__(cls)
        return instance

    def __init__(self, nom):
        print("__init__ : Initialisation des attributs de l'objet")
        self.nom = nom

# Utilisation
objet1 = MaClasse()
objet2 = MaClasse()
print(objet1 is objet2)  # Affiche "Test"
# Sortie :
# __new__ : Création et allocation de l'objet en mémoire
# __init__ : Initialisation des attributs de l'objet