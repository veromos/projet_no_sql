README

Notre projet est composé de la partie mongoDb et Neo4j.

Le script « run.sh » à la racine du dossier « sources » permet de lancer les dockers et d’importer la base de données. L’importation se fera à tous les lancements étant donné que le fichier est régulièrement mis à jour.

Le script « search_by_geolocation.py » permet de lancer une recherche d’infraction dans un rayon carré autour des coordonnées donnés en paramètre. Par exemple on pourra appeler le script comme ça une fois entré dans le docker PYTHON avec cette commande :
-	docker exec -ti ESGI_PYTHON /bin/sh
Puis faire ceci :
-	python search_by_geolocation.py 39.150 -77.100 3
Nous avons ici 2 coordonnées 39.150 et -77.1, puis le chiffre 3 qui donne le rayon en kilomètre où le script ira chercher les infractions.


Le script « similitude.sh » permet de lancer la recherche d’infractions similaires en fonction de 3 champs de la table.
