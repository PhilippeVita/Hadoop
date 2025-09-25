#!/usr/bin/env python3
import sys, csv


reader = csv.DictReader(sys.stdin)              # Lecture du fichier Spotify

for row in reader:
        try:
                d = row.get('danceability_%')   # Récupération de 'danceability_%'
                e = row.get('energy_%')         # Récupération de 'energy'
                s = row.get('streams')          # Récupération de 'streams'
                d = int(float(d))               # Conversion
                e = int(float(e))
                s = int(s)
                print(d,"\t", e , "\t",s) 
        except Exception:
            
            # Ignorer les lignes invalides
                continue