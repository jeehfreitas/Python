# -*- coding: utf-8 -*-

# Strings com Método

a = "Jéssica"
b = "Freitas"

concatenar = a + " " + b + "\n"

# Strip anula caracteres especiais - nesse exemplo foi a quebra de linha /n
print(concatenar.strip())

#print(concatenar.lower()) # deixa as letras minusculas
#print(concatenar.upper()) # deixa as letras maiúsculas

concatenar = concatenar.upper() # transforma definitivamente as letras em maiúsculas
print(concatenar)


# Split transforma uma frase em lista - chamado também de Delimitador
minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split("r")
print(minha_lista)


# Busca onde está localizada a string solicitada, no caso do exemplo Roma
busca = minha_string.find("rei")
print(busca)

print(minha_string[busca:])


#Replace subtitui partes de uma string
minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)