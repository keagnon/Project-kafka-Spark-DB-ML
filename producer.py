#Trouver un client afa en python
import json
import time
import pandas as pd
from kafka import KafkaProducer#pip install kafka-python

producer = KafkaProducer(bootstrap_servers="localhost:9092")
topic_name="raw_velib_data"
raw_data_file_path="velib_data.csv"#jeux de données de test
data = pd.read_csv(raw_data_file_path)

for i in range(len(data)): 
    df_value = data.iloc[i]
    value = df_value.to_dict()#Convertir le jeux de donnée sous forme de dictionnaire
    print(f"key : {i}, value : {value}")#That is what we are going to send to our produce
    producer.send(topic_name,json.dumps(value).encode())
    time.sleep(2)
