class cachorro:
    # Inicializador/construtor:
    def __init__(self, nome, raca, comida):
        self.nome = nome
        self.raca = raca
        self.comida = comida
        self.acordado = False
        self.feliz = False

    # Métodos:
    def comer(self):
        self.acordado == True
        if self.comida > 0:
            self.comida -= 1
            self.feliz = True
            print(f"{self.nome} comeu e agora está feliz! Comida restante: {self.comida}")
        else:
            print(f"{self.nome} não tem comida disponível!")

    def dormir(self):
        self.acordado = False
        print(f"{self.nome}, {self.raca} está dormindo.")

    def acordar(self):
        self.acordado = True
        print(f"{self.nome}, {self.raca} já acordou!")

    def brincar(self):
        self.feliz = True
        print(f"{self.nome} está feliz porque está brincando.")

    def ignorar(self):
        self.feliz = False
        print(f"{self.nome} ficou triste porque você o ignorou.")

    def latir(self):
        if self.acordado == True:
            print(f"{self.nome} está latindo!")
        else:
            print(f"{self.nome} não está latindo porque está dormindo.")

# Instanciando dois objetos da classe Cachorro
cachorro1 = cachorro("Dobby", "Galgo italiano", 15)

# Interagindo com os objetos
cachorro1.dormir()
cachorro1.acordar()
cachorro1.brincar()
cachorro1.ignorar()
cachorro1.latir()
cachorro1.comer()