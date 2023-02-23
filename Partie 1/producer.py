# Import des modules nécessaires
import json
import time
import pandas as pd
from kafka import KafkaProducer    
import requests
import collections
collections.Callable = collections.abc.Callable

# Créer un producteur Kafka
producer = KafkaProducer(bootstrap_servers="localhost:9092")

# Définir les informations de connexion Kafka
topic_name="raw_velib_data"

# Stocker la dernière mise à jour
last_update = 0

while True:
    try:

        #Get informations about the station
        url1="https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
        response_api_station_information=requests.get(url1)
   
        url2="https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"
        response_api_station_status=requests.get(url2)

        #Afficher le nombre de station disponible dans l'API
        number_rows=len(response_api_station_information.json()['data']['stations'])

        #Date de dernière mis-à jour des informations de la ville
        lastUpdatedOther =response_api_station_information.json()['lastUpdatedOther']

        count=0

        # Bonus partie 1 : Vérifier si les données sont différentes de la dernière mise à jour
        if lastUpdatedOther != last_update:

            # Mettre à jour la dernière mise à jour
            last_update=lastUpdatedOther

            for i in range(6): 

                station_id=response_api_station_information.json()['data']['stations'][i]['station_id']
                name=response_api_station_information.json()['data']['stations'][i]['name']
                lat=response_api_station_information.json()['data']['stations'][i]['lat']
                lon=response_api_station_information.json()['data']['stations'][i]['lon']
                capacity=response_api_station_information.json()['data']['stations'][i]['capacity']
                stationCode=response_api_station_information.json()['data']['stations'][i]['stationCode']
                num_bikes_available=response_api_station_status.json()['data']['stations'][i]['num_bikes_available']
                numBikesAvailable=response_api_station_status.json()['data']['stations'][i]['numBikesAvailable']
                num_bikes_available_types_mechanical=response_api_station_status.json()['data']['stations'][i]['num_bikes_available_types'][0]['mechanical']
                num_bikes_available_types_ebike=response_api_station_status.json()['data']['stations'][i]['num_bikes_available_types'][1]["ebike"]
                num_docks_available=response_api_station_status.json()['data']['stations'][i]['num_docks_available']
                numDocksAvailable=response_api_station_status.json()['data']['stations'][i]['numDocksAvailable']
                is_installed=response_api_station_status.json()['data']['stations'][i]['is_installed']
                is_returning=response_api_station_status.json()['data']['stations'][i]['is_returning']
                is_renting=response_api_station_status.json()['data']['stations'][i]['is_renting']
                last_reported=response_api_station_status.json()['data']['stations'][i]['last_reported']
                
                msg=f"{station_id},{name},{lat},{lon},{capacity},{stationCode},{numBikesAvailable},{num_bikes_available_types_mechanical},{num_bikes_available_types_ebike},{numDocksAvailable}"
               
                # Envoyer les données au producteur Kafka
                producer.send(topic_name, bytes(msg, encoding='utf8'))

                print(f'sending data to kafka, #{count}')
                count += 1
        
        # Attendre une minute avant de récupérer les données à nouveau
        time.sleep(60)

        print(f"Data available at,{time}")


    except Exception as e:
        print(f"Error: {e}")

    