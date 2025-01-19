import pandas as pd
import plotly.express as plt

class Histogram:
    """
    Cette classe permet de créer un histogramme qui affiche les statistiques des données en argument

    Attributs :
        hist : Affichage graphique des données des catastrophes
        data : Données des catastrophes

    Méthodes :
        __init__(self, filename, x_param, y_param, filter_color) : Initialise l'objet Histogram
        get_histogram(self) : Renvoie l'objet graphique
    """

    def __init__(self, filename, x_param, y_param, filter_color):
        """
        Initialise un histogramme depuis les données du fichier donné et les paramètres choisis

        :param filename : nom du fichier dans lequel rechercher les données
                x_param : Paramètre d'abscisse de l'histogramme
                y_param : Paramètre d'ordonnée de l'histogramme
                filter_color : filtre permettant de différencier avec de la couleur un paramètre supplémentaire
        """
        # Récupération des données en lisant le fichier csv correspondant
        self.data = pd.read_csv('data/cleaned/' + filename, delimiter=',')

        # Création de l'histogramme utilisant plotly express avec les données précisées
        self.hist = plt.histogram(self.data, x=x_param, y=y_param, color=filter_color, nbins=20)

        # Mise en page de l'histogramme
        self.hist.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor='rgba(0,0,0,0)'
        )

    def get_histogram(self):
        """
        Renvoie l'affichage graphique de l'histogramme créé
        """
        return self.hist
