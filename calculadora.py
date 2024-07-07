def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."
def raiz_quadrada(x):
    if x >= 0:
        return x ** (1/2)
    else:
        return "Erro! Raiz de número negativo"
def potência(x, y):
    if x == 0 and y <= 0:
        return "Erro!"
    else:
        return x ** y
def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1. Adicionar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Raiz quadrada")
        print("6. potência")
        print("7. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5/6/7): ")

        if escolha == '7':
            print("Encerrando a calculadora...")
            break

        if escolha in ('1', '2', '3', '4', '5', '6'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"{num1} + {num2} = {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                resultado = dividir(num1, num2)
                if resultado == "Erro! Divisão por zero.":
                    print(resultado)
                else:
                    print(f"{num1} / {num2} = {resultado}")
            elif escolha == '5':
                resultado = raiz_quadrada(num1)
                if resultado == "Erro! Raiz de número negativo":
                    print(resultado)
                else:
                    print(f"{num1} ** (1/2) = {resultado}")
            elif escolha == '6':
                resultado = potência(num1, num2)
                if resultado == "Erro!":
                    print(resultado)
                else:
                    print(f"{num1} ** {num2} = {resultado}")
        else:
            print("Escolha inválida. Por favor, tente novamente.")# Escreva o seu código aqui :-)
# Executa a calculadora
calculadora()
