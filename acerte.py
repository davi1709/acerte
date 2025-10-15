import random
numero = random.randint(1, 100)
escolha = int(input("Acerte o número entre 1 e 100!"))
while numero != escolha:
    if numero>escolha:
        escolha = int(input("O número misterioso é maior que o que você colocou!"))
    else: 
         escolha = int(input("O número misterioso é menor que o que você colocou!"))
        
print("Você acertou o número! O número era relamente", numero,".")        



