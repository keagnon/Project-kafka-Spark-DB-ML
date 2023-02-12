import requests
import json
import pandas as pd


#Get informations about the API
url1="https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
response_api_station_information=requests.get(url1)
station_information=response_api_station_information.json()['data']['stations'][0]
#print(station_information)


url2="https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"
response_api_station_status=requests.get(url2)
station_status=response_api_station_status.json()['data']['stations'][0]
#print(station_status)


#Afficher le nombre de station disponible dans l'API
number_rows_in_station_information=len(response_api_station_information.json()['data']['stations'])
number_rows_in_station_status=len(response_api_station_status.json()['data']['stations'])
print(number_rows_in_station_information,number_rows_in_station_status)

#Date de dernière mis-à jour des informations de la ville
lastUpdatedOther =response_api_station_information.json()['lastUpdatedOther']
#print(lastUpdatedOther)1453


#Durée de vie de l’information au-delà de laquelle elle doit être considérée comme obsolète
ttl =response_api_station_information.json()['ttl']
#print(ttl)

list_of_data = []
#Creation fonction get_velib_data pour récupérer les différentes lignes de données des APIs
def get_velib_data(nrows):
    
    for i in range (0,nrows):
        
        #Données de l'Api nécessaire à notre traitement (nous avons scrapé l'Api station information)
        station_id=response_api_station_information.json()['data']['stations'][i]['station_id']
        name=response_api_station_information.json()['data']['stations'][i]['name']
        lat=response_api_station_information.json()['data']['stations'][i]['lat']
        lon=response_api_station_information.json()['data']['stations'][i]['lon']
        capacity=response_api_station_information.json()['data']['stations'][i]['capacity']
        stationCode=response_api_station_information.json()['data']['stations'][i]['stationCode']
        

        #Données de l'Api nécessaire à notre traitement (nous avons scrapé de l'Api station status)
        stationCode=response_api_station_status.json()['data']['stations'][i]['stationCode']
        station_id=response_api_station_status.json()['data']['stations'][i]['station_id']
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

        list_of_data.append([station_id,name,lat,lon,capacity,stationCode,num_bikes_available,numBikesAvailable,num_bikes_available_types_mechanical,num_bikes_available_types_ebike,num_docks_available,numDocksAvailable,is_installed,is_returning,is_renting,last_reported])
        
        #print("------------------------")
        #print(f"Station {i}",station_id,name,lat,lon,capacity,stationCode,num_bikes_available,numBikesAvailable,num_bikes_available_types_mechanical,num_bikes_available_types_ebike,num_docks_available,numDocksAvailable,is_installed,is_returning,is_renting,last_reported)

get_velib_data(200)

df = pd.DataFrame(list_of_data,columns=['station_id','name','latitude','longitude','capacity','stationCode','num_bikes_available','numBikesAvailable','num_bikes_available_types_mechanical','num_bikes_available_types_ebike','num_docks_available','numDocksAvailable','is_installed','is_returning','is_renting','last_reported'])
print(df)
df.to_csv('velib_data.csv',index=True)