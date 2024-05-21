>>> frase="Teria sido melhor assistir o filme de Pele"
>>> frase.count("a", 2, 10) 

Exemplo
>>> "mariana".index("a”)
>>> "mariana".index("a", 2)
>>> "mariana".index("a",5, 7)
>>> ’Mariana’.index(’ana’)
>>> ’Mariana’.index(’x’) 


>>> a = (1,2,3,4)
>>> b = (1.0, 2, ’3’, 4+0j)
>>> c = 1,2,3,4
>>> d = (1,) 

>>> x = 1, 2, 3
>>> x
>>> a, b, c = x
>>> a
>>> b
>>> c 


>>> x = 1, 2, 3
>>> x
(1, 2, 3)
>>> a, b, c = x
>>> a
1
>>> b
2
>>> c
3 

>>> x = (1,2,3)
>>> len(x)
3 

>>> x[0]
1

>>> x[0:2]
(1,2)

>>> x*2
(1,2,3,1,2,3)
>>> x + (5,4)
(1,2,3,5,4) 

>>> x[0] = 9
Traceback (most recent call last):
File "<pyshell#2>", line 1, in <module> x[0]=9
TypeError: ’tuple’ object does not support item assignment


def bombom(dinheiro,preco):
return float(dinheiro)/preco, dinheiro%preco

def bombom(dinheiro,preco):
return dinheiro//preco, dinheiro%preco


def bombom(dinheiro,preco):
return dinheiro//preco, dinheiro%preco

def maisbombom(dinheiro,preco):
return preco – bombom(dinheiro,preco)[1]


>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

1
>>> list(range(3, 8))
[3, 4, 5, 6, 7]

>>> list(range(3, 8, 2))
[3, 5, 7] 