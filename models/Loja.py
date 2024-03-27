from abc import ABC, abstractclassmethod
from models.resposta import Resposta
class Loja(ABC):
    NOME_LOJA = str


    def __init__(self, nome, url) -> None:
        self.nome = nome
        self.url = url
        self.resultado: Resposta = Resposta()
