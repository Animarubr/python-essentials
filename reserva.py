"""
Faça um programa de terminal que exibe ao usuário uma lista dos quartos
disponíveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texo
separado por virgulas.

`quartos.txt`
# codigo, nome, preço
1, Suite Master, 500
2, Quarto Família, 200
3, Quarto Single, 100
4, Quarto Simples, 50

O Programa pergunta o usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservas.txt`

# cliente, quarto, dias
Bruno, 3,12


Se o outro usuário tentar reservar o mesmo quarto o programa deve exibir
uma mensagem informando que já esta reservado.
"""
import logging
import sys

log = logging.Logger("reserva")

ocupados = {}
try:
    for line in open("reservas.txt"):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {"nome": nome.encode("utf-8"), "dias": dias}

except FileNotFoundError:
    log.error("Arquivo reservas.txt não exist")
    sys.exit(1)


quartos = {}
try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco),  # TODO: Decimal
            "disponivel": False if int(codigo) in ocupados.keys() else True,
        }

except FileNotFoundError:
    log.error("Arquivo quartos.txt não exist")
    sys.exit(1)

print("Reserva Hotel Pythonico")
print("-" * 40)
if len(ocupados) == len(quartos):
    print("Hotel Lotado!")
    sys.exit(1)

nome_cliente = input("Nome do cliente: ").strip()
print("Lista de quartos disponiveis:")

for codigo, dados in quartos.items():
    nome = dados["nome"]
    preco = dados["preco"]
    disponivel = "📛" if not dados["disponivel"] else "👍"
    print(f"{codigo} - {nome} - R$ {preco:.2f} - {disponivel}")
print("-" * 40)


try:
    num_quarto = int(input("Número do quarto: ").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} esta ocupado.")
        sys.exit(1)

except ValueError:
    log.error("Número inválido, digite apenas digitos.")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(1)

try:
    dias = int(input("Qauntos dias?: ").strip())
except ValueError:
    log.error("Número inválido, digite apenas digitos.")
    sys.exit(1)

nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]
total = preco_quarto * dias

with open("reservas.txt", "a") as file_:
    file_.write(f"{nome_cliente},{num_quarto},{dias}\n")

print(
    f"{nome_cliente} você escolheu o quarto {nome_quarto} e vai custar: R${total:.2f}"
)
