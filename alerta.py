"""
Alarme de temperatura

Faça um script que pergunta ao usuário qual a teperatura atual e o indice de umi
dade do ar
sendo que caso será exibida uma mensagem de alerta dependendo das condições:

temp maior que 45: ALERTA!!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA!! perigo calor úmido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp <0: ALERTA: Frio extremo
"""
import sys
import logging

log = logging.Logger("alerta")

info = {"temperatura": None, "umidade": None}
keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Qual a {key} do ar no momento? ").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)


temp = info["temperatura"]
umidade = info["umidade"]

if temp > 45:
    print("ALERTA!!! Perigo calor extremo")
elif (temp * 3) >= umidade:
    print("ALERTA!! perigo calor úmido")
elif temp >= 10 and temp <= 30:
    print("Normal")
elif temp >= 0 and temp <= 10:
    print("Frio")
elif temp < 0:
    print("ALERTA: Frio extremo")
