
menu = """
Bem-vindo ao TeckBank
Escolha uma opção:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input('Digite o valor que deseja depositar: '))
            if valor <= 0:
                print('Valor invalido')
            else:
                saldo += valor
                extrato += f'Deposito: R${valor}\n'
                print(f'R${valor} depositado com sucesso')
        except ValueError:
            print('Erro, valor invalido')
            
    elif opcao == "s":
        try:
            if numero_saques >= LIMITE_SAQUES:
                print('Você atingiu o limite de saques diários')
            else:
                valor = float(input('Digite o valor que deseja sacar: '))
                if valor <= 0:
                    print('Não pode sacar valores negativos')
                elif valor > saldo:
                    print(f'Saldo insuficiente\nSaldo: R${saldo}')
                elif valor > limite:
                    print('O limite de saque é R$500,00')
                else:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f'Saque: R${-valor}\n'
                    print(f'Saque de R${valor} efetuado com sucesso')
        except ValueError:
            print('Erro, valor inválido')

    elif opcao == "e":
       ext = 'EXTRATO'
       final = '='
       print(ext.center(20, '='))
       print(f'{extrato}\n'f'Saldo: R${saldo:.2f}')
       print(final.center(20, '='))
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")