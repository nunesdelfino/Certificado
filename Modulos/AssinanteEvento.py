def Assinante(): # Função para coletar e validar o nome do assinante
    try:
        while True: # Iniciar o loop de verificação
            Assinante = str(input("Nome do assinante do certificado: ")) # Recebe o nome do assinante
            if Assinante != "": # Verifica se o usuário deixou vazio
                return Assinante # Retorna a string Assinante
            else:
                print("O nome do assinante não pode estar vazio!")
    except KeyboardInterrupt: # Caso o usuário interrompa o código
        print("Execução do código interrompida pelo usuário")
        exit()
