def imprimir_informacoes(nome, idade, cidade):
    print("Nome:", nome, sep=" ", end=", ")
    print("Idade:", idade, sep=" ", end=", ")
    print("Cidade:", cidade, sep=" ")

# Exemplo de uso da função
imprimir_informacoes("Maria", 23, "Rio de Janeiro")



def calcular():
    # Pedir ao usuário dois números e a operação desejada
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    # Calcular o resultado com base na operação especificada
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        # Verificar se o segundo número é zero para evitar divisão por zero
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            return
        resultado = num1 / num2
    else:
        print("Operação inválida.")
        return

    # Imprimir o resultado
    print("Resultado:", resultado)

# Exemplo de uso da função
calcular()





def lista_de_compras():
    # Pedir ao usuário para digitar os itens da lista de compras separados por vírgula
    entrada = input("Digite os itens da lista de compras separados por vírgula: ")

    # Dividir a entrada do usuário em uma lista de itens
    itens = entrada.split(',')

    # Imprimir os itens em linhas separadas usando um laço
    print("Lista de Compras:")
    for item in itens:
        print(item.strip())  # Remover espaços em branco extras, se houver

# Exemplo de uso da função
lista_de_compras()



def celsius_para_fahrenheit():
    # Pedir ao usuário a temperatura em graus Celsius
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    # Converter a temperatura para Fahrenheit usando a fórmula de conversão
    fahrenheit = (celsius * 9/5) + 32

    # Imprimir o resultado
    print("A temperatura em Fahrenheit é:", fahrenheit)

# Exemplo de uso da função
celsius_para_fahrenheit()



def digitar_nomes():
    nomes = []  # Lista para armazenar os nomes digitados

    # Loop infinito para pedir nomes até que 'sair' seja digitado
    while True:
        nome = input("Digite um nome ou 'sair' para encerrar: ")
        
        if nome.lower() == 'sair':
            break  # Sai do loop se 'sair' for digitado
        else:
            nomes.append(nome)  # Adiciona o nome à lista

    # Imprimir todos os nomes digitados
    print("Nomes digitados:")
    for nome in nomes:
        print(nome)

# Exemplo de uso da função
digitar_nomes()