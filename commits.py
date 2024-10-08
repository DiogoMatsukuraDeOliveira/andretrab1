while True:
    print("Este é um software de calculos matemáticos, abaixo é o menu que exibe as opções para escolha de equação.")
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Equação Quadrática")
    menu = int(input("Escolha a opção que deseja: "))

    if menu == 1:
       x = int(input("Qual o primeiro N?"))
       y = int(input("Qual o segundo N?"))
       result = x + y
       print("O resultado é: ",result)

    elif menu == 2:
       x = int(input("Qual o primeiro N?"))
       y = int(input("Qual o segundo N?"))
       result = x - y
       print("O resultado é: ",result)

    elif menu == 3:
       x = int(input("Qual o primeiro N?"))
       y = int(input("Qual o segundo N?"))
       result = x * y
       print("O resultado é: ",result)

    elif menu == 4:
       x = int(input("Qual o primeiro N?"))
       y = int(input("Qual o segundo N?"))
       result = x / y
       print("O resultado é: ",result)

    elif menu == 5:
       x = int(input("Qual o primeiro N?"))
       y = int(input("Qual o segundo N?"))
       result1 = x * x
       result2 = y * y
       print("O resultado é: ",result1, "para n1 ao quadrado e ",result2, "para n2 ao quadrado.")