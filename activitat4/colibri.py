class Colibri:
    def __init__(self, especie, mida, velocitat, color, habitat):
        self.especie = especie
        self.mida = mida
        self.velocitat = velocitat
        self.color = color
        self.habitat = habitat

    # Getters
    def get_especie(self):
        return self.especie

    def get_mida(self):
        return self.mida

    def get_velocitat(self):
        return self.velocitat

    def get_color(self):
        return self.color

    def get_habitat(self):
        return self.habitat

    # Setters
    def set_velocitat(self, nova_velocitat):
        self.velocitat = nova_velocitat

    def set_color(self, nou_color):
        self.color = nou_color
