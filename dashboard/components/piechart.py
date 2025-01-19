import pandas as pd
import plotly.express as plt

class PieChart:
    """
    Cette classe permet de créer un diagramme circulaire qui affiche les statistiques en pourcentages des données en argument

    Attributs :
        pie : Affichage graphique des données des catastrophes
        data : Données des catastrophes

    Méthodes :
        __init__(self, filename, value, name) : Initialise l'objet PieChart
        get_piechart(self) : Renvoie l'objet graphique
    """

    def __init__(self, filename, value, name):
        """
        Initialise un histogramme depuis les données du fichier donné et les paramètres choisis

        :param filename : nom du fichier dans lequel rechercher les données
                value : Premier paramètre du piechart
                name : Second paramètre du piechart
        """
        # Récupération des données en lisant le fichier csv correspondant
        self.data = pd.read_csv('data/' + filename, delimiter=',')

        # Création du piechart à l'aide des données en argument
        self.pie = plt.pie(self.data, values=value, names=name, hole=0.3)

        # Mise en page extérieure du piechart
        self.pie.update_layout(
            margin=dict(l=5, r=5, t=5, b=30),
            paper_bgcolor='rgba(0,0,0,0)',
            uniformtext_minsize=8,
            uniformtext_mode='hide'
        )

        # Mise en page des données propres au piechart
        self.pie.update_traces(textposition='inside', textinfo='percent+label', textfont_size=20,
                            marker=dict(line=dict(color='#000000', width=2)))

    def get_piechart(self):
        """
        Renvoie l'affichage graphique du pichart créé
        """
        return self.pie
