def verificar_idade():
    idade = int(input("Qual sua idade?"))
    if(idade >=18):
        print("É maior de idade")
    else:
        print("É menor de  idade")
verificar_idade()

def verificar_par_impar():
    numero_digitado = int(input("Digite um número inteiro: "))
    if numero_digitado % 2 == 0:
        print("O número é par.") 
    else:
        print("O número é ímpar.")

verificar_par_impar()

def verificar_aprovacao():
    nota_aluno = float(input("Digite a nota do aluno: "))
    if(nota_aluno >= 7):
        print("Aprovado")
    elif (nota_aluno <= 6):
        print("Reprovado")
        
    else:
        print("Em recuperação")

verificar_aprovacao()



