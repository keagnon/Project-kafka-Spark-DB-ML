# Projet-Big-data-et-Dataviz
L'objectif de ce projet est de mettre en place un système de traitement de données pour la métrople de Paris pour augmenter l'usage de son service de vélos partagés (vélib) et améliorer l’expérience de ses abonnements.


Ce repository héberge notre travail effectué lors d'un projet de notre majeure Big Data et Dataviz.

Il se compose de fichiers .ipynb de data cleaning, de fichiers .py pour le code python, de fichiers .csv et .xls qui étaient nos sources de données ainsi qu'une base de données NoSQL MongoDB.

Suivant les différentes parties de notre projet : partie 1 : Récupération des données (nous avons scrapés les données d'une APi ensuite Créer un producer kafka qui envoi les données reçu sur une instance Kafka toute les minutes); partie 2 : Traitement en ligne (nous avons connecté Spark Streaming à Kafka pour faire des calculs statistiques); partie 3 : Traitement par batch ( avoir des statistiques d'utilisation à plus long terme) et la partie 4 : Machine learning (avec Spark ml, nous avons fait un modèle qui aura pour but de prédire si une station sera remplie à un instant tt en fonction du nombre de place disponibles )

https://www.odoo.com/forum/help-1/how-to-install-pip-in-python-3-on-ubuntu-18-04-167715
https://www.atlassian.com/git/tutorials/git-ssh


Laisser tourner pendant 1h pour récuperer les données des stations