from BancoNapp.contas.Conta import Conta


class ContaPoupanca(Conta):
   def __init__(self, *args, **kwargs):
      kwargs.update({
         'limite': kwargs.get('limite', 0),
         'saldo': kwargs.get('saldo', 0),
      })
      super().__init__(*args, **kwargs)
      self.profissao = kwargs.get('profissao', '')

   def deposito(self, valor):
      if not isinstance(valor, (int, float)):
         raise TypeError('O depósito precisa ser numérico')

      if valor <= 0:
         raise ValueError('Valor do depósito precisa ser maior que zero')

      self.extrato.append(('D', valor))
      self.saldo += valor

   def saque(self, valor):
      if not isinstance(valor, (int, float)):
         raise TypeError('O valor do saque precisa ser numérico')
      if self.saldo < valor:
         raise ValueError('Valor do saque supera seu saldo.')
   
      self.saldo -= valor
      self.extrato.append(('S', valor))
      return valor

   def get_extrato(self):
      return self.extrato

   def rendimento_aniversario(self, juros):
      if juros < 0 or juros > 1:
         raise ValueError('Os juros precisam ser entre 0 (0%) e 1 (100%).')

      self.saldo *= 1 + juros
