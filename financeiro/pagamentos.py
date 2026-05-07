#financeiro/pagamentos

import config 


def processar_pagamentos(funcionario, imposto_calculado):
    #utilizar o GETTER
    # o financeiro usar o GETTER do rh para obter o salário
    salario_bruto = funcionario.get_salario()
    salario_liquido = salario_bruto - imposto_calculado
    
    print("\n" + "=" * 30)
    print("HOLERITE DE PAGAMENTO")
    print("=" * 30)
    print(f"Funcionario: {funcionario.nome}")
    print(f"Cargo: {funcionario.cargo}")
    print(f"Salario: {config.MOEDA} {salario_bruto:.2f}")
    print(f"Descontos (imposto): {config.MOEDA} {imposto_calculado:.2f}")
    print(f"Valor Liquido a receber: {config.MOEDA} {salario_liquido:.2f}")
    print("=" * 30)