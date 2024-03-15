"""
Programacao Estruturada 2024.1
Barbara Malta Moraes- Matricula: 202402898892
AC 3 - Exercicio 1
15/03/2024

"""

def determina_tipo_triangulos(a, b, c):
    if a == b and a == c and b == c:
        return str("equilatero")
    elif a == b or a == c or b == c:
        return str("isosceles")
    elif a != b and a != c and b != c:
        return str("escaleno")
    else:
        return str("nao e um triangulo")
    
print(determina_tipo_triangulos(1, 1, 4))