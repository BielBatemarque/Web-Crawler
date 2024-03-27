from models.resposta import Resposta
from abc import ABC, abstractclassmethod
from .Loja import Loja
import requests

class Buscador():

    def __init__(self, loja:Loja) -> None:
        self.loja = loja
        self.session = requests.Session()
        self.requisicao = None
        self.resposta = None

    
    def abrir_requisisao(self, link, method="GET", headers=None, data=None, json=None):
        self.requisicao = requests.Request(
            method=method,
            url=link,
            data=data,
            json=json
        )

    def enviar(self, permitir_redirecionamentos=True, stream_de_dados=False, **Kwargs):
        request_final = self.session.prepare_request(self.requisicao)

        self.resposta = self.session.send(
            request_final,
            allow_redirects=permitir_redirecionamentos,
            stream=stream_de_dados,
            verify=False,
            **Kwargs
        )

    @abstractclassmethod
    def buscar() -> Resposta:
        pass