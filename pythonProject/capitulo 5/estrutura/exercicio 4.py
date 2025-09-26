# Faça um algoritmo que leia a idade de 5 pessoas
# e escreva quantas delas possuem idades iguais a 21 anos.
def verificaIdade21(idade1, idade2, idade3, idade4, idade5):
    contaIdade = 0

    if(idade1 == 21):
        contaIdade +=1
    if(idade2 == 21):
        contaIdade +=1
    if(idade3 == 21):
        contaIdade +=1
    if(idade4 == 21):
        contaIdade +=1
    if(idade5 == 21):
        contaIdade +=1

    print(f"O numero de idades iguais a 21 são de {contaIdade}")

def main():
    idade1 = int(input("Digite a primeira idade numero:"))
    idade2 = int(input("Digite a segunda idade numero:"))
    idade3 = int(input("Digite a terceira idade numero:"))
    idade4 = int(input("Digite a quarta idade numero:"))
    idade5 = int(input("DIgite a quinta idade numero:"))

   verificaIdade21(idade1, idade2, idade3, idade4, idade5)

if __name__ == '__main__':
    main()
