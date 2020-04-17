# IMPORTAÇÕES
import csv

def Importar(): # Função para Importar os dados de um arquivo CSV em lista e retorna a lista
    try:
        NomeArquivo = "Certi.csv" # Nome do arquivo
        arquivo = open(NomeArquivo) # Importar CSV
        dados = csv.reader(arquivo) # Le como lista
        return dados # retorna os dados importados 
    except FileNotFoundError:
        print("Arquivo não encontrado: ", NomeArquivo)
        exit()
    except:
        print("Erro na importação do arquivo: ", NomeArquivo)
        exit()