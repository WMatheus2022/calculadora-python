def calculadora():
    while True:
        print("digite os numeros: 1. somar, 2. subtrair, 3. multiplicar, 4. divisao, 0. Sair")
        try:
            num = int(input())
            if(num == 1):
                a = float(input("digite o numero desejado: "))
                b = float(input("digite o numero desejado: "))
                print("Resultado da soma: ", a + b)
            elif(num == 2):
                a = float(input("digite o numero desejado: "))
                b = float(input("digite o numero desejado: "))
                print("Resultado da subtracao: ", a - b)
            elif(num == 3):
                a = float(input("digite o numero desejado: "))
                b = float(input("digite o numero desejado: "))
                print("Resultado da multiplicacao: ", a * b)
            elif(num == 4):
                a = float(input("digite o numero desejado: "))
                b = float(input("digite o numero desejado: "))
                print("Resultado da divisao: ", a / b)
            elif(num == 0):
                print("Encerrando calculadora")
            else:
                print("Voce encerrou a execucao.")
            break
        except:
            print("Essa opção não existe")
calculadora()
                