"""
Programacao Estruturada 2024.1
Barbara Malta Moraes- Matricula: 202402898892
AC 2 - Exercicio 2
05.03.24

"""
print("Ola professor, meu nome e Barbara.")

def calcula_salario(valor_hora, num_horas, irpf = 0.275):
    salario_bruto = valor_hora * num_horas
    desconto_imposto = salario_bruto * irpf
    salario_liquido = salario_bruto - desconto_imposto
    return print(round(salario_liquido, 2))
calcula_salario(20, 220)
