"""
Programacao Estruturada 2024.1
Barbara Malta Moraes- Matricula: 202402898892
AC 3 :
- Exercicio 1 : Triangulos
- Exercicio 2 : Dia da Semana
- Exercicio 3 : Calculadora
15/03/2024

"""

print("-" * 20, "Tipos de Triangulo", "-" * 20)

def determina_tipo_triangulos(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        return str("Nao e um triangulo!")
    elif a == b and a == c and b == c:
        return str("e um triangulo equilatero!")
    elif a == b or a == c or b == c:
        return str("e um triangulo  isosceles!")
    elif a != b and a != c and b != c:
        return str("e um triangulo escaleno!")  

print(determina_tipo_triangulos(4, 4, 4))
print(determina_tipo_triangulos(2, 4, 4))
print(determina_tipo_triangulos(3, 4, 5))
print(determina_tipo_triangulos(1, 1, 4))
print(determina_tipo_triangulos(4, 1, 1))

print("-" * 20, "Dias da Semana", "-" * 20)

def dias_da_semana(num):
    if num == 1:
        return str("Domingo")
    elif num == 2:
        return str("Segunda-feira")
    elif num == 3:
        return str("Terca-feira")
    elif num == 4:
        return str("Quarta-feira")
    elif num == 5:
        return str("Quinta-feira")
    elif num == 6:
        return str("Sexta-feira")
    elif num == 7:
        return str("Sábado")
    else:
        return str("")
    
print(dias_da_semana(2))
print(dias_da_semana(6))
print(dias_da_semana(7))
print(dias_da_semana(9))

print("-" * 20, "Calculadora", "-" * 20)

def soma(numero1, numero2):
    return numero1 + numero2
def subtracao(numero1, numero2):
    return numero1 - numero2
def divisao(numero1, numero2):
    return numero1 / numero2
def multiplicacao(numero1, numero2):
    return numero1 * numero2

def calculadora():
    numero1 = float(input("Informe um numero: "))
    numero2 = float(input("Informe outro numero: "))
    operacao = str(input("Informe a operacao: "))
    if operacao == "soma":
        print(soma(numero1, numero2))
    elif operacao == "subtracao":
        print(subtracao(numero1, numero2))
    elif operacao == "divisao":
        print(divisao(numero1, numero2))
    elif operacao == "multiplicacao":
        print(multiplicacao(numero1, numero2))
    else:
        print("Operacao invalida")
print(calculadora())

print("-" * 50)