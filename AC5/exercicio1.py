"""
Programacao Estruturada 2024.1
Barbara Malta Moraes- Matricula: 202402898892
AC 5
29/03/2024

"""

import random

def main():
    vida_aventureiro = 100
    att_aventureiro = random.randint(10 , 20)
    def_aventureiro = random.randint(1 , 5)
    print("Aventureiro: \n -Vida:", vida_aventureiro, "\n -Ataque:", att_aventureiro, "\n -Defesa:", def_aventureiro)

    vida_monstro = random.randint(60 , 80)
    att_monstro = random.randint(20 , 30)
    print("Monstro: \n -Vida:", vida_monstro, "\n -Ataque:", att_monstro)

    rodada = 1

    while vida_aventureiro >= 0 and vida_monstro >= 0:
        print("-" * 30)
        print("Rodada", rodada)
        vida_monstro = (vida_monstro - random.randint(1 , att_aventureiro))
        if vida_monstro <= 0:
            print("O monstro morreu!")
            break
        
        dano_montro = (random.randint(1 , att_monstro) - def_aventureiro)
        if dano_montro >= 0: 
                vida_aventureiro = (vida_aventureiro - dano_montro)
        if vida_aventureiro <= 0:
             print("Voce morreu!")
             break
        
        rodada += 1

        print("Aventureiro: \n -Vida:", vida_aventureiro, "\n -Ataque:", att_aventureiro, "\n -Defesa:", def_aventureiro)
        print("Monstro: \n -Vida:", vida_monstro, "\n -Ataque:", att_monstro)
main()