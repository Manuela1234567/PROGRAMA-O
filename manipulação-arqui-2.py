def imprimir_conteudo_arquivo():
    nome_arquivo = input("Por favor, digite o nome do arquivo de texto: ")
    
    # Abrindo o arquivo em modo de leitura ('r')
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)

# Chamando a função para imprimir o conteúdo do arquivo
imprimir_conteudo_arquivo()