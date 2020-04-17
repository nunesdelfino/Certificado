import os

def CriarPasta():
    if(os.path.exists("Certificados") == 0):
        # Se não existir, cria a pasta
        os.system("mkdir Certificados")