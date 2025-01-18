import pandas as pd

# Charger les fichiers
disasters_file = './data/All_Natural_Disasters.csv'
coordinates_file = './data/country-coordinates-world.csv'

# Lire les données en DataFrames
disasters_df = pd.read_csv(disasters_file)
coordinates_df = pd.read_csv(coordinates_file)


# Fusionner les deux fichiers sur la colonne 'Country'
# (adapter le nom de la colonne si nécessaire dans vos fichiers)
merged_df = pd.merge(disasters_df, coordinates_df, how='left', left_on='Country', right_on='Country')

# Sauvegarder dans un nouveau fichier
output_file = './data/All_Natural_Disasters_with_Coordinates.csv'
merged_df.to_csv(output_file, index=False)

