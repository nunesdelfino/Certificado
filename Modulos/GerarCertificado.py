# Importações
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import mm, inch
from Modulos.GerarNome import NomeCertificado
from Modulos.TratarDados import TratarHoras, TratarTexto

# Configurações da página
# Imagens
try:
    fundo = ImageReader('CertificadoFundo.png') # Fundo do certificado
except OSError:
    print("A imagem de fundo para o certificado não pode ser aberta")
    exit()

try:
    qr_code = ImageReader('qrcode.png') # QR Code
except OSError:
    print("A imagem do qr code para o certificado não pode ser aberta")
    exit()

try:
    logo_emissor = ImageReader('LogoEmissor.png') # Logo Emissor
except OSError:
    print("A imagem de logo do emissor para o certificado não pode ser aberta")
    exit()


size_page = (297*mm, 210*mm) # Tamanho da página

# Tamanhos das Fontes
size_name = 30 # Tamanho Fonte Nome
size_horas = 17 # Tamanho fonte horas
size_data = 10 # Tamanho fonte data
size_evento = 25 # Tamaho fonte evento
size_assinante = 18 # Tamanho fonte Assinante

# Posicação X Y
name_y = 330 # Nome Y
name_x = 420 # Nome x
horas_y = 175 # Horas Y
horas_x = 447 # Horas X
data_y = 200 # Data Y
data_x = 420 # Data X
evento_y = 260 # Evento Y
evento_x = 420 # Evento X
assinante_y = 90 # Assinante Y
assinante_x = 420 # Assinante X
qrcode_y = 70 # QR Code y
qrcode_x = 666 # QR Code X
logo_emissor_x = 190 # Logo Emissor X
logo_emissor_y = 390 # Logo Emissor Y

largura_altura = 37*mm # Tamanho Qr Code
logo_emissor_altura = 45*mm # Altura Logo Emissor
logo_emissor_largura = 160*mm # Largura Logo Emissor

# Fontes
fonte_nome = "Helvetica-Bold" # Nome
font_data = "Helvetica" # Data
fonte_horas = "Helvetica-Bold" # Horas
fonte_evento = "Helvetica-Bold" # Evento
fonte_assinante = "Helvetica-Bold" # Assinante

def Gerar(dados, Assinante): # Função que gera os certificados
    for linha in dados: # Loop para acessar os dados
        Nome = NomeCertificado(linha) # Gera o nome para o Certificado
        try:
            pdf = canvas.Canvas('{}.pdf'.format(Nome)) # Gerar certificado
            pdf.setPageSize(size_page) # Tamanho da página do certificado
            pdf.drawImage(fundo, 0, 0, 297*mm, 210*mm) # Imagem de fundo

            # NOME
            pdf.setFont(fonte_nome, size_name) # Fonte e Tamanho do nome
            linha[0] = TratarTexto(linha[0]) # Deixa o nome capitalizado
            pdf.drawCentredString(name_x, name_y, linha[0]) # Escreve o nome

            # HORAS
            pdf.setFont(fonte_horas, size_horas) # Fonte e Tamanho do horas
            linha[2] = TratarHoras(linha[2]) # Deixa a hora sempre com dois números
            pdf.drawCentredString(horas_x, horas_y, linha[2]) # Escreve o horas

            # DATA
            pdf.setFont(font_data, size_horas) # Fonte e tamamho do data
            pdf.drawCentredString(data_x, data_y, linha[3]) # Escreve o data

            # EVENTO
            pdf.setFont(fonte_evento, size_evento) # Fonte e tamamho do evento
            linha[1] = TratarTexto(linha[1]) # Deixa o evento capitalizado
            pdf.drawCentredString(evento_x, evento_y, linha[1]) # Escreve o evento

            # ASSINANTE
            pdf.setFont(fonte_assinante, size_assinante) # Fonte e tamamho do assinante
            pdf.drawCentredString(assinante_x, assinante_y, Assinante) # Escreve o assinante

            # QR CODE
            pdf.drawImage(qr_code, qrcode_x, qrcode_y, largura_altura, largura_altura) # Posiciona o QR Code

            # LOGO EMISSOR
            pdf.drawImage(logo_emissor, logo_emissor_x, logo_emissor_y, logo_emissor_largura, logo_emissor_altura)

            pdf.save() # Salva o PDF

            print('{}.pdf criado com sucesso!'.format(Nome)) # Retorna mensagem de sucesso
        except:
            print("Erro ao gerar o pdf: ", Nome)