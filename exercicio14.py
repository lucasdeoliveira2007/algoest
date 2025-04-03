nome_usuario=(input("insira o nome do usuario: "))
senha=(input("digite sua senha: "))
if nome_usuario == "Admin" and senha == "1234":
    print("Bem vindo")
else:
    print("acesso negado")