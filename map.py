import pandas as pd
import folium
import numpy as np

class NaturalDisasterMap:
    """
    Cette classe permet de créer une carte géographique qui représente les catastrophes naturelles
    par localisation, en utilisant les données enrichies avec des coordonnées.

    Attributs :
        centre_lat (float) : Latitude du centre de la carte.
        centre_lon (float) : Longitude du centre de la carte.
        map_bounds (list) : Coordonnées max de la carte.
        m (folium.Map) : Carte folium pour les visualisations.
    """
    def __init__(self, disaster_data_path):
        """
        Initialise la carte avec les données des catastrophes naturelles enrichies.

        :param disaster_data_path: Chemin vers le fichier CSV contenant les données enrichies.
        """
        self.df = pd.read_csv(disaster_data_path)
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

        self.m = folium.Map(location=[self.centre_lat, self.centre_lon], zoom_start=2,
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
                           f"Nombre total de catastrophes: {row['Disaster Count']}\n" \
                           f"Date: {row['Date']}" if 'Date' in row else ''

            folium.CircleMarker(
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

