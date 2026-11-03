from abc import ABC, abstractmethod


# Produit abstrait
class SupportPedagogique(ABC):

    @abstractmethod
    def generer(self, titre):
        pass


# Produits concrets
class SupportPDF(SupportPedagogique):

    def generer(self, titre):
        print(f"Création du cours PDF : {titre}")


class SupportPowerPoint(SupportPedagogique):

    def generer(self, titre):
        print(f"Création du cours PowerPoint : {titre}")


class SupportExcel(SupportPedagogique):

    def generer(self, titre):
        print(f"Création du fichier Excel : {titre}")


# Factory
class SupportFactory:

    @staticmethod
    def creer_support(format):

        if format == "pdf":
            return SupportPDF()

        elif format == "ppt":
            return SupportPowerPoint()

        elif format == "excel":
            return SupportExcel()

        else:
            raise ValueError("Format non pris en charge")


# Programme principal
print("=== Plateforme pédagogique ===")
print("1. PDF")
print("2. PowerPoint")
print("3. Excel")

choix = input("Choisissez un format : ")

formats = {
    "1": "pdf",
    "2": "ppt",
    "3": "excel"
}

if choix in formats:

    format_choisi = formats[choix]

    support = SupportFactory.creer_support(format_choisi)

    titre = input("Saisir le titre du cours : ")

    support.generer(titre)

else:
    print("Choix invalide.")