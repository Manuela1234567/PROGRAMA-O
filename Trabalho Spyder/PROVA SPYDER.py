# Definindo as vari�veis
numeros = [10, 20, 30, 40]
frase = "Esta � uma frase de exemplo"
palavra = "Python"

# Calculando a m�dia aritm�tica dos n�meros
media = sum(numeros) / len(numeros)
print("M�dia aritm�tica dos n�meros:", media)

# Calculando o quadrado de um dos n�meros
numero_quadrado = numeros[0] ** 2
print("Quadrado do primeiro n�mero:", numero_quadrado)

# Calculando o dobro de um dos n�meros
numero_dobro = numeros[1] * 2
print("Dobro do segundo n�mero:", numero_dobro)

# Contando a quantidade de letras na palavra
qtd_letras = len(palavra)
print("Quantidade de letras na palavra:", qtd_letras)

# Contando a quantidade de espa�os em branco na frase
qtd_espacos = frase.count(" ")
print("Quantidade de espa�os em branco na frase:", qtd_espacos)

# Verificando se o primeiro n�mero � maior que o segundo
primeiro_maior = numeros[0] > numeros[1]
print("O primeiro n�mero � maior que o segundo:", primeiro_maior)

# Encontrando o maior n�mero
maior_numero = max(numeros)
print("O maior n�mero �:", maior_numero)


