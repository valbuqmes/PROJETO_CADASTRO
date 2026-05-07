#contabil/impostos

#importando variaveis globais
import config

def calcular_imposto_renda(salario_bruto):
    if salario_bruto > config.TETO_INSENCA0:
        imposto = salario_bruto * config.IMPOSTO_ALTO
    else:
        imposto = salario_bruto * config.IMPOSTO_BAIXO

    return imposto

    