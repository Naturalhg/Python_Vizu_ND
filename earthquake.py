from dash import Dash, html, dcc
from piechart import PieChart
from tornado import Tornado

class Earthquake:
    """
    Tableau de bord des données sur les catastrophes naturelles

    Attributs :
        SubPiechart = Instance de la classe PieChart qui permet l'affichage d'un pichart général des catastrophes naturelles
    """
    def __init__(self):
        """
        Initialisation de l'affichage en implémentant un piechart
        """
        self.SubPiechart = PieChart('Total Deaths', 'Disaster Subgroup')

    def get_layout(self):
        """
        Changement du layout de l'application

        Retourne:
            Div : Div html de l'application concernant les séïsmes
        """

        self.layout = html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                dcc.Graph(figure=self.SubPiechart.get_piechart())
                            ]
                        ),
                    ]
                ),
            ]
        )

        return self.layout