from .produtos import Produto
class Resposta():

    def __init__(self, valor: float, produto: Produto) -> None:
        self.valor = valor
        self.produto = produto
