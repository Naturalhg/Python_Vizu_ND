import pandas as pd
import plotly.express as plt

class PieChart:
    """
    Cette classe représente un pie chart qui affiche les statistiques en pourcentages de la proportion d

    Attributs :
        fig : Affichage graphique des données des catastrophes
        df : Données filtrées des catastrophes
        filename : nom du fichier dans lequel rechercher les données
        value : nom du premier paramètre à sélectionner dans les données
        name : nom du second paramètre à sélectionner dans les données

    Méthodes :
        __init__(self, value, name) : Initialise l'objet PieChart
        get_piechart(self) : Renvoie l'objet graphique
    """
    def __init__(self, filename, value, name):
        self.df = pd.read_csv('data/cleaned/' + filename, delimiter=',')
        self.fig = plt.pie(self.df, values=value, names=name, hole=0.3)
        self.fig.update_layout(
            margin=dict(l=5, r=5, t=5, b=30),
            paper_bgcolor='rgba(0,0,0,0)',
            uniformtext_minsize=8,
            uniformtext_mode='hide'
        )
        self.fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=20,
                            marker=dict(line=dict(color='#000000', width=2)))

    def get_piechart(self):
        return self.fig
