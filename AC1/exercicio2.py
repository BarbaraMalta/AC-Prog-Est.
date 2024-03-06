print("Ola professor, meu nome e Barbara.")

ano = int(input("Informe o ano desejado: "))

print(ano % 4 == 0 and (not(ano % 100 == 0) or ano % 400 == 0))
