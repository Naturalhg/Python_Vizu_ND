import pandas as pd
import folium as fl
import numpy as np

class Map:
    """
    Cette classe permet de créer une carte géographique qui représente les catastrophes naturelles
    par localisation, en utilisant les données enrichies avec des coordonnées.

    Attributs :
        df : Données filtrées
        centre_lat (float) : Latitude du centre de la carte.
        centre_lon (float) : Longitude du centre de la carte.
        map_bounds (list) : Coordonnées max de la carte.
        m (folium.Map) : Carte folium pour les visualisations.

    Méthodes :
        __init__(self, disaster_data_path) : Initialise l'objet Map
        add_markers(self) : Implémente les cercles sur la carte
        get_map(self) : Renvoie l'objet graphique
        genCoords(self, disaster_data_path) : Crée un fichier CSV avec des coordonnées utilisables
    """

    def __init__(self, disaster_data_path):
        """
        Initialise la carte avec les données des catastrophes naturelles enrichies.

        :param disaster_data_path: Chemin vers le fichier CSV contenant les données enrichies.
        """
        self.genCoords('data/cleaned/' + disaster_data_path)

        self.df = pd.read_csv('data/cleaned/' + disaster_data_path)
        self.df = self.df.dropna(subset=['latitude', 'longitude'])

        # Calculer le nombre de catastrophes par pays
        self.df['Country'] = self.df['Country'].fillna('Unknown')
        self.country_counts = self.df.groupby('Country').size().reset_index(name='Disaster Count')
        self.df = pd.merge(self.df, self.country_counts, on='Country', how='left')

        # Définir le centre de la carte (moyenne des latitudes et longitudes)
        self.centre_lat = self.df['latitude'].mean()
        self.centre_lon = self.df['longitude'].mean()

        self.map_bounds = [[self.df['latitude'].min(), self.df['longitude'].min()],
                           [self.df['latitude'].max(), self.df['longitude'].max()]]

        self.m = fl.Map(location=[self.centre_lat, self.centre_lon], zoom_start=2,
                            max_bounds=True)

        self.add_markers()

    def add_markers(self):
        """
        Ajoute des cercles représentant les catastrophes naturelles sur la carte.
        """
        for _, row in self.df.iterrows():
            # Rayon basé sur le nombre de catastrophes dans le pays
            radius = np.log1p(row['Disaster Count']) * 2  # Ajustement dynamique

            # Couleur du cercle selon le type de catastrophe
            disaster_type = row['Disaster Type'] if 'Disaster Type' in row else 'Unknown'
            color = {
                'Earthquake': 'red',
                'Flood': 'blue',
                'Storm': 'green',
                'Wildfire': 'orange',
                'Unknown': 'gray'
            }.get(disaster_type, 'gray')

            # Texte info-bulle
            tooltip_text = f"{disaster_type} - {row['Country']}\n" \
                           f"Nombre total de catastrophes: {row['Disaster Count']}"

            fl.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=radius,
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.7,
                tooltip=tooltip_text
            ).add_to(self.m)

    def get_map(self):
        """
        Retourne la carte avec les marqueurs ajoutés.
        """
        return self.m

    def genCoords(self, disaster_data_path):
        """
        Crée un fichier CSV depuis deux fichiers de coordonées

        :param disaster_data_path: Chemin vers le fichier CSV à créer.
        """
        # Charger les fichiers
        disasters_file = './data/cleaned/All_Natural_Disasters.csv'
        coordinates_file = './data/cleaned/country-coordinates-world.csv'

        # Lire les données en DataFrames
        disasters_df = pd.read_csv(disasters_file)
        coordinates_df = pd.read_csv(coordinates_file)


        # Fusionner les deux fichiers sur la colonne 'Country'
        # (adapter le nom de la colonne si nécessaire dans vos fichiers)
        merged_df = pd.merge(disasters_df, coordinates_df, how='left', left_on='Country', right_on='Country')

        # Sauvegarder dans un nouveau fichier
        merged_df.to_csv(disaster_data_path, index=False)
        print(disaster_data_path+ " CAAAA")
