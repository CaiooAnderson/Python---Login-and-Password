import re

while True:
    login = input("Digite o seu nome de usuário: ")
    senha = input("Digite a sua senha: ")

    if isinstance(login, str):
        if re.match(r"^[a-zA-Z0-9]+$", login) and not re.search(r"[@#$]", login):
            senha = senha.strip()
            if re.match(r"^[a-zA-Z0-9@#$]+$", senha):
                if senha == "caiozin123":
                    print(f"\nBem-vindo ao site, {login}!\n")
                    break
                else:
                    print("\nA senha digitada está incorreta. Tente novamente!\n")
            else:
                print("\nA senha deve conter apenas letras, números e os caracteres especiais @, #, $. Tente novamente!\n")
        else:
            print("\nEste nome de usuário não existe ou contém caracteres especiais. Tente novamente!\n")
    else:
        print("\nErro: o nome de usuário deve ser uma string. Tente novamente!\n")
