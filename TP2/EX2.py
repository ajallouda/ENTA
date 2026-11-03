from abc import ABC, abstractmethod


# Produit abstrait
class Document(ABC):

    @abstractmethod
    def generer(self):
        pass


# Produits concrets
class DocumentPDF(Document):

    def generer(self):
        print("Génération d'un document PDF.")


class DocumentWord(Document):

    def generer(self):
        print("Génération d'un document Word.")


class DocumentExcel(Document):

    def generer(self):
        print("Génération d'un document Excel.")


# Créateur abstrait
class GenerateurDocument(ABC):

    @abstractmethod
    def creer_document(self):
        pass

    def exporter(self):
        document = self.creer_document()
        document.generer()


# Créateurs concrets
class GenerateurPDF(GenerateurDocument):

    def creer_document(self):
        return DocumentPDF()


class GenerateurWord(GenerateurDocument):

    def creer_document(self):
        return DocumentWord()


class GenerateurExcel(GenerateurDocument):

    def creer_document(self):
        return DocumentExcel()


# Programme principal
generateurs = [
    GenerateurPDF(),
    GenerateurWord(),
    GenerateurExcel()
]

for generateur in generateurs:
    generateur.exporter()