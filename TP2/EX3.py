class Voiture:

    def demarrer(self):
        print("La voiture démarre.")


class Moto:

    def demarrer(self):
        print("La moto démarre.")


class Camion:

    def demarrer(self):
        print("Le camion démarre.")


class VehiculeFactory:

    @staticmethod
    def creer_vehicule(type_vehicule):

        if type_vehicule == "voiture":
            return Voiture()

        elif type_vehicule == "moto":
            return Moto()

        elif type_vehicule == "camion":
            return Camion()

        else:
            raise ValueError("Type de véhicule inconnu")


# Programme principal
vehicule1 = VehiculeFactory.creer_vehicule("voiture")
vehicule2 = VehiculeFactory.creer_vehicule("moto")
vehicule3 = VehiculeFactory.creer_vehicule("camion")

vehicule1.demarrer()
vehicule2.demarrer()
vehicule3.demarrer()