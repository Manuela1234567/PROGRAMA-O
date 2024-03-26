def calcular_soma_media(lista):
    # Calcula a soma dos números na lista
    soma = sum(lista)
    # Calcula a média dos números
    media = soma / len(lista)
    return soma, media

# Exemplo de uso:
numeros = [1, 2, 3, 4]
soma_resultado, media_resultado = calcular_soma_media(numeros)
print(f"Soma: {soma_resultado}, Média: {media_resultado:.2f}")



def substituir_palavra(lista, palavra_procurada, nova_palavra):
    return [nova_palavra if palavra == palavra_procurada else palavra for palavra in lista]

# Exemplo de uso:
frutas = ["banana", "morango", "limão"]
nova_lista = substituir_palavra(frutas, "morango", "abacaxi")
print(nova_lista)



def gerar_triangulo_asteriscos(num_linhas):
    for i in range(1, num_linhas + 1):
        print(" " * (num_linhas - i) + "*" * (2 * i - 1))

# Exemplo de uso:
num_linhas = 4
gerar_triangulo_asteriscos(num_linhas)