from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, nome_cliente, numero_conta, pin_acesso):
        self.nome_cliente = nome_cliente
        self.numero_conta = numero_conta
        self.pin_acesso = pin_acesso
        self.saldo = 0.0
        self.movimentos = []

    def depositar(self, valor):
        self.saldo += valor
        self.__registra(f"Depósito: +{valor}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.__registra(f"Saque: -{valor}")
        else:
            print("Saldo insuficiente.")

    def __registra(self, movimento):
        self.movimentos.append(movimento)

    @abstractmethod
    def extrato(self):
        pass

class ContaPF(Conta):
    def __init__(self, nome_cliente, numero_conta, pin_acesso, cpf):
        super().__init__(nome_cliente, numero_conta, pin_acesso)
        self.cpf = cpf

    def extrato(self):
        print(f"Extrato da Conta PF - CPF: {self.cpf}")
        for movimento in self.movimentos:
            print(movimento)
        print(f"Saldo atual: {self.saldo}")

class ContaPJ(Conta):
    def __init__(self, nome_cliente, numero_conta, pin_acesso, cnpj):
        super().__init__(nome_cliente, numero_conta, pin_acesso)
        self.cnpj = cnpj

    def extrato(self):
        print(f"Extrato da Conta PJ - CNPJ: {self.cnpj}")
        for movimento in self.movimentos:
            print(movimento)
        print(f"Saldo atual: {self.saldo}")

# Exemplo de uso
conta_pf = ContaPF("João Silva", "12345", "1234", "123.456.789-00")
conta_pf.depositar(1000)
conta_pf.sacar(200)
conta_pf.extrato()

conta_pj = ContaPJ("Empresa XYZ", "67890", "5678", "12.345.678/0001-00")
conta_pj.depositar(5000)
conta_pj.sacar(1500)
conta_pj.extrato()
