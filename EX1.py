class CarteBancaire:
    def payer(self, montant):
        print(f"Paiement de {montant} DH par carte bancaire.")

class PayPal:
    def payer(self, montant):
        print(f"Paiement de {montant} DH avec PayPal.")


class Virement:
    def payer(self, montant):
        print(f"Paiement de {montant} DH par virement bancaire.")

class PaiementFactory:

    @staticmethod
    def creer_paiement(type_paiement):

        if type_paiement == "carte":
            return CarteBancaire()

        elif type_paiement == "paypal":
            return PayPal()

        elif type_paiement == "virement":
            return Virement()

        else:
            raise ValueError("Type de paiement inconnu")

# Programme principal
paiement1 = PaiementFactory.creer_paiement("carte")
paiement2 = PaiementFactory.creer_paiement("paypal")
paiement3 = PaiementFactory.creer_paiement("virement")

paiement1.payer(500)
paiement2.payer(250)
paiement3.payer(1000)