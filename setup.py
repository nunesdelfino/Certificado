#!/bin/python3
# -*- coding: utf-8 -*-

# Gerador de certificados
# Autor: Gabriel Nunes Delfino
# github: nunesdelfino


# IMPORTAÇÕES

from Modulos.AssinanteEvento import Assinante
from Modulos.CriaPasta import CriarPasta
from Modulos.GerarCertificado import Gerar
from Modulos.GerarNome import NomeCertificado
from Modulos.GerarQRCode import GerarQR
from Modulos.ImportarCSV import Importar
from Modulos.MoverCertificados import Mover
from Modulos.Ajuda import Ajuda


AjudaEscolha = str(input("Quer exibir a ajuda? [S - Para mostrar] ")).lower()
if (AjudaEscolha == "s"):
    Ajuda() # Exibe a ajuda

Assinante = Assinante() # Coleta o nome do assinante do certificado
GerarQR() # Gerar o QR Code para validar o Certificado
Dados = Importar() # Importa os dados do arquvio CSV
Gerar(Dados, Assinante) # Gera o Certificado
