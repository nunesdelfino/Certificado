from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.lib.units import mm, inch

# Caminho para a imagem de fundo
logo = ImageReader('Certificado.png')

# Tamanho da página
size_page = (297*mm, 210*mm)

# Tamanho Fonte Nome
size_name = 140

# Nome local
name_x = size_page[1]/2
name_y = 1380

# Fonte
font = "Helvetica-Bold"

def GeneratePDF(lista):
    try:
        for indice, nome in enumerate(lista):
            # Gerar certificado
            pdf = canvas.Canvas('{}.pdf'.format(nome))
            # Tamanho da página do certificado
            pdf.setPageSize(size_page)
            # Imagem de fundo
            pdf.drawImage(logo, 0, 0)
            pdf.setFont(font, size_name)
            pdf.drawCentredString(name_x, name_y, nome)
            pdf.save()
            print('{}.pdf criado com sucesso!'.format(nome))
    except:
        print('Erro ao gerar pdf')

lista = ["Gabriel Nunes Delfino"]

GeneratePDF(lista)