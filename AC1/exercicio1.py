"""
Programacao Estruturada 2024.1
Barbara Malta Moraes- Matricula: 202402898892
AC 1 - Exercicio 1
02.03.24

"""

print("Ola professor, meu nome e Barbara.")

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))

# valor de delta = b ao quadrado - 4ac
delta = b**2 - 4*a*c
print("O valor de delta e: ", delta)

# valor de das raizes = -b +- raiz de delta/2a
raiz1 = (-b + delta ** 0.5) / (2 * a)
raiz2 = (-b - delta ** 0.5) / (2 * a)
(print("O valor da raiz 1 e: ", raiz1))
(print("O valor da raiz 2 e: ", raiz2))
