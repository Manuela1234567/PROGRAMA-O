def copiar_arquivo(origem, destino):
    """
    Lê o conteúdo do arquivo de origem e escreve em um novo arquivo de destino.
    """
    try:
        with open(origem, 'r') as arquivo_origem:
            conteudo = arquivo_origem.read()
            with open(destino, 'w') as arquivo_destino:
                arquivo_destino.write(conteudo)
        print(f"Conteúdo do arquivo {origem} copiado para {destino} com sucesso!")
    except FileNotFoundError:
        print(f"Arquivo {origem} não encontrado.")
        
def encontrar_nome_por_numero(arquivo, numero):
    """
    Lê o arquivo e exibe o nome correspondente ao número fornecido.
    """
    try:
        with open(arquivo, 'r') as arquivo_exemplo:
            linhas = arquivo_exemplo.readlines()
            nomes = [linha.strip() for linha in linhas]
            if 1 <= numero <= len(nomes):
                print(f"Nome correspondente ao número {numero}: {nomes[numero - 1]}")
            else:
                print(f"Número fora do intervalo válido.")
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado.")
# Exemplo de uso:
# copiar_arquivo("nome_do_usuario.txt", "novo_arquivo.txt")
# encontrar_nome_por_numero("arquivo-exemplo", 3)