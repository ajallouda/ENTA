class Eleve:
    obj=None
    def __new__(cls):
        if cls.obj is None:
            cls.obj=super().__new__(cls)
        return cls.obj
    
    def __init__(self):
        self.code=15
        self.nom="Azizi"
        
    def afficher(self):
        print(f"Code : {self.code}")
        print(f"Nom : {self.nom}")

E1=Eleve()
E2=Eleve()

E1.code=27

E1.afficher()
print("================", E2 is E1, "=====================")
E2.afficher()

