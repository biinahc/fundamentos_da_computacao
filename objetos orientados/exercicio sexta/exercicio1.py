#crie as classes leao, elefante e macaco herdando de animal e sobrescreva o método falar () com sons adequados.


class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        pass

class Leao(Animal):
    def __init__(self):
        super().__init__("Leão")

    def falar(self):
        return "Rugido AAAAAUUUU ! 🦁"

class Elefante(Animal):
    def __init__(self):
        super().__init__("Elefante")

    def falar(self):
        return "trummmmmmmm! 🐘"

class Macaco(Animal):
    def __init__(self):
        super().__init__("Macaco")

    def falar(self):
        return "Uuuh uuuh aaah aaah! 🐒"

animais = [Leao(), Elefante(), Macaco()]

for animal in animais:
    print(f"{animal.nome}: {animal.falar()}")