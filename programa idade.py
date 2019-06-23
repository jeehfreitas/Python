# -*- coding: utf-8 -*-

#Faça um programa que receba a idade do usuário
#e diga se ele é maior ou menor de idade.

idade = int(input("Digite sua idade: "))
maior_idade = 18
#menor_idade = <18

if idade >= maior_idade:
 	print("Maior de idade")

elif idade > 0 and idade < maior_idade:
	print("Menor de idade")
	
else:
 	print("Idade Inválida")

