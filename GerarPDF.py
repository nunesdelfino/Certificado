from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import mm, inch
import csv
import os
import os.path


# # Importar CSV
arquivo = open('Certificados.csv')

# # Le como dicionário
dados = csv.reader(arquivo)

# Configurações da página
# Fundo
logo = ImageReader('CertificadoDias.png')

# Tamanho da página
size_page = (297*mm, 210*mm)


# Tamanhos das Fontes
# Tamanho Fonte Nome
size_name = 30

# Tamanho fonte horas
size_horas = 17

# Tamanho fonte data
size_data = 10

# Tamaho fonte evento
size_evento = 25


# Localização X Y
# Nome local
name_y = 330
name_x = 420

# Horas Local
horas_y = 175
horas_x = 447

# Data Local
data_y = 203
data_x = 420

# Evento Local
evento_y = 260
evento_x = 420

# Fontes
font = "Helvetica-Bold"
font_data = "Helvetica"





def GeneratePDF(lista):
    try:
        for linhas in dados:

            # Gerar certificado
            pdf = canvas.Canvas('{}-{}.pdf'.format(linhas[0],linhas[2]))

            # Tamanho da página do certificado
            pdf.setPageSize(size_page)

            # Imagem de fundo
            pdf.drawImage(logo, 0, 0, 297*mm, 210*mm)

            # NOME
            # Fonte e Tamanho do texto
            pdf.setFont(font, size_name)
            # Escreve o texto
            pdf.drawCentredString(name_x, name_y, linhas[0])


            # HORAS
            # Fonte e Tamanho do texto
            pdf.setFont(font, size_horas)
            # Escreve o texto
            pdf.drawCentredString(horas_x, horas_y, linhas[2])

            # DATA
            # Fonte e tamamho do texto
            pdf.setFont(font_data, size_horas)
            # Escreve o texto
            pdf.drawCentredString(data_x, data_y, linhas[3])


            # EVENTO
            # Fonte e tamamho do texto
            pdf.setFont(font, size_evento)
            # Escreve o texto
            pdf.drawCentredString(evento_x, evento_y, linhas[1])

            # Salva o PDF
            pdf.save()

            # Retorna mensagem de sucesso
            print('{}-{}.pdf criado com sucesso!'.format(linhas[0],linhas[2]))
    except:
        print('Erro ao gerar pdf')


def CopiarCertificados():
    if(os.path.exists("Certificados") == 0):
        os.system("mkdir Certificados")

    os.system("mv *.pdf Certificados")


GeneratePDF(dados)

CopiarCertificados()