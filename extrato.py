from cliente import Cliente

class Extrato:
    def __init__(self):
        self.saques_extrato = []
        self.depositos_extrato = []
        
    def encontrar_cliente_por_numero(self, numero_conta):
        for cliente in Cliente.lista_clientes:
            numero_conta = int(numero_conta)
            if cliente.numero_conta == numero_conta:
                return cliente
        return None

    def adicionar_saque(self, valor_saque, data_hora):
        self.saques_extrato.append({"valor": valor_saque, "data_hora": data_hora})

    def adicionar_deposito(self, valor_deposito, nome_depositador, data_hora):
        from deposito import Deposito 
        deposito = Deposito(valor_deposito, nome_depositador, data_hora)
        self.depositos_extrato.append(deposito)
        self.depositos_extrato.append({"Nome de quem depositou": nome_depositador, "valor": valor_deposito, "data_hora": data_hora})
        
    
    def exibir_extrato_cliente(self, cliente):
        print(f"Extrato para o cliente: {cliente.nome} - Conta: {cliente.numero_conta}\n")
        print("Saques:")
        for saque in self.saques_extrato:
            print(f"\tData: {saque['data_hora']} - Valor: R${saque['valor']:.2f}")
        print("\nDepósitos:")
        for deposito in self.depositos_extrato:
            print(f"\tData: {deposito['data_hora']} - Valor: R${deposito['valor']:.2f}")
        print("\nSaldo atual: R$ {:.2f}".format(cliente.saldo))



    def mostrar_extrato_por_numero_conta(self, numero_conta):
        cliente = self.encontrar_cliente_por_numero(numero_conta)
        if cliente:
            self.exibir_extrato_cliente(cliente)
        else:
            print("Cliente não encontrado.")
