#!/usr/bin/env python3
"""
faça um programa que imprime os números pares de 1 à 200

ex:
`python numeros_pares.py`
2
4
6
8
...
"""

numeros = range(1, 201)
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
