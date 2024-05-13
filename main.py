menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input()

    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
        else:
            print("Informe um valor válido.")
            
    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))
        if valor > saldo or valor > limite or numero_saques > LIMITE_SAQUES:
            print("Informe um valor válido.")
        else:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque de R$ {valor:.2f}, saldo na conta de R$ {saldo:.2f}\n"
            
    elif opcao == "e":
        print(extrato)
    elif opcao == "q":
        print("Obrigado e até a próxima!\n")
        break
    