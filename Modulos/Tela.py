import PySimpleGUI as sg

class TelaInicial:

    NomeTela = "Gerar Certificados"
    TamTexto = 29
    TamBotArq = 10
    TamCamEntrada = 30
    TamCamArq = 30

    Valor = []

    sg.theme('DarkGrey5')

    def __init__(self):
        # Cria o Layout
        layout = [
            # Caminho do CSV
            [sg.Text('Selecione o arquivo CSV:', size=(self.TamTexto,1)),
                sg.In (size=(self.TamCamArq, 1), key='ArquivoCSV'),
                sg.FileBrowse (file_types = (('Arquivos de CSV', '*.csv'),), size=(self.TamBotArq, 1), button_text='Procurar CSV')],

            # Caminho do Fundo
            [sg.Text('Selecionar o Fundo do Certificado:', size=(self.TamTexto,1)),
                sg.In(size=(self.TamCamArq, 1), key='ArquivoFundo'),
                sg.FileBrowse (file_types = (('Arquivo PNG', '*.png'),), size=(self.TamBotArq, 1), button_text='Procurar Fundo')],

            # Caminho do Logo
            [sg.Text('Selecionar o Logo do Emissor:', size=(self.TamTexto,1)),
                sg.In(size=(self.TamCamArq, 1), key="ArquivoLogo"),
                sg.FileBrowse (file_types = (('Arquivo PNG', '*.png'),), size=(self.TamBotArq, 1), button_text='Procurar Logo'), ],

            # Assinante
            [sg.Text('Nome do Assinante:', size=(self.TamTexto,1)),
                sg.Input(size=(self.TamCamEntrada, 1), key='NomeAssiante')],
            
            # Local para validar
            [sg.Text('Local para Validação:', size=(self.TamTexto,1)),
                sg.Input(size=(self.TamCamEntrada, 1), key='LocalValidar')],

            # Local para Salvar
            [sg.Text('Escolha o local para salvar:', size=(self.TamTexto, 1)),
                sg.In(size=(self.TamCamArq, 1), key="PastaSalvar"),
                sg.FolderBrowse(size=(self.TamBotArq, 1), button_text='Procurar Pasta')],
            
            [sg.Button('Gerar Certificado', key='Gerar')],

        ]

        #Cria a janela
        janela = sg.Window(self.NomeTela, size=(600, 250)).layout(layout)

        self.button, self.values = janela.Read()


    def RetornaValores(self):
        Valores = [
            self.values['ArquivoCSV'],
            self.values['ArquivoFundo'],
            self.values['ArquivoLogo'],
            self.values['NomeAssiante'],
            self.values['LocalValidar'],
            self.values['PastaSalvar']
        ]
        return Valores