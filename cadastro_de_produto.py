#!/usr/bin/env python
"""Cadastro de produtos"""
__version__ = "0.1.0"

produto = {
    "nome": "Caneta",
    "cores": ["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,
}


cliente = {"nome": "Bruno"}
compra = {"cliente": cliente, "produto": produto, "quantidade": 3}
total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra['cliente']['nome']} comprou {compra['quantidade']} unidades de {compra['produto']['nome']} e pagou o total de {total_compra}"
)
