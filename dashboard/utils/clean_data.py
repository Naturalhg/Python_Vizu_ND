import os
import pandas as pd

def clean_csv_files():
    # Définir les chemins des répertoires
    input_dir = "./data/raw/"
    output_dir = "./data/cleaned/"

    # Créer le répertoire de sortie s'il n'existe pas
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Liste des fichiers à traiter et des colonnes à supprimer
    files_to_clean = {
        "earthquakes.csv": [
            "month", "day", "area", "region"
        ],
        "All_Natural_Disasters.csv": [
            "Year", "Disaster Group", "Disaster Subgroup", "Disaster Subtype", 
            "Total Affected", "Total Damage (USD, adjusted)", "CPI"
        ],
        "country-coordinates-world.csv": [
        ],
        "tornados.csv": [
            "om","mo","dy","date","time","tz","datetime_utc","st","stf","inj","fat","slat","slon","elat","elon","len","wid","ns","sn","f1","f2","f3","f4","fc"
        ]

    }

    for file_name, columns_to_remove in files_to_clean.items():
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, file_name)

        try:
            # Charger le fichier CSV
            df = pd.read_csv(input_path)
            
            # Vérifier les colonnes à supprimer existantes
            existing_columns_to_remove = [col for col in columns_to_remove if col in df.columns]

            # Supprimer les colonnes spécifiées
            df_cleaned = df.drop(columns=existing_columns_to_remove)

            # Sauvegarder le fichier nettoyé
            df_cleaned.to_csv(output_path, index=False)

            print(f"Fichier nettoyé et sauvegardé : {output_path}")
        except FileNotFoundError:
            print(f"Le fichier n'existe pas : {input_path}")
        except Exception as e:
            print(f"Erreur lors du traitement du fichier {file_name} : {e}")
