# TP Hadoop
 
## Objectif

Sujet : Analyse des tendances musicales de Spotify

Ce projet utilise Hadoop Streaming pour analyser les données Spotify via MapReduce. Les résultats sont ensuite 
- visualisés à l'aide de Matplotlib 
- stockés dans HBase.

### Fichiers inclus
- `mapper.py` : Job MapReduce Mapper
- `reducer.py` : Job MapReduce Reducer
- `Spotify_Most_Streamed_Songs.csv` : Dataset source
- `Rapport-TP-Hadoop.docx` : Rapport complet

### Évaluateur du TP
 - Centre de formation : DIGINAMIC
 - Promotion : 2025-D04-07 / Section Data Engineer
 - Formatrice : Madame Amina MARIE
 - GitHub Repository : https://github.com/AminaMarie

## Configuration de Git Repository
* Fichier "./gitignore"

## Liste de fichiers et de dossiers exclus
* Exclure le fichier .gitignore lui-même
.gitignore

* Exclure les dossiers du projet
archives/
dataset/
modele/
streaming/
documents/

* Exclure les fichiers temporaires ou sensibles
 *.log
 *.tmp
 *.bak
 *.swp

* Exclure les fichiers système
 .DS_Store
 Thumbs.db

* Exclure les fichiers Python compilés
 __pycache__/
 *.pyc


* Commit
git add .
git commit -m "Ajout des livrables du TP Hadoop : " -m " - Scripts du Job MapReduce (mapper.py & reduce.py)" -m " - Dataset" -m " - Rapport Docx"


## Configuration de GitHub Repository

1. Création du GitHub Repository : https://github.com/PhilippeVita/Hadoop
    Ne cocher aucune option : 
    - README
    - Licence
    - .gitignore

2. Lier le Git Repository au GitHub Repository : 
    - HTTPS : git remote add origin https://github.com/PhilippeVita/Hadoop.git

3. Pousser les commits locaux sur GitHub : 
    - GitHub : git push -u origin main

4. Inviter les collaborateurs du TP : 
    - AminaMarie (Amina MARIE), Robin HOTTON
    - Nour1990 (Nour ZERABIB)
