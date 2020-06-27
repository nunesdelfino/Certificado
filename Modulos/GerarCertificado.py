# Importações
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import mm, inch
import shutil
from pathlib import Path

class GerarCertificado:

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

    # Configurações da página
    # Imagens
    def ImportarFundo(self, CaminhoFundo):
        try:
            FundoCertificado = ImageReader(CaminhoFundo) # Fundo do certificado
            return FundoCertificado
        except OSError:
            print("A imagem de fundo para o certificado não pode ser aberta")
            exit()

    def ImportarQRCode(self):
        try:
            qr_code = ImageReader('qrcode.png') # QR Code
            return qr_code
        except OSError:
            print("A imagem do qr code para o certificado não pode ser aberta")
            exit()

    def ImportarLogo(self, CaminhoLogo):
        try:
            LogoEmissor = ImageReader(CaminhoLogo) # Logo Emissor
            return LogoEmissor
        except OSError:
            print("A imagem de logo do emissor para o certificado não pode ser aberta")
            exit()


    def NomeCertificado(self, linha): # Recebe um linha de dados
        Aluno = linha[0] # Copia o conteúdo posição 0 para a variável Aluno
        Evento = linha[1] # Copia o conteúdo posição 1 para a variável Evento
        NomeAluno = Aluno.split(' ') # Separa a string do nome aluno onde tem espaço
        NomeAluno = NomeAluno[0] + NomeAluno[-1] # Cria uma string unindo primeiro e ultimo nome do aluno
        NomeEvento = Evento.split(' ') # Separa a string do nome evento onde tem espaço
        if len(NomeEvento) > 1: # Verifica se o evento tem mais de uma palavra como nome
            NomeEvento = NomeEvento[0] + NomeEvento[-1] # Se tiver, gera uma string com primeiro e ultimo nome do evento
        else:
            NomeEvento = str(NomeEvento[0]) # Se não, Gera uma string com o nome do evento
        NomeCertificado = NomeAluno + "_" + NomeEvento # Gera o nome do certificado unindo a string NomeAluno e NomeEvento
        return NomeCertificado # Retorna o nome do certificado

    # Funçao para tratar uma string e deixa-lá capitalziada em casa item
    def TratarTexto(self, Texto): # Recebe uma string como entrada
        Texto = Texto.split(' ') # Separa a string por espaço, gerando uma lista
        for Indice, Nome in enumerate(Texto): # Acessa cada item da lista
            Texto[Indice] = Nome.capitalize() # Capitaliza cada item da lista
        Texto = " ".join(Texto) # Tansforma a lista em string novamente
        return Texto # Retorna a string

    # Função para tratar a hora e deixa-la com dois algarismos sempre
    def TratarHoras(self, Hora): # Recebe a hora
        if (len(Hora) == 1): # Converte em inteiro e verifica se é menor de 10
            return "0"+Hora # Se for retorna uma string começada com 0 + a hora recebida
        elif (len(Hora) > 3):
            print("Verifique a coluna de horas e garanta que tenha no máximo três algarismos")
            print("Erro no valor: ", Hora)
        else:
            return Hora # Se não for, retorna a hora recebida

    def Gerar(self, Dados, CaminhoFundo, CaminhoLogo, Assinante, CaminhoSalvar): # Função que gera os certificados
        for Linha in Dados: # Loop para acessar os dados
            Nome = self.NomeCertificado(Linha) # Gera o nome para o Certificado
            try:
                pdf = canvas.Canvas('{}.pdf'.format(Nome)) # Gerar certificado
                pdf.setPageSize(self.size_page) # Tamanho da página do certificado
                pdf.drawImage(self.ImportarFundo(CaminhoFundo), 0, 0, 297*mm, 210*mm) # Imagem de fundo

                # NOME
                pdf.setFont(self.fonte_nome, self.size_name) # Fonte e Tamanho do nome
                Linha[0] = self.TratarTexto(Linha[0]) # Deixa o nome capitalizado
                pdf.drawCentredString(self.name_x, self.name_y, Linha[0]) # Escreve o nome

                # HORAS
                pdf.setFont(self.fonte_horas, self.size_horas) # Fonte e Tamanho do horas
                Linha[2] = self.TratarHoras(Linha[2]) # Deixa a hora sempre com dois números
                pdf.drawCentredString(self.horas_x, self.horas_y, Linha[2]) # Escreve o horas

                # DATA
                pdf.setFont(self.font_data, self.size_horas) # Fonte e tamamho do data
                pdf.drawCentredString(self.data_x, self.data_y, Linha[3]) # Escreve o data

                # EVENTO
                pdf.setFont(self.fonte_evento, self.size_evento) # Fonte e tamamho do evento
                Linha[1] = self.TratarTexto(Linha[1]) # Deixa o evento capitalizado
                pdf.drawCentredString(self.evento_x, self.evento_y, Linha[1]) # Escreve o evento

                # ASSINANTE
                pdf.setFont(self.fonte_assinante, self.size_assinante) # Fonte e tamamho do assinante
                pdf.drawCentredString(self.assinante_x, self.assinante_y, Assinante) # Escreve o assinante

                # QR CODE
                pdf.drawImage(self.ImportarQRCode(), self.qrcode_x, self.qrcode_y, self.largura_altura, self.largura_altura) # Posiciona o QR Code

                # LOGO EMISSOR
                pdf.drawImage(self.ImportarLogo(CaminhoLogo), self.logo_emissor_x, self.logo_emissor_y, self.logo_emissor_largura, self.logo_emissor_altura)

                pdf.save() # Salva o PDF
                print('{}.pdf criado com sucesso!'.format(Nome)) # Retorna mensagem de sucesso

                print(f'{Path().absolute()}/*.pdf')
                print(CaminhoSalvar)

                shutil.move(f'{Path().absolute()}/{Nome}.pdf', CaminhoSalvar)

            except:
                print("Erro ao gerar o pdf: ", Nome)