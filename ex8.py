senha_certa="1986"
nome_certo="Lucas"
nome=int(input("insira o nome de usuário"))
senha=int(input("insira a sua senha"))
if nome == nome_certo and senha_certa == senha:
  print("Seja bem vindo!")
else:
  print("acesso negado!")
