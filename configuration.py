import json
import re


def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
        if not re.search('^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', config['server']):
            raise Exception("Chyba: chybná IP adresa serveru")
        if len(config['database']) < 1:
            raise Exception("Chyba: chybný název databáze")
        if len(config['username']) < 1:
            raise Exception("Chyba: chybné uživatelské jméno")
        if len(config['password']) < 1:
            raise Exception("Chyba: chybné heslo")
        return config
