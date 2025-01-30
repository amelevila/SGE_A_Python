class Cotxe:
    def __init__(self, marca, model, any, color, preu):
        self.marca = marca
        self.model = model
        self.any = any
        self.color = color
        self.preu = preu

    # Getters
    def get_marca(self):
        return self.marca

    def get_model(self):
        return self.model

    def get_any(self):
        return self.any

    def get_color(self):
        return self.color

    def get_preu(self):
        return self.preu

    # Setters
    def set_color(self, nou_color):
        self.color = nou_color

    def set_preu(self, nou_preu):
        self.preu = nou_preu
