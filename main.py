#fazendo as importações necessários
import config
from rh.models import Funcionario
from contabil.impostos import calcular_imposto_renda
from financeiro.pagamentos import processar_pagamentos

def ligar_sistema():
    print("=" * 5, f"BEM-VINDO AO ERP DA {config.NOME_EMPRESA}", "="*5)


    #PASSO 1 - RH
    print("\n [1] MÓDULO RH: Nova Contratação")
    nome: str = input("Digite o nome: ")
    cpf: str = input("Digite o cpf: ")
    cargo: str = input("Digite o cargo: ")
    salario: float = float(input("Digite o salario: "))

    #PASSO 2- CRIANDO O OBJETO COM OS DADOS DIGITADOS
    colaborador = Funcionario(nome, cpf, cargo, salario)
    print(f"Sucesso! Colaborador Cadastrado no Sistema.")

    #PASSO 3 - Puasa para o utilizador acompanhar
    input("\nPressione ENTER para enviar os dados para a contabilidade...")
     
    #PASSO 4 - CONTABILIDADE
    print("[2] MÓDULO CONTABIL: Calulo de Tributos.")
    #lendo meu salario encapsulado 
    salario_base = colaborador.get_salario()
    #passar para a funcao de contabil p
    imposto_retido = calcular_imposto_renda(salario_base)
    print(f"Imposto Calculado com sucesso!: {config.MOEDA} {imposto_retido:.2f}")

    input("\nPressione ENTER para enviar a folha para o financeiro.")

    #PASSO 4 - FINANCEIRO
    print("[3] MODULO FINANCEIRO: Fechamento de Folha")
    #passando objeto inteiro e imposto calculado
    salario_final = processar_pagamentos(colaborador, imposto_retido)
    input("\n ==OPERAÇÃO FINALIZADA== ")



if __name__ =="__main__":
    ligar_sistema()