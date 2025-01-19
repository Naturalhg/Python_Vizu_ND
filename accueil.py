from dash import Dash, html, dcc
from piechart import PieChart
from map import NaturalDisasterMap

class Accueil:
    """
    Tableau de bord des données sur les catastrophes naturelles

    Attributs :
        GenPiechart = Instance de la classe PieChart qui permet l'affichage d'un pichart général des catastrophes naturelles
        SubPiechart = Instance de la classe PieChart qui permet l'affichage d'un pichart général des catastrophes naturelles
    """
    def __init__(self):
        """
        Initialisation de l'affichage en implémentant deux piechart
        """
        self.GenPiechart = PieChart('Total Deaths', 'Disaster Type')
        self.SubPiechart = PieChart('Total Deaths', 'Disaster Subgroup')
        self.carte = NaturalDisasterMap('./data/All_Natural_Disasters_with_Coordinates.csv')

    def get_layout(self):
        """
        Changement du layout de l'application

        Retourne:
            Div : Div html de l'application concernant l'accueil
        """

        self.layout = html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Graph(figure=self.GenPiechart.get_piechart(),
                                    style={'width':'50%'})
                    ]
                ),
                html.Div(
                    children=[
                        html.Iframe(srcDoc=self.carte.get_map().get_root().render(), height='600px', width='1000px')
                    ]
                ),
                
            ]
        )

        return self.layout
