import logging

logger = logging.getLogger("polymarket_bot")

if not logger.handlers:
    handler = logging.StreamHandler()
    logger.addHandler(handler)

logger.setLevel(logging.INFO)
