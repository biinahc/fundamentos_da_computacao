class Boi:
    def __init__(self, nome, cor):
        self.__nome = nome
        self.__cor = cor
        self.__pontuacao = 0.0

    def get_nome(self):
        return self.__nome


    def get_cor(self):
        return self.__cor


    def get_pontuacao(self):
        return self.__pontuacao


    def set_pontuacao(self, valor):
        self.__pontuacao = valor


    def adicionar_pontos(self, valor):
        self.__pontuacao += valor

    def mostrar_info(self):
        print(f"{self.__nome} ({self.__cor}) - Pontuação: {self.__pontuacao}")
        
        
class BoiEspecial(Boi):
    def __init__(self, nome, cor, categoria_especial):
        super().__init__(nome, cor)
        self.__categoria_especial = categoria_especial

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Categoria Especial: {self.__categoria_especial}")
        
        
class jurada:
    def __init__(self, nome, nota_caprichoso, nota_garantido):
        self.nome = nome
        self.nota_caprichoso = nota_caprichoso
        self.nota_garantido = nota_garantido

    def avaliar(self):
        return {
            "Caprichoso": self.nota_caprichoso,
            "Garantido": self.nota_garantido
        }
        
class Competicao:
    def __init__(self, boi_azul, boi_vermelho, jurados):
        self.boi_azul = boi_azul
        self.boi_vermelho = boi_vermelho
        self.jurados = jurados

    def somar_pontuacoes(self):
        for jurado in self.jurados:
            notas = jurado.avaliar()
            self.boi_azul.adicionar_pontos(notas["Caprichoso"])
            self.boi_vermelho.adicionar_pontos(notas["Garantido"])

    def mostrar_campeao(self):
        azul = self.boi_azul.get_pontuacao()
        
        vermelho = self.boi_vermelho.get_pontuacao()
        
        self.boi_azul.mostrar_info()
        
        self.boi_vermelho.mostrar_info()
        
        
        if azul > vermelho:
            print(f"\nCampeão: {self.boi_azul.get_nome()}")
        elif vermelho > azul:
            print(f"\nCampeão: {self.boi_vermelho.get_nome()}")
        else:
            print("\nEmpate!")
            
            
            
caprichoso = BoiEspecial("Caprichoso", "Azul", "Coreografia perfeita")
garantido = BoiEspecial("Garantido", "Vermelho", "Melhor alegoria")

juradas = [
    jurada("Sabrina", 9.8, 9.9),
    jurada("Hayssa", 9.5, 9.9),
    jurada("Rauane", 9.9, 9.8)
]

festival = Competicao(caprichoso, garantido, juradas)
festival.somar_pontuacoes()
festival.mostrar_campeao()
            