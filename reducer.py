#!/usr/bin/env python3
import sys

current_key = None  
sum_streams = 0
count = 0

for line in sys.stdin:                      # Lecture du flux entrant
        line = line.strip()                 # Nettoyage des données brutes
        if not line:                        # Sauter la ligne vide
                continue
        d, e, s = line.split('\t')          # Récupérer 'danceability', 'energy', 'streams'
        key= d+"_"+e                        # Créer la clé : Pair ('danceability', 'energy')
        val = int(s)                        # Créer la valeur (streams)

        if current_key is None:             # Initialiser les clés et valeurs
                current_key = key
                sum_streams = val
                count = 1
                continue

        if key == current_key:              # Agrégation des données recueillies
                sum_streams += val
                count += 1
        else:
                avg = sum_streams / count if count else 0 # Fonction d'agrégation appliquée
                print(current_key,"\tsum=",sum_streams,"\tcount=",count,"\tavg=",avg)
                current_key = key 
                sum_streams = val
                count = 1

# Pour la dernière clé
if current_key is not None:                 # Si la clé courante n'est pas nulle
        avg = sum_streams / count if count else 0 
        print(current_key,"\tsum=",sum_streams,"\tcount=",count,"\tavg=",avg)