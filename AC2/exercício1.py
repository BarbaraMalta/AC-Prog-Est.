"""
Programacao Estruturada 2024.1
Barbara Malta Moraes- Matricula: 202402898892
AC 2 - Exercicio 1
02.03.24

"""
print("Ola professor, meu nome e Barbara.")

def resolucao_do_delta(a, b, c):
    delta = b**2 - 4*a*c
    return delta
print(resolucao_do_delta(1, -4, 3))
def resolucao_das_raizes(a, b, delta):
    raiz1 = (-b + delta ** 0.5) / (2 * a)
    raiz2 = (-b - delta ** 0.5) / (2 * a) 
    return raiz1, "<----->", raiz2
print(resolucao_das_raizes(1, -4, 4))

print("-" * 50)

def anos_bissextos(ano):
    bissexto = (ano % 4 == 0 and (not(ano % 100 == 0) or ano % 400 == 0))
    return bissexto
print(anos_bissextos(1858))
