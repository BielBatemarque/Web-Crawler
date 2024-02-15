from datetime import datetime

class Cor():
    VERMELHO = '\033[91m'
    VERDE    = '\033[92m'
    AZUL     = '\033[94m'
    CIANO    = '\033[96m'
    BRANCO   = '\033[97m'
    AMARELO  = '\033[93m'
    MAGENTA  = '\033[95m'
    CINZA    = '\033[90m'
    PRETO    = '\033[90m'
    PADRAO   = '\033[0m'

class Logger():
    def salva_mensagem_no_txt(mensagem: str):
        # with open("log.txt", "a", encoding="utf-8") as file:
        #     file.write(mensagem + "\n")

        pass

    def salva_error_no_txt(mensagem: str):
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(str(mensagem) + "\n")

    def retorna_horario_formatado():
        now = datetime.now()
        horario_formatado = now.strftime("%d/%m %H:%M:%S")

        return horario_formatado

    def retorna_mensagem_crua(prefixo, texto):
        """Retorna a mensagem sem nenhum tipo de cor ou decoração"""
        mensagem = f"[{Logger.retorna_horario_formatado()}] {prefixo} - {texto}"
        Logger.salva_mensagem_no_txt(mensagem)

        return mensagem

    def mensagem(prefixo, texto, cor:Cor):
        texto = Logger.retorna_mensagem_crua(prefixo, texto)
        print(cor+texto+Cor.PADRAO)

        # Por algum motivo estava salvando duas vezes no txt
        # Logger.salva_mensagem_no_txt(texto)

    def debug(texto):
        Logger.mensagem("DEBUG", texto, Cor.AZUL)

    def erro(texto, prefixo = "ERRO"):
        Logger.mensagem("ERRO", texto, Cor.VERMELHO)
    
    def alerta(texto):
        Logger.mensagem("ALERTA", texto, Cor.AMARELO)

    def sucesso(texto):
        Logger.mensagem("SUCESSO", texto, Cor.VERDE)

    def linha_em_branco():
        print("")