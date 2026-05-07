from padrao.models import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, cargo, salario):
        #super chama construtor da classe mãe
        super().__init__(nome, cpf)
        self.cargo = cargo
        self.__salario = salario

    #metodo GETTER para o financeiro e a contabilidade conseguirem ver meu salário
    def get_salario(self):
        return self.__salario

    def promover(self, novo_cargo, aumento):
        self.cargo = novo_cargo
        self.__salario = aumento
        print(f"[RH] Parabéns {self.nome}!\n Promovido à {self.cargo}.")

    