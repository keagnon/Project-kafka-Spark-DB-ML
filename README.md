### Mise en place d'un système de traitement des vélos partagés (vélib) 
<!-- BLOG-POST-LIST:START -->
Ce repository héberge notre travail effectué lors d'un projet de notre majeure Big Data et Dataviz.

L'objectif de ce projet est de mettre en place un système de traitement de données pour la métrople de Paris pour augmenter l'usage de son service de vélos partagés (vélib) et améliorer l’expérience de ses abonnements.

Il se compose de fichiers .ipynb de data cleaning, de fichiers .py pour le code python, de fichiers .csv  qui étaient nos sources de données ainsi qu'une base de données NoSQL MongoDB.
<!-- BLOG-POST-LIST:END -->

<img align="center" src="/Images/station_velib.jpg"/>
<br/>


## Architecture globale du projet 
<img align="center" src="/Images/architecture-projet-velib.png"/>
<br/>


## Outils
<!-- BLOG-POST-LIST:START -->
- Apache Kafka
- Spark
- MongoDB
- Databriks
- Spark ML
- API SQL
- Pandas
- Logic regression
- Système d'exploition : Ubuntu
<!-- BLOG-POST-LIST:END -->


# Mise en place du projet
<!-- BLOG-POST-LIST:START -->
Pour mettre en place ce système de traitement de données nous avons divisé notre projet en 4 grandes parties :


## Partie 1 : Récupération des données 
Nous avons collecté les données en tant réel sur le site https://data.opendatasoft.com/pages/home/ensuite (scraping api) puis nous avons créer un producer kafka qui envoi les données reçu sur une instance Kafka toute les minutes tout en vérifiant qu'il ne prend pas 2 fois la mme donnée.
<!-- BLOG-POST-LIST:END -->


## Partie 2 : Traitement en ligne
<!-- BLOG-POST-LIST:START -->
Ici nous avons effectué des traitements en ligne pour mesurer statistiques d'utilisation des stations en temps réel. Pour ce fait, nous avons connecté Spark Streaming à Kafka et calculer la moyenne pour chaque station disponible : 
- du nombre de vélos mécaniques disponibles
- du nombre de vélos électriques disponibles
- du nombre de place libres disponibles
- moyenne d'occupation des stations dans une zone géographique 
Puis nous avons stocké le résultat des traitements dans une base de donnée Nosql MongoDB
<!-- BLOG-POST-LIST:END -->


## Partie 3 : Traitement par batch
<!-- BLOG-POST-LIST:START -->
Ici nous avons effectué des traitements sur des batchs afin d'avoir des statistiques d'utilisation à plus long terme. Pour ce fait, nous avons :
- Agréger l'ensemble des données récupérée dans un fichier csv
- Créer un cluster gratuit et un notebook sur https://community.cloud.databricks.com
- Analyser les données
- Faire un traitement des données l'API SQL
- Comparer le temps de traitement entre une partition et deux partitions
<!-- BLOG-POST-LIST:END -->


## Partie 4 : Machine learning
<!-- BLOG-POST-LIST:START -->
Pour cette partie, nous avons procédé comme suit :
- Récupérer toutes les données d'une station seulement
- faire un modèle qui prédire si une station sera remplie à un instant tt en fonction du nombre de place disponibles
<!-- BLOG-POST-LIST:END -->






