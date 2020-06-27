# IMPORTAÇÕES
import csv

def Importar(CaminhoArquivo): # Função para Importar os dados de um arquivo CSV em lista e retorna a lista
    try:
        Arquivo = open(CaminhoArquivo) # Importar CSV
        Dados = csv.reader(Arquivo) # Le como lista
        return Dados # retorna os dados importados 
    except FileNotFoundError:
        print("Arquivo não encontrado: ", CaminhoArquivo)
        exit()
    except:
        print("Erro na importação do arquivo: ", CaminhoArquivo)
        exit()