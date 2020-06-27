#!/bin/bash
# -*- coding: utf-8 -*-

# Gerador de certificados
# Autor: Gabriel Nunes Delfino
# github: nunesdelfino

# IMPORTAÇÕES

from Modulos.Tela import TelaInicial
from Modulos.GerarQRCode import GerarQR
from Modulos.ImportarCSV import Importar
from Modulos.GerarCertificado import GerarCertificado

Dados = []

Dados = TelaInicial().RetornaValores()

GerarQR(Dados[4]) # Gerar o QR Code para validar o Certificado
DadosCSV = Importar(Dados[0]) # Importa os dados do arquvio CSV
GerarCertificado().Gerar(DadosCSV, Dados[1], Dados[2], Dados[3], Dados[5]) # Gera o Certificado
