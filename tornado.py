from dash import Dash, html, dcc
from map import Map
from histogram import Histogram
from piechart import PieChart

class Tornado:
    """
    Tableau de bord des données sur les catastrophes naturelles

    Attributs :
        GenPiechart = Instance de la classe PieChart qui permet l'affichage du pichart général des catastrophes naturelles
    """
    def __init__(self):
        """
        Initialisation de l'affichage en implémentant un piechart
        """
        self.GenPiechart = PieChart('Total Deaths', 'Disaster Type')

    def get_layout(self):
        """
        Changement du layout de l'application

        Retourne:
            Div : Div html de l'application concernant les tornades
        """

        self.layout = html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                dcc.Graph(figure=self.GenPiechart.get_piechart(),
                                          style={'width':'50%'})
                            ]
                        ),
                    ]
                ),
            ]
        )

        return self.layout
