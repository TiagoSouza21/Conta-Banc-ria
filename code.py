def menu():
  menu = """
  ----------------- MENU ----------------------\n
  [1] Depósito
  [2] Saque
  [3] Extrato
  [4] Criar usuário
  [5] Criar conta
  [6] Listar contas
  [0] Sair

"""
  return input(menu)

def deposito(valor, saldo, extrato, /):
  if valor > 0:
    saldo += valor
    extrato += f"\nDepósito:{valor}"
    print("Depósito realizado com sucesso")
  return saldo, extrato

def Saque(valor, saldo, extrato, /):
  if saldo > valor:
    saldo -= valor
    extrato += f"\nSaque:{valor}"
    print("Saque realizado com sucesso")
  return saldo, extrato

def Extrato(saldo, extrato):
  print("\n-------EXTRATO--------")
  if extrato == "":
    print("Extrato vazio")
  else:
    print(extrato)
  print(f"\nSaldo: {saldo:.2f}")
  print("----------------------------------")

def Criar_usuario(usuarios):
  cpf = input("Digite o CPF: ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("Usuário já existe")
    return
  nome = input("Digite o nome: ")
  data_nascimento = input("Digite a data de nascimento: ")
  endereco = input("Digite o endereço: ")
  usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
  print("Usuário criado com sucesso")

def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Digite o CPF: ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("Conta criada com sucesso")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
  

def listar_contas(contas):
  for conta in contas:
    usuario = conta["usuario"]
    print(f"Agência: {conta['agencia']}")
    print(f"C/C: {conta['numero_conta']}")
    print(f"Titular: {usuario['nome']}")

def main():
  saldo = 0
  extrato = ""
  usuarios = []
  contas = []
  agencia = "0001"
  numero_conta = 0

  while True:
    opcao = menu()

    if opcao == "1":
      valor = float(input("Digite o valor do depósito: "))
      saldo, extrato = deposito(valor, saldo, extrato)
    if opcao == "2":
      valor = float(input("Digite o valor do saque: "))
      saldo, extrato = Saque(valor, saldo, extrato)
    if opcao == "3":
      Extrato(saldo, extrato)
    if opcao == "4":
      Criar_usuario(usuarios)
    if opcao == "5":
      numero_conta += len(contas) + 1
      conta = criar_conta(agencia, numero_conta, usuarios)
      if conta:
        contas.append(conta)
    if opcao == "6":
      listar_contas(contas)
    if opcao == "0":
      break
    
  
main()
