# Funçao para tratar uma string e deixa-lá capitalziada em casa item
def TratarTexto(Texto): # Recebe uma string como entrada
    Texto = Texto.split(' ') # Separa a string por espaço, gerando uma lista
    for Indice, Nome in enumerate(Texto): # Acessa cada item da lista
        Texto[Indice] = Nome.capitalize() # Capitaliza cada item da lista
    Texto = " ".join(Texto) # Tansforma a lista em string novamente
    return Texto # Retorna a string

# Função para tratar a hora e deixa-la com dois algarismos sempre
def TratarHoras(Hora): # Recebe a hora
    if (len(Hora) == 1): # Converte em inteiro e verifica se é menor de 10
        return "0"+Hora # Se for retorna uma string começada com 0 + a hora recebida
    elif (len(Hora) > 3):
        print("Verifique a coluna de horas e garanta que tenha no máximo três algarismos")
        print("Erro no valor: ", Hora)
    else:
        return Hora # Se não for, retorna a hora recebida