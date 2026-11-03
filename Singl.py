class Configuration:
    _instance = None
    _inscrit = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._inscrit:
            self.langue = "fr"
            self.annee_universitaire = "2026-2027"
            self._inscrit = True


config1 = Configuration()
config1.langue = "ar"
config2 = Configuration()

print(config2.langue)
print(config1 is config2)





