import pandas as pd
import plotly.express as plt

class PieChart:
    """
    Cette classe représente un pie chart qui affiche les statistiques en pourcentages de la proportion d

    Attributs :
        isSecondDash (bool) : Indique la deuxième partie du dashboard ( partie des graphes )
        data : Contient les données des doses n°1 du Covid-19
        filtered_data : Filtrage des données
        columnFilter (str) : Nom de la colonne dans la date filtrée
        forDisplayY (str) : Axe des ordonnées dans le graphique
        forDisplayX (str) : Axe des abscisse dans le graphique
        colorDash (str) : Couleur des barres dans le graphique

    Méthodes :
        __init__(self, isSecondDash) : Initialise l'objet PieChart
        get_dash(self) : Renvoie l'objet graphique
    """
    def __init__(self, value, name):
        self.df = pd.read_csv('data/All_Natural_Disasters.csv', delimiter=',')
        print(self.df)

        #self.filtered_data = self.data[self.data['Valeur de la variable'] != 0]
        #self.grouped_data = self.filtered_data.groupby((self.filtered_data['Valeur de la variable'] // 10) * 10)["Parité d'apparition des catastrophes"].sum().reset_index()
        #self.average_disaster = self.grouped_data["disaster"].sum()
        self.fig = plt.pie(self.df, values=value, names=name, hole=0.3)
        '''self.fig.update_traces(texttemplate='%{y:f}%', textposition='outside')'''
        self.fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor='rgba(0,0,0,0)'
        )

    def get_piechart(self):
        return self.fig
