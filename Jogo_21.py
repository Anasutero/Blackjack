import random

# Classe Jogador representa um jogador no jogo
class Jogador:
    def __init__(self, nome, idade, saldo):
        self.nome = nome
        self.idade = idade
        self.pontos = 0
        self.cartas_na_mao = []
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo  # Método para acessar o saldo privado

    def fazer_aposta(self, valor_aposta):
        if self.idade >= 18 and valor_aposta <= self.saldo:
            self.__saldo -= valor_aposta  # Deduz a aposta do saldo do jogador
            return valor_aposta  # Retorna o valor da aposta
        else:
            print("Você não pode fazer essa aposta.")
            return 0  # Retorna 0 se a aposta não for válida

    def receber_carta(self, carta):
        self.cartas_na_mao.append(carta)  # Adiciona a carta à mão do jogador
        self.pontos += carta  # Adiciona o valor da carta aos pontos do jogador

    def ganhar_aposta(self, valor_aposta):
        self.__saldo += valor_aposta  # Adiciona o valor da aposta ao saldo do jogador quando ganha


# Classe Dealer representa o dealer no jogo
class Dealer:
    def __init__(self):
        self.cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Cartas disponíveis no jogo

    def sortear_carta(self):
        return random.choice(self.cartas)  # Sorteia uma carta aleatória do baralho


# Classe Jogo representa o jogo do 21
class Jogo:
    def __init__(self):
        self.dealer = Dealer()  # Cria um objeto Dealer para distribuir cartas
        self.jogadores = []  # Lista para armazenar os jogadores

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)  # Adiciona um jogador à lista de jogadores

    def jogar(self):
        while True:
            print("\n================JOGO DO 21=====================")
            print("==============QUEM FIZER 21 GANHA!!===========")
            print("==================COMEÇOU===================")
            jogador_vencedor = None  # Variável para armazenar o jogador vencedor da rodada
            maior_pontuacao = 0  # Variável para armazenar a maior pontuação na rodada
            dinheiro_apostado = 0  # Variável para armazenar o total de dinheiro apostado na rodada

            # Loop para distribuir cartas aos jogadores e realizar as apostas
            for jogador in self.jogadores:
                jogador.cartas_na_mao = []  # Reinicializa as cartas na mão do jogador
                jogador.pontos = 0  # Reinicializa os pontos do jogador
                print(f"\n{jogador.nome}, é sua vez, o Dealer distribuirá as cartas:")
                for _ in range(2):
                    carta = self.dealer.sortear_carta()  # Sorteia uma carta para o jogador
                    print(f"Você tirou um {carta}")
                    jogador.receber_carta(carta)  # Adiciona a carta à mão do jogador
                print(f"Total de pontos: {jogador.pontos}")

                aposta = int(input(f"{jogador.nome}, faça sua aposta: "))  # Pede ao jogador para fazer uma aposta
                valor_aposta = jogador.fazer_aposta(aposta)  # Realiza a aposta e obtém o valor da aposta
                dinheiro_apostado += valor_aposta  # Adiciona o valor da aposta ao total de dinheiro apostado

                # Loop para o jogador decidir se quer continuar tirando cartas ou parar
                while jogador.pontos < 21:
                    verificacao = input("Digite 1 para sortear carta ou 2 para parar: ")
                    if verificacao == "1":
                        carta = self.dealer.sortear_carta()  # Sorteia uma carta para o jogador
                        print(f"Você tirou um {carta}")
                        jogador.receber_carta(carta)  # Adiciona a carta à mão do jogador
                        print(f"Total de pontos: {jogador.pontos}")
                    elif verificacao == "2":
                        print("Você escolheu parar!")
                        break
                    else:
                        print("Opção inválida! Insira 1 para sortear carta ou 2 para parar.")

                # Verifica se o jogador tem uma pontuação válida e se é a maior na rodada
                if jogador.pontos <= 21 and jogador.pontos > maior_pontuacao:
                    maior_pontuacao = jogador.pontos
                    jogador_vencedor = jogador  # Atualiza o jogador vencedor e a maior pontuação

            # Se houver um jogador vencedor, exibe as informações sobre a rodada
            if jogador_vencedor:
                print(f"\n{jogador_vencedor.nome} é o vencedor com {maior_pontuacao} pontos!")
                jogador_vencedor.ganhar_aposta(dinheiro_apostado)  # O jogador vencedor ganha o dinheiro apostado
                print(f"Dinheiro ganho por {jogador_vencedor.nome}: {dinheiro_apostado}")
                print(f"Saldo final de {jogador_vencedor.nome}: {jogador_vencedor.saldo}")
            else:
                print("\nNenhum jogador venceu. Todos ultrapassaram 21 pontos.")

            # Pergunta aos jogadores se desejam jogar novamente
            verificacao2 = input(f"\nDeseja jogar novamente? Sim / Não: ").lower()
            if verificacao2 == "sim":
                continue  # Reinicia o jogo se os jogadores querem jogar novamente
            elif verificacao2 == "nao":
                print("\nOk, obrigado por jogar!")
                print("\nFim do jogo!")
                break  # Encerra o jogo se os jogadores não querem jogar novamente


# Inputs para adicionar nome e idade dos jogadores
nome_jogador1 = input("Insira o nome do Jogador 1: ")
idade_jogador1 = int(input("Insira a idade do jogador 1: "))
saldo_jogador1 = int(input("Insira o saldo do jogador 1: "))
nome_jogador2 = input("\nInsira o nome do Jogador 2: ")
idade_jogador2 = int(input("Insira a idade do jogador 2: "))
saldo_jogador2 = int(input("Insira o saldo do jogador 2: "))

jogador1 = Jogador(nome_jogador1, idade_jogador1, saldo_jogador1)
jogador2 = Jogador(nome_jogador2, idade_jogador2, saldo_jogador2)

jogo = Jogo()
jogo.adicionar_jogador(jogador1)
jogo.adicionar_jogador(jogador2)
jogo.jogar()

