# IMPORTAÇÕES
import pyqrcode

def GerarQR(Caminho): # Função para gerar o Qr Code para o certificado
    try:
        qr_code = pyqrcode.create(Caminho, error='L', version=5, mode='binary') # Gera o Qr Code
        # Salva o Qr Code em png com o nome 'qrcode.png'
        qr_code.png('qrcode.png', scale=1, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    except KeyboardInterrupt:
        print("Execução do código interrompida pelo usuário")
        exit()
    except:
        print("Erro ao gerar Qr Code")
        exit()