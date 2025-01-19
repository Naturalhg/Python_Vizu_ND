# DashBoard Catastrophes Naturelles
---

L’objectif de notre projet est de proposer à l’utilisateur un accès a de nombreuses données concernant plusieurs types de catastrophes naturelles depuis 1900.

# User Guide

---

Voici le lien git qui vous permettra de télécharger les fichiers avant les différents étapes de configuration 

```bash

https://github.com/Naturalhg/Python_Vizu_ND/tree/main

```

Afin de manipuler dans de bonnes conditions l’outil d’analyse plusieurs étapes sont à suivre:

Tout d’abord, vous devez accéder localement sur votre machine aux différents fichiers composants.

```bash
git clone https://github.com/Naturalhg/Python_Vizu_ND.git   
```

Il est important dans un second temps de télécharger les différentes bibliothèques python       utilisées dans le projet.

```bash
python -m pip install -r requirements.txt
```
Enfin vous pouvez simplement exécuter le code grâce à la commande 

```bash
python main.py
```
N’oubliez pas qu’afin de visualiser les différents graphiques après exécution du code vous devez vous connecter à votre serveur local hébergeant le projet via votre navigateur, en entrant dans votre barre de recherche l’url.
```bash
http://127.0.0.1:8050/
```

# Data

---

- **All_Natural_Disasters** contient un grand volume de catastrophes naturelles s’étant produit depuis 1900. On y trouve essentiellement les dates lieux et types de catastrophes naturelles. Mais aussi les couts financiers et le nombre de morts provoqués par l’évènement. Lien de la source (Omdena) : https://datasets.omdena.com/dataset/natural-disasters-emergency-events-database---country-profiles
- **All_Natural_Disasters_with_Coordinates** est une version améliorée de “All natural Disasters” dans laquelle l’on trouve les colonnes essentiels de sa version mère mais aussi les coordonnées géographiques du pays d’origine de la catastrophe.
- **Earthquakes** contient les différents séismes s’étant produits depuis 1902 avec comme donnée importante la puissance sur l’échelle de Richter associé à l’évènement. Lien de la source (OpenIntro) : https://www.openintro.org/data/index.php?data=earthquakes
- **Tornados** contient les différentes tornades s’étant produites depuis 1950 en prenant en compte la puissance et les pertes de chacun d’entre eux. Lien de la source (Kaggle) : https://www.kaggle.com/datasets/sujaykapadnis/tornados
- **Country-coordinates-world** contient pour chaque pays du monde les coordonnées en longitude et latitude correspondantes. Il est utiliser dans le cadre de la concaténation avec “All_Natural_Disasters” pour formés le fichier “All_Natural_Disasters_with_Coordinates”

# Developer Guide

---

```
python_vizu_nd
|-- .𝗴𝗶𝘁𝗶𝗴𝗻𝗼𝗿𝗲
|-- 𝗱𝗮𝘁𝗮                                        
│   |-- cleaned
│   │   |-- all_natural_disasters.csv
│   |   |-- all_natural_disasters_with_coordinates.csv
|   |   |-- country-coordinates-world.csv
|   |   |-- earthaquakes.csv
|   |   |-- tornados.csv
│   |-- 𝗿𝗮𝘄
│       |-- all_natural_disasters.csv
│       |-- country-coordinates-world.csv
|       |-- earthquakes.csv
|       |-- tornados.csv
|-- 𝗺𝗮𝗶𝗻.𝗽𝘆                                     
|-- 𝗥𝗘𝗔𝗗𝗠𝗘.𝗺𝗱
|-- 𝗿𝗲𝗾𝘂𝗶𝗿𝗲𝗺𝗲𝗻𝘁𝘀.𝘁𝘅𝘁                              
|-- dashboard 
|   |-- components                              
|   |   |-- histogram.py
|   |   |-- map.py
|   |   |-- piechart.py
|   |-- pages                                  
|   |   |-- accueil.py
|   |   |-- dashboard.py
|   |   |-- earthquake.py
|   |   |-- assets
|   |   |   |-- logo_black.png
|   |   |   |-- logo_white.png
|   |   |   |-- style.css
|   |   |-- tornado.py
|   |-- 𝘂𝘁𝗶𝗹𝘀     
|   |   |-- clean_data.py
|-- video.mp4                                   
```

Nos fichiers sont organisés par classe. A chaque instanciation de classe un init met en place l’ensemble des paramètres il ne reste plus qu’a appeler un getter ainsi qu’une méthode d’affichage pour rendre les graphiques visibles.

La partie graphique du projet est organisée de sorte à refléter la structure du code en affichant les charts globaux de “All natural disasters”. Une seconde page affiche les charts associés aux Tremblements de terres et enfin un dernier ongle se concentre sur les Tornades.

# Rapport d’analyse

---

