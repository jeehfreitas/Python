# -*- coding: utf-8 -*-

#Estruturas condicionais - IF

x = 1
y = 1000000000

if x > y:
	print("x é maior que y")

if y > x:
	print("y é maior que x")

#if else - se se não
if x > y:
	print("x é maior que y")
else:
	print("x não é maior que y")


#elif executa a primeira condição verdadeira que ele encontrar
if x == y:
	print("numeros iguais")
elif x < y:
	print("x é menor que y")
elif y > x:
	print("y maior que x")
else:
	print("numeros diferentes")