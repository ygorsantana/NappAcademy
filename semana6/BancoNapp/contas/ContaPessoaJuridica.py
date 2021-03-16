from BancoNapp.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    def __init__(self, *args, **kwargs):
        kwargs.update({
            'limite': kwargs.get('limite', 1500),
        })
        super().__init__(*args, **kwargs)
        self.empresa = kwargs.get('empresa', None)

    def deposito(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError('O depósito precisa ser numérico')
        if valor <= 0:
            raise ValueError('Valor do depósito precisa ser maior que zero')
        self.saldo += valor
        self.extrato.append(('D', valor))

    def saque(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError('O valor do saque precisa ser numérico')
        if self.limite < valor:
            raise ValueError('Valor do saque supera seu saldo e seu limite')

        if self.saldo < valor:
            self.limite -= valor - self.saldo

        self.saldo -= valor
        self.extrato.append(('S', valor))
        return valor
    
    def get_extrato(self):
        return self.extrato
