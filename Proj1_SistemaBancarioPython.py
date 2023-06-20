menu = """
### MENU ###

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: "))
        if valor <= 0:
            print("Valor inválido, por favor digite um valor maior que zero.")
        else:
            saldo += valor
            extrato += f'Depósito no valor de R$ {valor:.2f}\n'
            print(f'Depósitono valor de R$ {valor:.2f}. Realizado  com sucesso!')
            
    elif opcao == "2":
        valor_saque = float(input("Digite o valor a ser sacado: "))
        if valor_saque <= 0:        
            print("Valor inválido, por favor digite um valor maior que zero.")
        elif valor_saque > saldo:     
            print("Saldo insuficiente.")
        elif numero_saques >= LIMITE_SAQUES:    
            print("Limite de saques diários atingido.")
        else:   
            saldo -= valor_saque
            extrato += f'Saque no valor de R$ {valor_saque:.2f}\n'
            numero_saques += 1
            print(f'Saque no valor de R$ {valor_saque:.2f}. Realizado com sucesso!')
        
    elif opcao == "3":
        print('========== EXTRATO ==========')
        if extrato == "":
            print("Nenhuma operação realizada.\n")
        else:
            print(extrato)
            
        print(f'Saldo atual: R$ {saldo:.2f}')
        print(f'Limite disponível: R$ {limite - saldo:.2f}')
        print(29 * "=")
        
    elif opcao == "4":
        print("Obrigado por utilizar o sistema!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        