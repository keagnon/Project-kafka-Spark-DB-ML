### Projet Big data et Dataviz : Mise en place d'un système de traitement des vélos partagés (vélib) 

Ce repository héberge notre travail effectué lors d'un projet de notre majeure Big Data et Dataviz.

L'objectif de ce projet est de mettre en place un système de traitement de données pour la métrople de Paris pour augmenter l'usage de son service de vélos partagés (vélib) et améliorer l’expérience de ses abonnements.

Il se compose de fichiers .ipynb de data cleaning, de fichiers .py pour le code python, de fichiers .csv  qui étaient nos sources de données ainsi qu'une base de données NoSQL MongoDB.

<img align="left" src="/Images/station_velib.jpg"/ style="margin-bottom:2rem">
<br/>

# Mise en place du projet
<!-- BLOG-POST-LIST:START -->
Notre projet comprend 4 grandes parties :
## partie 1 : Récupération des données 
Nous avons scrapés les données d'une APi ensuite Créer un producer kafka qui envoi les données reçu sur une instance Kafka toute les minutes
<!-- BLOG-POST-LIST:END -->

## partie 2 : Traitement en ligne
<!-- BLOG-POST-LIST:START -->
gdg
<!-- BLOG-POST-LIST:END -->

## partie 3 : Traitement par batch
<!-- BLOG-POST-LIST:START -->
sgdshd
<!-- BLOG-POST-LIST:END -->

## partie 4 : Machine learning
<!-- BLOG-POST-LIST:START -->
tsry
<!-- BLOG-POST-LIST:END -->


partie 2 : Traitement en ligne (nous avons connecté Spark Streaming à Kafka pour faire des calculs statistiques); 
partie 3 : Traitement par batch ( avoir des statistiques d'utilisation à plus long terme)
la partie 4 : Machine learning (avec Spark ml, nous avons fait un modèle qui aura pour but de prédire si une station sera remplie à un instant tt en fonction du nombre de place disponibles )





