produto_1 = 20
produto_2 = 10

#Em caso de mesma precedência o Python considera quem vem primeiro da esquerda para direita

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = (10 + 5) * 4
print(x)

#Se desejar forçar uma precedêcia deve-se utilizar o parênteses

y = (10 / 2) + 25 * ((2 - 2) ** 2)
print(y)
