import random
while True:
    jogo = ["pedra", "papel", "tesoura"]
    jogo_aleatorio = random.choice(jogo)
    print("Selecione uma opção abaixo: \n [0]: pedra, [1]: papel, [2]: tesoura")
    while True:
        jogo_usuario = input()
        if jogo_usuario in ["0", "1", "2"]:
            jogo_usuario = int(jogo_usuario)
            break
        else:
            print("Por favor, escreva um número válido (0, 1 ou 2)")
    jogo_usuario_str = jogo[jogo_usuario]
    if jogo_aleatorio == jogo_usuario_str:
        print(f"Empate! O computador escolheu {jogo_aleatorio}.")
    elif (jogo_aleatorio == "pedra" and jogo_usuario_str == "tesoura") or \
         (jogo_aleatorio == "papel" and jogo_usuario_str == "pedra") or \
         (jogo_aleatorio == "tesoura" and jogo_usuario_str == "papel"):
        print(f"Você perdeu! O computador escolheu {jogo_aleatorio}.")
    else:
        print(f"Você venceu! O computador escolheu {jogo_aleatorio}.")
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar! Até a próxima.")
        break
