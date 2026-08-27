# 3. Tentativa de Login e Senha
# Simule um sistema de login simples onde o usuário tem um número limitado de tentativas
# para digitar a senha correta.
# ● Defina um nome de usuário e uma senha corretos (ex: admin e 123456).
# ● Dê ao usuário 3 tentativas para acertar a combinação.
# ● Se a senha estiver correta, imprima uma mensagem de sucesso e use o comando
# break para sair do loop.
# ● Se a senha estiver errada, informe o erro e diminua o número de tentativas
# restantes.
# ● Se as tentativas acabarem, imprima uma mensagem de bloqueio


for i in range(3):
    senha = 123456
    login = "mari@gmail.com"

    print ("Bem-Vindo à nossa plataforma.")
    usuario = input("Digite seu e-mail.")
    codigo = input("Digite sua senha.")

    if usuario == login and codigo == str(senha):
        print("Login realizado com sucesso!")
        break
    else:
        print("Login ou senha incorretos. Tente novamente.")
        tentativas_restantes = 2 - i
        if tentativas_restantes > 0:
            print(f"Você tem {tentativas_restantes} tentativas restantes.")
        else:
            print("Suas tentativas acabaram. Acesso bloqueado.")

     

