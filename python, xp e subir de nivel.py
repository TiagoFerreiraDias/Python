import random

class Jogador:
    def _init_(self, nome, vida=100):
        self.nome = nome
        self.nivel = 1
        self.xp = 0
        self.vida = vida 

    def ganhar_xp(self, valor):
        self.xp += valor
        while self.xp >= 100:  # se o xp passar de 100, tira tudo mas aumenta um nivel
            self.xp -= 100 
            self.nivel += 1

    def status(self):
        print(f"Jogador: {self.nome} | Nível: {self.nivel} | Experiência: {self.xp}/100 | Vida: {self.vida}")

    def caçar(self):
        vidinha1 = random.randint(0, 10)
        vidinha2 = random.randint(20, 50)
        vidinha3 = random.randint(30, 65)
        vidinha = random.randint(15, 35)
        sorte = random.randint(0, 10)

        if sorte >= 8:
            print("Encontraste um guaxinim com fome")
            print(f"Perdeste {vidinha2} de vida na luta")
            self.vida -= vidinha2

        elif 5 <= sorte < 8:
            print("Encontraste um papa-formigas gordo")
            print(f"Perdeste {vidinha} de vida na luta")  # VER OS DIFERENTES ADVERSÁRIOS
            self.vida -= vidinha

        elif 1 <= sorte < 5:
            print("Encontraste uma formiga venenosa, light weight")
            print(f"Perdeste {vidinha1} de vida na luta")
            self.vida -= vidinha1

        else:
            print("O mais difícil de todos...")
            print("Encontraste a temível Lagosta do Box")
            print(f"Perdeste {vidinha3} de vida na luta")
            self.vida -= vidinha3

# --------------------------------------------------------------------------------------------------
        if self.vida <= 0:
            print(f"\n\nGame Over! O(a) pequeno(a) {self.nome} morreu.\n\n")  # morreu
            self.status()
            exit()
# --------------------------------------------------------------------------------------------------
        if sorte >= 8 and vidinha1 > 4:
            print("Conseguiste derrotar o adversário, parabéns")
            self.ganhar_xp(50)
            print("Ganhaste 50 de XP")
        elif 5 <= sorte < 8 and vidinha1 > 3:
            print("Conseguiste derrotar o adversário, parabéns")
            self.ganhar_xp(20)
            print("Ganhaste 20 de XP")
        elif 1 <= sorte < 5 and vidinha1 > 1:
            print("Conseguiste derrotar o adversário, parabéns")  # VER SE CONSEGUE MATAR OS ARTISTAS
            self.ganhar_xp(10)
            print("Ganhaste 10 de XP")
        elif sorte < 1 and vidinha1 > 6:
            print("Conseguiste derrotar o adversário, parabéns")
            self.ganhar_xp(90)
            print("Ganhaste 90 de XP")
        else:
            print("Não conseguiste derrotar, womp womp")

    def descansar(self):
        print("\n0 - Descansar debaixo da bananeira")
        print("1 - Ir a casa")
        banana = int(input())

        coisa = random.randint(5, 30)
        coisa1 = random.randint(20, 60)

        if banana == 0:
            print("Ok, também serve")
            print(f"Vida recuperada: {coisa}\n")
            self.vida = min(100, self.vida + coisa)
        elif banana == 1:
            print("Excelente escolha!")
            print(f"Vida recuperada: {coisa1}\n")
            self.vida = min(100, self.vida + coisa1)

print("BEM-VINDO AO JOGUINHO DE SOBREVIVÊNCIA")
nome_jogador = input("Digite o nome do jogador: ")  # onde isto começa
jogador = Jogador(nome_jogador)

def menu():
    while True:
        print("\n__MENU")
        print("0 - Sair do Programa")
        print("1 - Mostrar Status")
        print("2 - Ir à caça")
        print("3 - Descansar (recupera hp)")
        escolha = int(input())

        if escolha == 0:
            exit("Adiós my friend")
        elif escolha == 1:
            jogador.status()
        elif escolha == 2:
            jogador.caçar()
        elif escolha == 3:
            jogador.descansar()

menu()