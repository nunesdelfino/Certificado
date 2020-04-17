# IMPORTAÇÕES
import pyqrcode

def GerarQR(): # Função para gerar o Qr Code para o certificado
    try:
        while True: # Iniciar o loop de verificação
            # Recebe do usuário onde a validação poderá ser realizada
            Verificador = str(input("Informe o local onde o certificado pode ser validado: "))
            if Verificador != "": # Verifica se o usuário deixou vazio
                break # Para o loop
            else:
                print("O local de validação não pode estar vazio!")
        qr_code = pyqrcode.create(Verificador, error='L', version=5, mode='binary') # Gera o Qr Code
        # Salva o Qr Code em png com o nome 'qrcode.png'
        qr_code.png('qrcode.png', scale=1, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    except KeyboardInterrupt:
        print("Execução do código interrompida pelo usuário")
        exit()
    except:
        print("Erro ao gerar Qr Code")
        exit()