class Estacionamento:
    
    total_a_pagar = 0  
    
    def __init__(self, preco_inicial=1.0, preco_hora=1.0, lista_veiculos=[]):
        if lista_veiculos is None:
            lista_veiculos = []
        self.__preco_inicial = preco_inicial
        self.__preco_hora = preco_hora
        self.__lista_veiculos = lista_veiculos
        
    
    def valores_entrada(self):
        while True:
            try:
                self.__preco_inicial = float(input('Digite a taxa inicial: € '))
                break
            except ValueError:
                print(f"ERRO! Valor inválido, Digite novamente")
        while True:
            try:
                self.__preco_hora = float(input('Digite o valor da hora: € '))
                break
            except ValueError:
                print(f"ERRO! Valor inválido, Digite novamente")        
        while True:
            try:                
                quantidade_horas = int(input('Digite a quantidade de horas: '))
                break
            except ValueError:
                print(f"ERRO! Valor inválido, Digite novamente")

                
        total_a_pagar = float(self.__preco_inicial + (self.__preco_hora * quantidade_horas)) 
        

        print(f'Taxa de estacionamento: € {self.__preco_inicial:.2f}\n'
              f'Valor da Hora: € {self.__preco_hora:.2f}\n'
              f'Tempo de permanência: {quantidade_horas} horas\n'
              f'TOTAL A PAGAR: € {total_a_pagar:.2f}') 

    
    def adicionar_veiculo(self, placa_veiculo):
        if len(placa_veiculo) == 7 and placa_veiculo[:3].isalpha() and placa_veiculo[3:].isdigit():
            self.__lista_veiculos.append(placa_veiculo)
            return True
        return False

    def remover_veiculo(self, remover_veiculo):
        if remover_veiculo in self.__lista_veiculos:
            self.__lista_veiculos.remove(remover_veiculo)
            return True
        return False

    def listar_veiculos(self):
        return self.__lista_veiculos

    def calcular_valor(self, horas):
        return self.__preco_inicial + (self.__preco_hora * horas)

    @property
    def preco_inicial(self):
        return self.__preco_inicial

    @property
    def preco_hora(self):
        return self.__preco_hora