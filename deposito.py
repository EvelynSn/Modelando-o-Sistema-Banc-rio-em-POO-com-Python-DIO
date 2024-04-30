from datetime import datetime
from cliente import Cliente
from extrato import Extrato


class Deposito:
    def __init__(self, valor, cliente, data_hora=None):
        self.valor = valor
        self.cliente = cliente
        if data_hora is None:
            self.data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        else:
            self.data_hora = data_hora

    def realizar_deposito(self, extrato):
        def verificar_conta_existe(numero_conta):
            for cliente in Cliente.lista_clientes:
                if cliente.numero_conta == numero_conta:
                    return cliente
            return None

        nome_depositador = input('Digite o nome de quem está depositando: ')

        while True:
            try:
                numero_conta_destino = input("Digite o número da conta de destino: ")
                numero_conta_destino = int(numero_conta_destino)
                break
            except ValueError:
                print("Número da conta inválido. Digite um número inteiro.")

        cliente_destinatario = verificar_conta_existe(numero_conta_destino)

        while cliente_destinatario is None:
            print('Conta destinatária não encontrada. Verifique os dados informados.')
            while True:
                try:
                    numero_conta_destino = input("Digite novamente o número da conta de destino: ")
                    numero_conta_destino = int(numero_conta_destino)
                    break
                except ValueError:
                    print("Número da conta inválido. Digite um número inteiro.")
            cliente_destinatario = verificar_conta_existe(numero_conta_destino)

        print(f'Conta destinatária encontrada. Cliente associado: {cliente_destinatario.nome}')

        while True:
            try:
                valor_deposito = float(input('Digite o valor que você deseja depositar: \n'))
                if valor_deposito > 0:
                    break
                else:
                    print("Digite um valor maior que zero.")
            except ValueError:
                print("Valor inválido. Digite um valor numérico.")

        print(f'Depositando R${valor_deposito:.2f} na conta {cliente_destinatario.numero_conta} em nome de {cliente_destinatario.nome}')
        prosseguir = input('Deseja prosseguir com o depósito? [1] SIM [2] Não \n')

        if prosseguir == '1':
            print('Depósito realizado com sucesso!')
            extrato = Extrato()
            extrato.adicionar_deposito(nome_depositador, valor_deposito, self.data_hora)
            cliente_destinatario.saldo_conta += valor_deposito
            print(f"Informações do depósito: \n"
                  f"Nome do Remetente: {nome_depositador} \n"
                  f"Nome do destinatário: {cliente_destinatario.nome} \n"
                  f"Número da conta: {cliente_destinatario.numero_conta} \n"
                  f"Valor do depósito: R${valor_deposito:.2f} \n"
                  f"Data e hora do depósito: {self.data_hora} \n")
        else:
            print('Operação de depósito cancelada.')

