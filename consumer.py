#le role de ce consumer est de parcourir la liste des messages émis par le producer et d'afficher dans la console les stations dont le nombre de vélo disponible à changer
#Application en temps réel permettant de voir les locations de vélo de 28 villes dans le monde
#le consumer affiche bien les stations dont le nombre d'emplacement libre à changer dans toute les villes du monde 

import json
import pandas as pd
import pickle
from kafka import KafkaConsumer
import time

group_id="velib_sation"
topic_name="raw_velib_data"
consumer = KafkaConsumer(topic_name, bootstrap_servers='localhost:9092', group_id=group_id)
for msg in consumer:
    #data = msg.content()
    station = msg.value.decode()
    #data_dict = json.loads(data)
    print(station)
    #Données de l'Api nécessaire à notre traitement (nous avons scrapé l'Api station information)
    