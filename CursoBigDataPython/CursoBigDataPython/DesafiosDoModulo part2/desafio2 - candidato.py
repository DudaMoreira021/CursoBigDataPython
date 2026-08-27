for i in range(12):

    nascimento = int(input("Digite seu ano de nascimento: "))

    idade = 2026 - nascimento

    if idade < 18:
        print("Você é menor de 18 anos e não pode participar.")
    else:
        telefone = input("Digite seu telefone: ")
        email = input("Digite seu email: ")

        print("Cadastro realizado com sucesso!")