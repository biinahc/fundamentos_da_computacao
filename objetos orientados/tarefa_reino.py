class Personagem:
    def __init__(self, nome, poder, tipo):
        self.nome = nome
        self.poder = poder
        self.tipo = tipo
        self.esquerda = None
        self.direita = None

    def exibir(self):
        print(f"{self.nome} ({self.tipo}) Poder: {self.poder}")

class Chefe(Personagem):
    def __init__(self, nome, poder, tipo, reino):
        super().__init__(nome, poder, tipo)
        self.reino = reino

    def exibir(self):
        print(f"{self.nome} ({self.tipo}) Poder: {self.poder} Reino: {self.reino}")

class ArvoreFloresta:
    def __init__(self):
        self.raiz = None

    def inserir(self, personagem):
        self.raiz = self._inserir(self.raiz, personagem)

    def _inserir(self, no, personagem):
        if no is None:
            return personagem
        if personagem.poder < no.poder:
            no.esquerda = self._inserir(no.esquerda, personagem)
        else:
            no.direita = self._inserir(no.direita, personagem)
        return no

    def percorrer_em_ordem(self):
        self._percorrer_em_ordem(self.raiz)

    def _percorrer_em_ordem(self, no):
        if no:
            self._percorrer_em_ordem(no.esquerda)
            no.exibir()
            self._percorrer_em_ordem(no.direita)

floresta = ArvoreFloresta()

floresta.inserir(Personagem("Sabrina", 30, "Animal"))
floresta.inserir(Personagem("Mago Hayssa", 70, "Mago"))
floresta.inserir(Chefe("Dragão Kamila", 90, "Chefe", "Montanhas Vermelhas"))
floresta.inserir(Personagem("Fada Keith", 50, "Fada"))
floresta.inserir(Chefe("Rei Anderson", 85, "Chefe", "Vale Dourado"))
floresta.inserir(Personagem("Sabia Eduardo", 40, "Animal"))

floresta.percorrer_em_ordem()