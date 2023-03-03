### Mise en place d'un système de traitement des vélos partagés (vélib) 
<!-- BLOG-POST-LIST:START -->
Ce repository héberge notre travail effectué lors d'un projet de notre majeure Big Data et Dataviz.

L'objectif de ce projet est de mettre en place un système de traitement de données pour la métrople de Paris dans le but d'augmenter l'usage de son service de vélos partagés (vélib) et améliorer l’expérience de ses abonnements.
Il se compose de fichiers .ipynb de data analysis, des fichiers .py pour le code python, de fichier .csv pour agréger des données collectées dans le but d'obtenir une vue d'ensemble et une compréhension plus complète des données, des fichiers .md contenant les liens de chaque notebook créé dans le databrick (une pour le traitement avec par batch & l'API SQL et un second pour la mise en place du modèle de machine Learning avec Spark Ml ) ainsi qu'une base de données NoSQL (MongoDB).

<!-- BLOG-POST-LIST:END -->

<img align="center" src="/Images/station_velib.jpg"/>
<br/>


## Architecture globale du projet 
<img align="center" src="/Images/Architecture_projet_velib2.png"/>
<br/>


## Outils et librairies
<!-- BLOG-POST-LIST:START -->
- Apache Kafka
- MongoDB
- Databriks
- Spark ML
- API SQL
- Spark
- Pandas
- Python
- Logistic regression
- Système d'exploition : Ubuntu

Plus de détail : Voir fichier requirements.txt
<!-- BLOG-POST-LIST:END -->


# Mise en place du projet
<!-- BLOG-POST-LIST:START  -->
Pour mettre en place ce système de traitement de données nous avons divisé notre projet en 4 grandes parties :


## Partie 1 : Récupération des données 
Nous avons collecté les données en tant réel sur le site https://data.opendatasoft.com/pages/home/ensuite (scraping api) puis nous avons créé un producer kafka qui envoi les données reçu sur une instance Kafka toute les minutes tout en vérifiant qu'il ne prend pas deux fois la même donnée.
<!-- BLOG-POST-LIST:END -->


## Partie 2 : Traitement en ligne
<!-- BLOG-POST-LIST:START -->
Ici nous avons effectué des traitements en ligne pour mesurer les statistiques d'utilisation des stations en temps réel. Pour ce fait, nous avons connecté Spark Streaming à Kafka et calculer la moyenne pour chaque station disponible : 
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
- Faire un modèle qui prédire si une station sera remplie à un instant tt en fonction du nombre de place disponibles
<!-- BLOG-POST-LIST:END -->


## Pour lancer le projet 
<!-- BLOG-POST-LIST:START -->
Il faut :
- Installer kafka : https://kafka.apache.org/quickstart
- Installer Spark ansi que ses dependencies
- Lancer le server kafka : bin/kafka-server-start.sh config/server.properties
- Lancer Zookeeper : bin/zookeeper-server-start.sh config/zookeeper.properties
<!-- BLOG-POST-LIST:END -->

## DEMOS
<!-- BLOG-POST-LIST:START -->

<img align="center" src="/Images/collecte_envoi_des_données.PNG"/>
<br/>

<img align="center" src="/Images/consumer_velib.PNG"/>
<br/>

<img align="center" src="/Images/average_type_of_bike.PNG"/>
<br/>

<img align="center" src="/Images/average_bike_available_calculate_every_3min.PNG"/>
<br/>

<img align="center" src="/Images/avg_zone_type_bike.PNG"/>
<br/>

<img align="center" src="/Images/avg_bike_available_in_specific_zone_3min.PNG"/>
<br/>


<!-- BLOG-POST-LIST:END -->

## BILAN
<!-- BLOG-POST-LIST:START -->
Dans l'ensemble, je suis satisfait de la mise en place de ce projet. Voici quelques éléments clés de mon bilan personnel :

- Réalisation des objectifs :
J'ai réussi à atteindre les objectifs que je m'étais fixés pour le projet.

- Apprentissages : 
La mise en place de ce projet m'a appris beaucoup de choses sur l'environnement kafka, spark, la programmation python, l'utilisation d'une base de donnée nosql, l'analyse des données et la mise en place de modèle de machine avec sparkml. Je suis heureuse d'avoir acquis de nouvelles compétences.

- Points à améliorer : Bien que le projet ait été un succès, je pense qu'il y a toujours des points à améliorer. Par exemple, je pourrais travailler sur l'automatisation des taches avec Airflow.

- Prochaines étapes : Utilisation des DAGs pour construire des pipelines de traitement de données robustes et résilients.

En somme, la mise en place de ce projet a été une expérience positive pour moi. Je suis fier du travail accompli et j'ai hâte de voir où cela va me mener dans le futur.

<!-- BLOG-POST-LIST:END -->
