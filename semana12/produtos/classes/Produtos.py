from abc import ABC, abstractmethod
from produtos.classes.Caracteristicas import Caracteristicas


class Produto(ABC):
    def __init__(self, implementation):
        if not isinstance(implementation, Caracteristicas):
            raise TypeError(
                'Class need to be instantiated with a Caracteristicas arg type'
            )

        self.implementation = implementation

    @abstractmethod
    def operation(self):
        pass


class CocaCola(Produto):
    def operation(self):
        return (f"CocaCola tamanho:"
                f"{self.implementation.operation_implementation()}")


class Pepsi(Produto):
    def operation(self):
        return (f"Pepsi tamanho:"
                f"{self.implementation.operation_implementation()}")


class Dolly(Produto):
    def operation(self):
        return (f"Dolly tamanho:"
                f"{self.implementation.operation_implementation()}")


class GuaranaAntartica(Produto):
    def operation(self):
        return (f"Guarana Antartica tamanho:"
                f"{self.implementation.operation_implementation()}")
