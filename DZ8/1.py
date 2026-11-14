import logging

def info(info):
    logging.basicConfig(level=logging.INFO, format=f'{info} %(asctime)s', filename='log.log')
    logging.info(None)

info("you only asked for the time so rn its")