def calculadora():
    
    print("Bem-vindo à calculadora da tia Drika!")
    print("Escolha o que vamos fazer:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")

    while True:
        escolha = input("Digite a operação desejada (1/2/3/4/0): ")

        if escolha == '0':
            print("Obrigada por usar a calculadora da tia Drika!")
            break

        if escolha in ('1', '2', '3', '4'):
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))

            if escolha == '1':
                resultado = num1 + num2
                print("A soma de ", (num1), "e" (num2), "é igual a " (resultado))
            elif escolha == '2':
                resultado = num1 - num2
                print("A diferença entre ", (num1), "e" (num2), "é igual a " (resultado))
            elif escolha == '3':
                resultado = num1 * num2
                print("O produto de ", (num1), "e" (num2), "é igual a " (resultado))
            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print("O quociente de ", (num1), "e" (num2), "é igual a " (resultado))
                else:
                    print("Erro: Não é possível dividir por zero.")
        else:
            print("Opção inválida. Por favor, escolha uma operação válida (1/2/3/4/0).")

calculadora()
