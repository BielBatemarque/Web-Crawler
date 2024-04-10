from utils.logger import Logger
from utils.config import Config
from todos_scripts import TodosScripts

class Robo:

    def __init__(self) -> None:
        pass

    def chama_nome_robo(nome: str):
        Logger.debug(nome)

    site = Config.retorna_preferenciais_de_busca()["marketplace"]
    print(site)

    todos_scripts = TodosScripts.scripts
    print(todos_scripts)

    for loja in todos_scripts:
        print(loja)


    

if __name__ == "__main__":
    Robo.chama_nome_robo("vm-01")
    
