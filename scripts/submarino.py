from models.Loja import Loja
class Submarino(Loja):
    NOME_LOJA = "Submarino"
    
    def __init__(self, nome, url) -> None:
        super().__init__(nome, url)
