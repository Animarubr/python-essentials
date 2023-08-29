#! /usr/bin/env python

"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiete o programa exibe a mensagem
correspondente.

Como usar:

Ter a variável LANG devidamente configurada ex:
	export LANG=pt_br

Ou informe atraves do CLI argument `--lang`

Ou o usuário terá que digitar

Execução:
	
	python3 hello.py
	ou
	./hello.py
"""
__version__ = "0.1.3"
__author__ = "Marcos Silva"
__license__ = "Unlicense"

import os
import sys

arguments = {"lang": None, "count": 1}
for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid key -> `{key}`")
        sys.exit()
    arguments[key] = value


current_language = arguments["lang"]
if current_language is None:
    if current_language in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

# O(1)
print(msg[current_language] * int(arguments["count"]))
