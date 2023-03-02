from kafka import KafkaConsumer
import csv

# Configuration du consumer
bootstrap_servers = ['localhost:9092']  # Adresse du serveur Kafka
topicName = 'velib_data'  # Nom du topic Kafka

# Création d'un objet KafkaConsumer pour le topic de Kafka
consumer = KafkaConsumer(topicName, bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest')

# Ouvrir un fichier CSV pour écrire les données agrégées
with open('aggregated_velib_data.csv', mode='w') as csv_file:

    fieldnames = ['station_id', 'name', 'latitude', 'longitude','capacity','stationCode','numBikesAvailable','num_bikes_available_types_mechanical','num_bikes_available_types_ebike','numDocksAvailable','Last_reported']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Agréger les données de toutes les stations Velib & Boucle infinie pour consommer les messages Kafka
    for message in consumer:

        # Convertir le message en une ligne CSV
        message_data = message.value.decode('utf-8').split(',')

        print(message_data)

        station_id = message_data[0]
        name = message_data[1]
        latitude = message_data[2]
        longitude = message_data[3]
        capacity = message_data[4]
        stationCode = message_data[5]
        numBikesAvailable = message_data[6]
        num_bikes_available_types_mechanical = message_data[7]
        num_bikes_available_types_ebike = message_data[8]
        numDocksAvailable = message_data[9]
        Last_reported=message_data[10]

        line = {
            'station_id': station_id, 
            'name': name,
            'latitude': latitude, 
            'longitude': longitude,
            'capacity': capacity,
            'stationCode': stationCode,
            'numBikesAvailable': numBikesAvailable, 
            'num_bikes_available_types_mechanical': num_bikes_available_types_mechanical,
            'num_bikes_available_types_ebike': num_bikes_available_types_ebike, 
            'numDocksAvailable': numDocksAvailable,
            'Last_reported':Last_reported
        }

        # Écrire la ligne CSV dans le fichier
        writer.writerow(line)