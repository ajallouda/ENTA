from abc import ABC, abstractmethod


# Produit abstrait
class Notification(ABC):

    @abstractmethod
    def envoyer(self, message):
        pass


# Produits concrets
class NotificationEmail(Notification):

    def envoyer(self, message):
        print(f"Email envoyé : {message}")


class NotificationSMS(Notification):

    def envoyer(self, message):
        print(f"SMS envoyé : {message}")


class NotificationWhatsApp(Notification):

    def envoyer(self, message):
        print(f"WhatsApp envoyé : {message}")


# Créateur abstrait
class NotificationCreator(ABC):

    @abstractmethod
    def creer_notification(self):
        pass

    def notifier(self, message):
        notification = self.creer_notification()
        notification.envoyer(message)


# Créateurs concrets
class EmailCreator(NotificationCreator):

    def creer_notification(self):
        return NotificationEmail()


class SMSCreator(NotificationCreator):

    def creer_notification(self):
        return NotificationSMS()


class WhatsAppCreator(NotificationCreator):

    def creer_notification(self):
        return NotificationWhatsApp()


# Programme principal
message = "Votre inscription est confirmée."

createurs = [
    EmailCreator(),
    SMSCreator(),
    WhatsAppCreator()
]

for createur in createurs:
    createur.notifier(message)