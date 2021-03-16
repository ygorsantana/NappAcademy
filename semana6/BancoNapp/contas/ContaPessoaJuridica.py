from BancoNapp.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.limite = kwargs.get('limite', 1500)
        self.empresa = kwargs.get('empresa', None)
