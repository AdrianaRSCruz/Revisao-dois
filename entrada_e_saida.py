def saudar():
    nome = input("Qual seu nome?")
    print("Olá, ", nome,"! Seja bem-vindo(a)!")
saudar()

def somar():
    primeiro_numero = int(input ("Digite primeiro numero: "))
    segundo_numero = int(input ("Digite segundo numero: "))
    somar = primeiro_numero + segundo_numero
    print ("A soma dos numeros é:", somar)
somar()

def multiplicar():
    primeiro_numero = int(input ("Digite primeiro numero: "))
    segundo_numero = int(input ("Digite segundo numero: "))
    multiplicar = primeiro_numero * segundo_numero
    print ("O produto dos numeros é:", multiplicar)
multiplicar()

def divisao():
    primeiro_numero = int(input ("Digite primeiro numero: "))
    segundo_numero = int(input ("Digite segundo numero: "))
    divisao = primeiro_numero/segundo_numero
    print ("O quociente dos numeros é:", divisao)
divisao()

def calcular_imc():
  altura = float(input("Digite sua altura (em cm): "))
  peso = float(input("Digite seu peso (em kg): "))

  imc = (peso / altura **2)
  

  print("Seu IMC é ", imc)

  if imc < 18.5:
    print("Abaixo do peso")
  elif imc < 25:
    print("Peso ideal")
  elif imc < 30:
    print("Sobrepeso")
  elif imc < 40:
    print("Obesidade")
  else:
    print("Obesidade mórbida")

calcular_imc()



    