class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {}

        return cls._instance

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key):
        return self.settings.get(key)


# Test de validation
cfg1 = ConfigurationManager()
cfg2 = ConfigurationManager()

# Vérifier que les deux variables référencent le même objet
print("Même instance :", cfg1 is cfg2)

# Enregistrer des paramètres avec cfg1
cfg1.set("debug", True)
cfg1.set("api_url", "https://api.example.com")
cfg1.set("timeout", 30)

# Lire les paramètres avec cfg2
print("Debug :", cfg2.get("debug"))
print("URL de l'API :", cfg2.get("api_url"))
print("Timeout :", cfg2.get("timeout"))

# Modifier une valeur avec cfg2
cfg2.set("debug", False)

# Vérifier la modification avec cfg1
print("Debug après modification :", cfg1.get("debug"))

