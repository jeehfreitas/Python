# -*- coding: utf-8 -*-

#Laços de repetições - 
#While

x = 1

while x < 10:
	print(x)
	#x = x + 1
	x += 1 # x = x + 1


# For

lista1 = [1,2,3,4,5]
lista2 = ["ola","mundo","!"]
lista3 = [0,"ola","biscoito","bolacha",9.99,True]

for i in lista1:
	print(i)

for i in lista2:
	print(i)

for i in lista3:
	print(i)


# For combinado com a função range

for i in range(10,20,2):
	print(i)
