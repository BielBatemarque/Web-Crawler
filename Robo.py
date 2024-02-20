from utils.logger import Logger
from utils.config import Config


class Robo():

    def __init__(self) -> None:
        pass

    def chama_nome_robo(nome: str):
        Logger.debug(nome)


    site = Config.retorna_preferenciais_de_busca()["marketplace"]
    print(site)
    

if __name__ == "__main__":
    Robo.chama_nome_robo("vm-01")
    
