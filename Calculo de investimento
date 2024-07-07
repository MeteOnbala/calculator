while True:
    print('Vamos calcular seu investimento com juros compostos!')

    while True:
        try:
            Capital_inicial = float(input('Digite o valor do capital inicial: '))
            break
        except ValueError:
            print('Erro! Digite um número válido.')

    while True:
        try:
            Tempo = int(input('Digite quantos meses irá investir: '))
            break
        except ValueError:
            print('Erro! Digite um número válido.')

    while True:
        try:
            Taxa = float(input('Digite a taxa de rendimento mensal dos juros (sem digitar "%"): '))
            break
        except ValueError:
            print('Erro! Digite um número válido.')

    Taxa = Taxa / 100
    Montante_final = Capital_inicial * (1 + Taxa) ** Tempo
    Valor_juros = Montante_final - Capital_inicial

    print(f'O Montante final adquirido com o investimento durante {Tempo} meses é de R$ {Montante_final:.2f}, e o valor adquirido durante esse tempo é de R$ {Valor_juros:.2f}!')

    resposta = input('Deseja calcular novamente? (Digite "s" para sim ou qualquer outra tecla para sair): ')
    if resposta.lower() != 's':
        break
