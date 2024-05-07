def copiar_conteudo_arquivo(origem, destino):
    try:
        with open(origem, "r") as arquivo_origem:
            conteudo = arquivo_origem.read()
        
        with open(destino, "w") as arquivo_destino:
            arquivo_destino.write(conteudo)
        
        print(f"Conteúdo do arquivo '{origem}' foi copiado para o arquivo '{destino}' com sucesso.")
    except FileNotFoundError:
        print("Arquivo de origem não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
nome_arquivo_origem = "arquivo_de_exemplo.txt"
nome_arquivo_destino = "novo_arquivo.txt"
copiar_conteudo_arquivo(nome_arquivo_origem, nome_arquivo_destino)