#Faça um algoritmo que leia 4 números inteiros e apresente a média
#(Se (varNumero % 2 == 0) ele é par)
def soma(numero1, numero2, numero3, numero4):
    total = 0

    if (numero % 2 == 0):
        total += numero1
    if (numero % 2 == 0):
        total += numero2
    if (numero % 2 == 0):
        total += numero3
    if (numero % 2 == 0):
        total += numero4
    return total

def contaPares(numero1, numero2, numero3, numero4):
    total = 0

    if(numero % 2 == 0):
        total += 1
    if(numero % 2 == 0):
        total += 1
    if(numero % 2 == 0):
        total += 1
    if(numero % 2 == 0):
        total += 1
    return total

def main():
    numero1 = int(input("Digite o primeiro numero"))
    numero2 = int(input("Digite o segundo numero"))
    numero3 = int(input("Digite o terceiro numero"))
    numero4 = int(input("Digite e o quarto numero"))

    totalSoma = soma(numero1, numero2, numero3, numero4)
    totalPares = quantidade(numero1, numero2, numero3, numero4)
    media = totalSoma / totalPares
    print(f"A soma dos numeros é: {totalSoma}")
    print(f"A media dos numeros é: {media}")

if __name__ == '__main__':
    main()