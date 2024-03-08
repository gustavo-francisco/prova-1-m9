import paho.mqtt.client as mqtt
import time
import json
import random
import numpy as np

sensors_file = open ('sensors.json')
json_array = json.load(sensors_file)

class DynamicMessage:
    def __init__(self, **entries):
        self.__dict__.update(entries)

    def message(self):
        attributes = ', '.join(f'{key}={value}' for key, value in self.__dict__.items())
        return str(attributes)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publiser")

client.connect("localhost", 1891, 60)

freezer_publish_normal = DynamicMessage(**json_array[0]).message()
refrigerator_publish_normal = DynamicMessage(**json_array[1]).message()
freezer_publish_above = DynamicMessage(**json_array[2]).message()
refrigerator_publish_above = DynamicMessage(**json_array[3]).message()
freezer_publish_below = DynamicMessage(**json_array[4]).message()
refrigerator_publish_below = DynamicMessage(**json_array[5]).message()

try:
    while True:
        message = "Hello MQTT" + time.strftime("%H:%M:%S")
        client.publish("sensors/topic", freezer_publish_normal)
        client.publish("sensors/topic", refrigerator_publish_normal)
        print(f"Publicado: {freezer_publish_normal} e {refrigerator_publish_normal}")
        client.publish("sensors/topic", freezer_publish_above + " TEMPERATURA DO FREEZER ESTÁ ACIMA! ")
        client.publish("sensors/topic", refrigerator_publish_above + " TEMPERATURA DA GELADEIRA ESTÁ ACIMA! ")
        print(f"Publicado: {freezer_publish_above} e {refrigerator_publish_above}")
        client.publish("sensors/topic", freezer_publish_below + " TEMPERATURA DO FREEZER ESTÁ ABAIXO! ")
        client.publish("sensors/topic", refrigerator_publish_below + " TEMPERATURA DA GELADEIRA ESTÁ ABAIXO! ")
        print(f"Publicado: {freezer_publish_below} e {refrigerator_publish_below}")
        time.sleep(2)
except KeyboardInterrupt:
    print("Publicação encerrada")

client.disconnect()