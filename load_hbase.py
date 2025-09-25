#!/usr/bin/env python3
import happybase

TABLE = 'tendance_music' # table Hbase


conn = happybase.Connection('node195233-hadoop-2025-d04-etudiant07.sh1.hidora.com',11667)	# Connexion au serveur HBase
conn.open()
table = conn.table(TABLE) # connection à la table


with open('part-00000', 'r') as f: # lecture du fichier de sortie 
	for line in f: 
		line = line.strip() # nettoyage
		if not line: 
			continue
		key, rest = line.split('\t', 1) # séparation de la clé et des valeurs
		# extraction des valeurs sum, count, avg
		fields = dict(item.split('=') for item in rest.split('\t'))
		total = int(float(fields['sum']))
		count = int(float(fields['count']))
		avg = float(fields['avg'])
		table.put(key, {
			b'data:total_streams': str(total).encode(),
			b'data:count': str(count).encode(),
			b'data:avg_streams': f"{avg:.2f}".encode(),
		}) # insertion dans la table HBase


print('Chargement terminé')