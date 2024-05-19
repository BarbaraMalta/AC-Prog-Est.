"""
Programação Estruturada
2024.1
21/04/2024
Barbara Malta Moraes

AC10
"""

print("-" * 20, "Exercicio 1", "-" * 20)

from operator import attrgetter

class Camiseta():
    def __init__(self, nome, cor, tamanho):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho

def ordenacao_multipla(lista, specs):
    for key, reverse in reversed(specs):
        lista.sort(key=attrgetter(key), reverse=reverse)
    return lista

while True:
    loop = int(input())
    if loop == 0 or loop > 60:
        break
    lista = [None] * loop
    cont = 0
    while cont < loop:
        nome = input()
        entrada = input()
        cor, tamanho = entrada.split(" ")
        b = Camiseta(nome, cor, tamanho)
        lista[cont] = b
        cont += 1
    specs = (('cor', False), ('tamanho', True), ('nome', False))  
    aux = ordenacao_multipla(list(lista), specs)
    cont = 0
    while cont < loop:
        print(aux[cont].cor, aux[cont].tamanho, aux[cont].nome)  # Adicionando espaço entre os atributos
        cont += 1
    print()

    print("-" * 20, "Exercicio 2", "-" * 20)
def processar_dados_arvores():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')  
    
    caso_total = int(data[0]) 
    indice = 1
    
    resultados = []
    
    for _ in range(caso_total):
        contagem_especies = {} 
        total_arvores = 0
        
        
        if data[indice] == '':
            indice += 1
        
       
        while indice < len(data) and data[indice].strip():
            especie = data[indice].strip()  
            if especie in contagem_especies:
                contagem_especies[especie] += 1 
            else:
                contagem_especies[especie] = 1  
            total_arvores += 1 
            indice += 1  
        
       
        resultado_caso = []
        for especie in sorted(contagem_especies): 
            percentual = (contagem_especies[especie] / total_arvores) * 100   
            resultado_caso.append(f"{especie} {percentual:.4f}")  
        
        resultados.append('\n'.join(resultado_caso))  
        
        indice += 1  
    
   
    print('\n\n'.join(resultados))

if __name__ == "__main__":
    processar_dados_arvores()

print("-" * 20, "Exercicio 3", "-" * 20)
import sys
import math

def calcular_area_rampa(N, H, C, L):
    base = N * C
    altura = N * H
    hipotenusa = math.sqrt(base*2 + altura*2)
    area_cm2 = hipotenusa * L
    area_m2 = area_cm2 / 10000
    return area_m2

def main():
    input = sys.stdin.read
    data = input().strip().split()
    
    i = 0
    resultados = []
    while i < len(data):
        N = int(data[i])
        H = int(data[i + 1])
        C = int(data[i + 2])
        L = int(data[i + 3])
        i += 4
        
        area_m2 = calcular_area_rampa(N, H, C, L)
        resultados.append(f"{area_m2:.4f}")
    
    for result in resultados:
        print(result)

if __name__ == "__main__":
    main()
