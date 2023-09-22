import re

acesso_autorizado = False

while not acesso_autorizado:
  login = input("Digite o seu nome de usuário: ").strip()
  senha = input("Digite a sua senha: ").strip()
  
  if isinstance (login, str):
    if re.match(r"^[a-z,A-Z,0-9]+$", login):
      if (login == "Skywalker") and (senha == "caiozin123"):
        print(f"Bem-vindo ao site, {login}!")
        acesso_autorizado = True
      elif (login != "Skywalker") and (senha == "caiozin123"):
        print("Erro encontrado: O login não foi corretamente digitado. Tente novamente!")
        print("")
      elif (login == "Skywalker") and (senha != "caiozin123"):
        print("Erro encontrado: A senha não foi corretamente digitado. Tente novamente!")
        print("")
      elif (login != "Skywalker") and (senha != "caiozin123"):
        print("Erro encontrado: O login e a senha não foram corretamente digitados. Tente novamente!")
        print("")
    elif not re.match(r"^[a-z,A-Z,0-9]+$", login):
        print("O nome de usuário apenas pode conter letras de A a Z e números de 0 a 9!")