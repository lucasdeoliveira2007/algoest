nome_produto = input("digite o nome do produto: ")
quantidade = int(input("insira a quantidade comprada: "))
preço = float(input("digite o preço:"))
total= quantidade * preço
desconto5 = total - total *0.5
if total <=100:
  print(f"total R${total-desconto}")
else:
  print(f"total: R${total}")
   