# Função para gerar nome dos certificados
def NomeCertificado(linha): # Recebe um linha de dados
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