def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair

    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso.")
    else:
        print("\nOperação falhou.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo excedido.")
    elif excedeu_limite:
        print("Limite excedido.")
    elif excedeu_saques:
        print("Limite de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        print("Operação realizada.")
    else:
            print("Valor informado é inválido, operção falhou")

    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\nEXTRATO:")
    print(f"\nSaldo: R${saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("*Informe apenas os numeros do CPF*")
    usuario = busca_usuario(cpf,usuarios)

    if usuario:
        print("\nEsse usuário já existe.")
        return
    
    nome = input("Nome completo: ")
    dt_nascimento = input("Informe a data de nascimento (dd-mm-aaaa)")
    endereco = input("Informe seu endereço (rua - numero - bairro - municipio/estado)")

    usuarios.append({"nome":nome, "dt_nascimento":dt_nascimento, "cpf":cpf, "endereco":endereco})

    print("Usuario criado com sucesso!")
    
def busca_usuario(cpf, usuarios):
    usuarios_por_cpf = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_por_cpf[0] if usuarios_por_cpf else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("*Informe o CPF do usuário: *")
    usuario = busca_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    
    print("\n Usuario não encontrado, fluxo de criação de conta encerrado! ")

def listar_contas(contas):
    for conta in contas:
        print(f"""
            Agência: {conta['agencia']}
            Numero: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
              """)
        print("-"*50)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo,extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
