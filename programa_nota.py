# -*- coding: utf-8 -*-

#Média

"""Faça um programa que receba duas notas digitadas pelo usuário. 
Se a nota for maior ou igual a seis, escreva aprovado, 
senão escreva reprovado."""

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

resultado = nota1 + nota2

if resultado >= 6:
	print("Aprovado")

elif resultado >0 and resultado < 6:
	print("Reprovado")

else:
	print("Nota Inválida")
	