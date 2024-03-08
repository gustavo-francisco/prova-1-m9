import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Recebido: {message.payload.decode()} no tópico {message.topic}")

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Conexão bem sucedida!")
        client.subscribe("sensors/topic")
    else:
        print(f"Conexão falhou! Código {reason_code}")
        exit(reason_code)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_subscriber")
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1891, 60)

client.loop_forever()