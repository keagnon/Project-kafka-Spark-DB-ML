# Import des modules nécessaires
from kafka import KafkaConsumer
import json


# Définir les informations de connexion Kafka
KAFKA_TOPIC = 'velib_data'


# Créer un consumer Kafka
consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers='localhost:9092')


# bouclez pour consommer les messages du topic Kafkaa
for msg in consumer:
    # Récupérer les données du message
   
    # récupérez le message en tant que dictionnaire
    station = msg.value.decode()
    print(station)


