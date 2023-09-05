"""
Repete vogais

Faça um programa que pode ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas

ex:

`python repete_vogais.py`
'Digite uma palavra (ou enter para sair): ' Python
'Digite uma palavra (ou enter para sair): ' Bruno
'Digite uma palavra (ou enter para sair): ' <enter>
Pythoon
Bruunoo
...
"""
words = []
while True:
    palavra = input("Digite uma palavra (ou enter para sair): ").strip()
    if not palavra:
        break
    palavra_final = ""
    for letra in palavra:
        # TODO: Remover acentuação
        if letra.lower() in "aeiouêâôõíúü":
            palavra_final += letra
        palavra_final += letra

    words.append(palavra_final)

print(*words, sep="\n")
