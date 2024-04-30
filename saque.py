from datetime import datetime
from cliente import Cliente



class Saque:
    def __init__(self, valor, cliente):
        self.valor = valor
        self.cliente = cliente
        self.data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def verificar_cliente(self, numero_conta, senha_conta):
        for cliente in Cliente.lista_clientes:
            if cliente.numero_conta == numero_conta and cliente.senha_conta == senha_conta:
                return cliente
        return None

    def verificar_saldo_suficiente(self, valor_saque):
        if self.cliente and hasattr(self.cliente, 'saldo_conta') and self.cliente.saldo_conta >= valor_saque:
            return True
        else:
            return False

    def realizar_saque(self):
        while True:
            numero_conta_cliente = input("Digite o número da conta: \n")
            numero_conta_cliente = int(numero_conta_cliente)
            senha_cliente = input("Digite a senha de 4 dígitos: \n")
            senha_cliente = int(senha_cliente)
        
            cliente_autenticado = self.verificar_cliente(numero_conta_cliente, senha_cliente)

            if cliente_autenticado:
                self.cliente = cliente_autenticado 
                print("Cliente autenticado com sucesso! \n")
                valor_saque = float(input('Digite o valor que você deseja sacar: \n'))
                
                if self.verificar_saldo_suficiente(valor_saque):
                    self.cliente.saldo_conta -= valor_saque
                    self.extrato.adicionar_saque("saque:", valor_saque, self.data_hora)
                    print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
                    print(f"Data e hora do saque: {self.data_hora} \n")
                    print(f"Seu novo saldo é: R${self.cliente.saldo_conta:.2f}")
                else:
                    print("Saldo insuficiente para realizar o saque. Tente um valor menor.")
                    continue

                if input(f"Confirmar saque de R${valor_saque:.2f}? [S/N]: ").upper() == "S" or "s":
                    break
                else:
                    print("Operação de saque cancelada.")
            else:
                print("Número da conta ou senha incorretos. Verifique os dados informados e tente novamente.")
                continue
