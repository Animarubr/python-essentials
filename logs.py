#!/usr/bin/env python3

import os
import logging
from logging import handlers

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# nossa instancia
# TODO: usar funções
# TODO: usar lib (loguru)
log = logging.Logger(__name__, log_level)
# level
# ch = logging.StreamHandler()  # Console/terminal/stderr
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler("meulog.log", maxBytes=100, backupCount=10)
fh.setLevel(log_level)
# formatação
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)

# destino
# log.addHandler(ch)
log.addHandler(fh)

"""log.debug("Mensagem para o dev, qe, sysadmin")
log.info("Mensagem para os usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execução")
log.critical("Erro geral ex: Banco de dados sumiu")"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
