def bombom(dinheiro,preco):
    return float(dinheiro)/preco, dinheiro%preco

def maisbombom(dinheiro,preco):
    return preco_bombom(dinheiro,preco)[1]

def numeros_pares(numero):
    lista_pares = []
    for i in range(2, numero + 1, 2):
        lista_pares.append(i)
    return lista_pares

# Exemplo de uso:
numero = 10
print(numeros_pares(numero))