Les analyses effectuées concernent plusieurs types de catastrophes naturelles et implique plusieurs fichiers csv ciblant différentes unités. Toutefois il est important de prendre en compte que les graphiques ne sont pas fiables à 100% et qu’ils manquent parfois certaines données.

# Impact des séismes sur le monde

### Nombre de morts en fonction de la puissance des séismes & **Fréquence des séismes en fonction de leur puissance**

On voit que les séismes touchent une grande partie du monde et tuent de nombreuses personnes chaque année.

Grâce aux histogrammes et au diagramme circulaire , on comprend que les séismes les plus mortels sont ceux de 7.3 à 8.2 de puissance mais que les séismes de puissance 7.3 à 7.7 sont très nombreux en comparaison.

En effet, ceux de puissance 7.8 à 8.2 représentent seulement 7% des séismes contrairement à ceux de 7.3 à 7.7 de puissance qui représentent plus de 33% des séismes.

# Détails sur le temps

### Nombre de morts par année en fonction de l'échelle de Richter & Total de la puissance des séismes par an

Au fil des années, en fonction de la puissance des séismes, on se rend compte que les chances de survie grandissent dernièrement.

Par exemple, dans les années 70, on recense 1 million de morts pour un cumul de 134 des puissances des séismes. Par contre, dans les années 90, un total de 100 000 morts pour une somme de 151 des puissances de Richter sur les 10 ans.

On se rend également compte que les séismes les plus mortels ne sont pas les plus puissants, cela peut être dû à des raisons géographiques par exemple ou des systèmes de détection des séismes.

# Impact des tornades aux États-Unis

### Nombre de morts en fonction de la magnitude des tornades & **Fréquence des tornades en fonction de leur magnitude**

On voit que les tornades touchent principalement les États-Unis et font perdre beaucoup d'argent et d'informations à ce pays chaque année.

Grâce aux histogrammes et au diagramme circulaire, on comprend que les tornades les plus courantes sont celles de magnitude 0 et 1 qui représentent 80% des tornades mais seulement 14% des pertes totales.

On remarque également qu'une tornade à magnitude élevée est forcément synonyme de dégâts plus importants, sûrement parce que cela signifie qu'elle va parcourir une plus grande distance avant de s'arrêter.

# Détails sur le temps

### Nombre de morts par année en fonction de leur magnitude Total des magnitudes des tornades par an

Au fil des années, en fonction de la magnitude des tornades, on se rend compte que les pertes sont difficiles à minimiser et les dégâts restent toujours très voire plus conséquents.

Par exemple, en 1974, un total de 3 milliards de dollars ont été perdus pour une somme de 1236 des magnitudes des tornades. Par contre, en 2019, 3 milliards de dollars ont été perdus pour un cumul de 876 des magnitudes des tornades.

Le même phénomène se produit en 2011 car 10 milliards de dollars sont perdus avec un total des magnitudes de 1288, alors qu'en 1973, seulement 1.2 milliards sont perdus pour une somme de 1369 des magnitudes.

# Impact des catastrophes naturelles dans le monde

### Fréquence des catastrophes dans le monde entier & **Carte des catastrophes naturelles dans le monde**

Grâce au Piechart sur la fréquence des catastrophes naturelles et à la carte interactive des catastrophes depuis 1900, on peut distinguer que la plupart des évènements de ce type sont des inondations (près de 40%) ou encore des tempêtes (30.5%) suivi de loin par les tremblements de terre à 10%. 

On remarque que la plupart des inondations se déroulent en Afrique (coïncidence ?) . Quant aux tempêtes on en retrouver majoritairement en Europe ou en Asie de l’Est même si les résultats doivent être pris avec des pincettes étant donné l’imprécision parfois des coordonnées en corrélation avec les noms des pays.

# Détails sur la mortalité

## Nombre de morts pour chaque catastrophe & Détail du nombre de morts par an pour chaque catastrophe

Grâce au Pie Chart montrant  le pourcentage ainsi que le nombre de morts pour chaque catastrophe. On peut distinguer les évènement précisément et voir que la Sécheresse représente plus de la moitié des morts pour chaque catastrophe (environ 11 Millions de personnes) suivi par les Inondations à près de 30% (7 Millions de morts). On distingue une corrélation entre la fréquence de catastrophe et le nombre de morts assez facilement (excepté pour les tempêtes 6,5% de morts pour 30% des catastrophes).

On peut  grâce au Bar Chart remarquer que la chine est première de loin en terme de victimes de catastrophes naturelles avec environ 13 Millions de morts dont la moitié morts en raison d’inondations. L’inde est également très présente avec près de 5 Millions de morts majoritairement par inondations également. Le reste des pays se fond dans la masse.

# Copyright

Dans le cadre de notre projet nous avons utilisé une extension IA de chatGPT sur ide. Nous nous sommes également inspiré de la bibliothèque Plotly. De plus comme précisé précédemment nous avons apporté combiné deux fichiers csv pour en faire un global.
