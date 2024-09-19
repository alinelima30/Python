#Menu: Digite o primeiro número:\Digite o segundo número:\selecione a operação:
# 1.soma\2.subtração\3.multiplicação\4.divisão\5.novo número\6.sair.

n1 = int(input("Primeiro Valor: "))
n2 = int(input("Segundo Valor: "))
opcao = 0
while opcao != 6:
    print("[1] para somar\n [2] para subtrair\n [3] para multiplicar\n"
          " [4] para dividir\n [5] para novo valor\n [6] para sair")
    opcao = int(input("Escolha uma Operação? "))
    if opcao == 1:
        soma = n1 + n2
        print(f"O resultado da Soma entre {n1} + {n2} = {soma}")
    elif opcao == 2:
        subtrair = n1 + n2
        print(f"O resultado da Subtração entre {n1} + {n2} = {subtrair}")
    elif opcao == 3:
        multiplicar = n1 + n2
        print(f"O resultado da Multiplicação o entre {n1} + {n2} = {multiplicar}")
    elif opcao == 4:
        dividir = n1 + n2
        print(f"O resultado da Divisão entre {n1} + {n2} = {dividir}")
    elif opcao == 5:
        n1 = int(input("Primeiro Valor: "))
        n2 = int(input("Segundo Valor: "))
    elif opcao == 6:
        print("Você saiu da Operação!")
        print("")
    else:
        print("Operação Inválida, Tente Novamente: ")
print("Fim da Operação!")