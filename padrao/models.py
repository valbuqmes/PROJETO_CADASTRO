#padrao/models.py

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf

    def imprimir_dados_basicos(self):
        print(f"Colaborador {self.nome} | CPF: {self.__cpf}")