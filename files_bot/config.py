
import json

with open("./config.json", "r") as configfile:
    config = json.load(configfile)

def get_estado_log():
    return (F'Estado de los logs: {config["log"]}')

#print("Autor: " + config["autor"])
#print("Ciclos: " + config["ciclos"])
