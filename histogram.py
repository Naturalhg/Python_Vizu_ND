import pandas as pd
import plotly.express as plt

class Histogram:
    """
    Cette classe représente un pie chart qui affiche les statistiques en pourcentages de la proportion d

    Attributs :
        fig : Affichage graphique des données des catastrophes
        df : Données filtrées des catastrophes
        filename : nom du fichier dans lequel rechercher les données
        x_param : Paramètre d'abscisse de l'histogramme
        y_param : Paramètre d'ordonnée de l'histogramme
        filter_color : filtre permettant de différencier avec de la couleur certains évènements

    Méthodes :
        __init__(self, value, name) : Initialise l'objet PieChart
        get_piechart(self) : Renvoie l'objet graphique
    """
    def __init__(self, filename, x_param, y_param, filter_color):
        self.df = pd.read_csv('data/cleaned/' + filename, delimiter=',')

        #self.filtered_data = self.data[self.data['Valeur de la variable'] != 0]
        #self.grouped_data = self.filtered_data.groupby((self.filtered_data['Valeur de la variable'] // 10) * 10)["Parité d'apparition des catastrophes"].sum().reset_index()
        #self.average_disaster = self.grouped_data["disaster"].sum()
        self.fig = plt.histogram(self.df, x=x_param, y=y_param, color=filter_color, nbins=20)
        self.fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor='rgba(0,0,0,0)'
        )
        '''
        self.fig = plt.pie(self.df, values=value, names=name, hole=0.3)
        #self.fig.update_traces(texttemplate='%{y:f}%', textposition='outside')
        self.fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor='rgba(0,0,0,0)'
        )'''

    def get_histogram(self):
        return self.fig
