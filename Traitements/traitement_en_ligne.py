# import necessary libraries
from pyspark.sql.functions import split,avg
from pyspark.sql.types import StructType, StructField, StringType,IntegerType,FloatType
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.1.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 pyspark-shell'
import findspark
findspark.init('/opt/spark')
from pyspark.sql import SparkSession
from pymongo import MongoClient


# Connexion à la base de données MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["velib"]
mongo_collection = mongo_db["Average_station"]


# Définition du topic Kafka à consommer
topic = "velib_data"


# Création de la session Spark
spark = (SparkSession
        .builder
        .appName("consumer_structured_streaming_test_1")  
        .getOrCreate())


# Définition du schéma du message Kafka
message_schema = StructType([
    StructField("key", StringType()),
    StructField("value", StringType()),
    StructField("topic", StringType()),
    StructField("partition", StringType()),
    StructField("offset", StringType())
])


# Créer un stream de données Spark à partir du topic Kafka et lire dans un dataframe
kafka_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", topic) \
    .load() \
    .selectExpr("CAST(value AS STRING)")


# split the "value" column on comma and create new columns
split_df = kafka_df.select(split(kafka_df["value"], ",").alias("split_values"))


# select the split columns
final_df = split_df.selectExpr(
    "CAST(split_values[0] AS INTEGER) as station_id",
    "split_values[1] as name",
    "CAST(split_values[2] AS FLOAT) as latitude",
    "CAST(split_values[3] AS FLOAT) as longitude",
    "CAST(split_values[4] AS INTEGER) as capacity",
    "CAST(split_values[5] AS INTEGER) as stationCode",
    "CAST(split_values[6] AS INTEGER) as numBikesAvailable",
    "CAST(split_values[7] AS INTEGER) as numBikesAvailableTypesMechanical",
    "CAST(split_values[8] AS INTEGER) as numBikesAvailableTypesEbike",
    "CAST(split_values[9] AS INTEGER) as numDocksAvailable",
)


# Calcule la moyenne par station pour chaque station disponible : du nombre de vélos mécaniques disponibles,du nombre de vélos électriques disponibles et du nombre de place libres disponibles
station_average = final_df \
    .groupBy("station_id") \
    .agg(avg("numBikesAvailableTypesMechanical").alias("Avg_numBikesAvailableTypesMechanical"),
         avg("numBikesAvailableTypesEbike").alias("Avg_numBikesAvailableTypesEbike"),
         avg("numDocksAvailable").alias("Avg_numDocksAvailable"),
        )


# Calcule la moyenne d'occupation des stations dans une zone géographique pour chaque station disponible : du nombre de vélos mécaniques disponibles,du nombre de vélos électriques disponibles et du nombre de place libres disponibles
zone_avgs = final_df.filter("latitude > 48.865983 AND latitude < 48.91206062860357 AND longitude > 2.275725 AND longitude < 2.4865807592869") \
    .agg(avg("numBikesAvailableTypesMechanical").alias("Zone_Avg_numBikesAvailableTypesMechanical"),
         avg("numBikesAvailableTypesEbike").alias("Zone_Avg_numBikesAvailableTypesEbike"),
         avg("numDocksAvailable").alias("Zone_Avg_numDocksAvailable"))


# write the results to MongoDB
station_average.writeStream \
    .foreachBatch(lambda batch_df, batch_id: batch_df.write.format("mongo").option("uri", "mongodb://localhost:27017/").option("database", "velib").option("collection", "Average_station").mode("append").save())

zone_avgs.writeStream \
    .foreachBatch(lambda batch_df, batch_id: batch_df.write.format("mongo").option("uri", "mongodb://localhost:27017/").option("database", "velib").option("collection", "Average_station").mode("append").save())


# start the streaming query
"""query = final_df \
    .writeStream \
    .format("console") \
    .option("truncate", "false") \
    .start()
"""

# Write the output to the console
query = station_average \
    .writeStream \
    .format("console") \
    .option("truncate", "false") \
    .outputMode("complete") \
    .trigger(processingTime="3 minutes") \
    .start()


# wait for the query to terminate
query.awaitTermination()
