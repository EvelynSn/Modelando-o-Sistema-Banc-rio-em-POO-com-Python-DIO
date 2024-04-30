import random

class Cliente:
    lista_clientes = []
    lista_numeros_conta = [] 
    lista_senhas_cliente = []

    def __init__(self, nome, cpf, endereco, telefone, numero_conta, saldo_conta, senha_conta):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.numero_conta = numero_conta
        self.saldo_conta = saldo_conta 
        self.senha_conta = senha_conta

    @classmethod
    def cadastrar_cliente(cls):
        
        saldo_conta = 0
        nome = input('Digite o nome do cliente: \n')
        while not nome.strip() or ' ' not in nome.strip():
            print('Nome inválido. O nome não pode ser vazio e deve conter ao menos um espaço entre os nomes.')
            nome = input('Digite o nome do cliente: \n')

        cpf = input('Digite o CPF do cliente: \n')
        while len(cpf.strip()) != 11 or not cpf.strip().isdigit():
            print('CPF inválido. O CPF deve conter 11 dígitos numéricos.')
            cpf = input('Digite o CPF do cliente: \n')

        cpf_formatado = cls.formatar_cpf(cpf)  

        endereco = input('Digite o endereço do cliente (Formato: Rua, número, bairro, complemento(opcional)): \n')
        while not endereco.strip():
            print('Endereço inválido. O endereço não pode ser vazio.')
            endereco = input('Digite o endereço do cliente: \n')

        telefone = input('Digite o telefone do cliente (no formato 9XXXX-XXXX): \n')
        while not telefone.strip() or not telefone.strip().replace('-', '').isdigit() or len(telefone.strip()) !=10:
            print('Telefone inválido. O telefone deve estar no formato 9XXXX-XXXX e não pode ser vazio.')
            telefone = input('Digite o telefone do cliente (no formato 9XXXX-XXXX): \n')

        numero_conta = cls.gerar_numero_conta()
        senha_conta = cls.gerar_senha_conta()
        cliente = Cliente(nome, cpf_formatado, endereco, telefone, numero_conta, saldo_conta, senha_conta)
        cls.lista_clientes.append(cliente)

    @staticmethod
    def formatar_cpf(cpf):
        cpf_numerico = ''.join(filter(str.isdigit, cpf))
        cpf_formatado = f'{cpf_numerico[:3]}.{cpf_numerico[3:6]}.{cpf_numerico[6:9]}-{cpf_numerico[9:]}'
        return cpf_formatado

    @classmethod
    def gerar_numero_conta(cls):
        while True:
            numero_conta = random.randint(1000, 9999) 
            if numero_conta not in cls.lista_numeros_conta:
                cls.lista_numeros_conta.append(numero_conta)
                return numero_conta
    
    @classmethod
    def gerar_senha_conta(cls):
        while True:
            senha_conta = random.randint (2300, 9999)
            if senha_conta not in cls.lista_senhas_cliente:
                cls.lista_senhas_cliente.append(senha_conta)
                return senha_conta
    
    @classmethod
    def editar_cliente(cls, cpf):
        cpf_formatado = cls.formatar_cpf(cpf) 

        for cliente in cls.lista_clientes:
            if cliente.cpf == cpf_formatado:
                novo_nome = input("Digite o novo nome: \n")
                novo_endereco = input("Digite o novo endereço: (Formato: Rua, número, bairro, complemento(opcional)) \n")
                
                while True:
                    novo_telefone = input("Digite o novo telefone no formato 9XXXX-XXXX: \n")
                    if novo_telefone.strip() and novo_telefone.strip().replace('-', '').isdigit() and len(novo_telefone.strip()) == 10:
                        break
                    print('Telefone inválido. O telefone deve estar no formato 9XXXX-XXXX e não pode ser vazio.')

                cliente.nome = novo_nome
                cliente.endereco = novo_endereco
                cliente.telefone = novo_telefone
                print(f"Dados do cliente portador do CPF {cpf_formatado} foram atualizados com sucesso.")
                print("Novos dados:")
                print('-' * 20)
                print(f"Nome: {cliente.nome}")
                print(f"Telefone: {cliente.telefone}")
                print(f"Endereço: {cliente.endereco}")
                print('-' * 20)
                return
        print(f"Erro ao editar os dados do cliente. CPF {cpf_formatado} não encontrado.")
            
    @classmethod
    def remover_cliente(cls, cpf, codigo_gerencia):
        cpf_formatado = cls.formatar_cpf(cpf) 
        
        for cliente in cls.lista_clientes:
            if cliente.cpf == cpf_formatado and codigo_gerencia == 7766:
                cls.lista_clientes.remove(cliente)
                print(f"Cliente com CPF {cpf_formatado} foi removido com sucesso.")
                return
        print("Erro ao remover cliente.")
        
    

            
    @classmethod
    def mostrar_clientes(cls):
        for cliente in cls.lista_clientes:
            print('-' * 20)
            print(f'Nome: {cliente.nome}')
            print(f'CPF: {cliente.cpf}')
            print(f'Endereço: {cliente.endereco}')
            print(f'Telefone: {cliente.telefone}')
            print(f'Número da Conta: {cliente.numero_conta}')
            print(f"Senha: {cliente.senha_conta}")
            print(f"Saldo: {cliente.saldo_conta}")
            print('-' * 20)




