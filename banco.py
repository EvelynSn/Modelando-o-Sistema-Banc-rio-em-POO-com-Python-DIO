from cliente import Cliente
from deposito import Deposito
from saque import Saque
from extrato import Extrato 

while True:
    print("Menu:")
    print("1. Cadastrar Cliente")
    print("2. Mostrar Clientes")
    print("3. Editar Cliente")
    print("4. Remover Cliente")
    print("5. Depósito")
    print("6. Saque")
    print("7. Extrato")
    print("8. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        Cliente.cadastrar_cliente()
    elif opcao == "2":
        Cliente.mostrar_clientes()
    elif opcao == "3":
        cpf_cliente = input("Digite o CPF do cliente que você deseja editar: \n")
        Cliente.editar_cliente(cpf_cliente)
    elif opcao == "4":
        cpf_cliente_remover = input("Digite o CPF do cliente que você deseja remover: \n")
        codigo_gerencia = int(input("Digite o código correspondente para remover o cliente: "))
        Cliente.remover_cliente(cpf_cliente_remover, codigo_gerencia)
    elif opcao == "5":
        extrato = Extrato()
        valor_deposito = float(input("Digite o valor que você deseja depositar: \n"))
        cliente = input("Digite o número da conta do cliente de destino do depósito: \n")
        deposito = Deposito(valor_deposito, cliente)
        deposito.realizar_deposito(extrato)
    elif opcao == "6":
        valor_saque = float(input("Digite o valor que você deseja sacar: \n"))
        cliente = input("Digite o número da conta do cliente: \n")
        saque = Saque(valor_saque, cliente)
        saque.realizar_saque()
    elif opcao == "7":
        numero_conta = input("Digite o número da conta do cliente para ver o extrato: \n")
        extrato = Extrato()
        extrato.mostrar_extrato_por_numero_conta(numero_conta)
    elif opcao == "8":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")



