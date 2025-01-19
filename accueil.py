from dash import Dash, html, dcc
from piechart import PieChart
from histogram import Histogram

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
        #faire map
        self.DeathPiechart = PieChart('All_Natural_Disasters.csv', 'Total Deaths', 'Disaster Type')
        self.LossPiechart = PieChart('All_Natural_Disasters.csv', 'Total Damage (USD, original)', 'Disaster Type')
        self.DeathHistogram = Histogram('All_Natural_Disasters.csv', 'Year', 'Total Deaths', None)
        self.LossHistogram = Histogram('All_Natural_Disasters.csv', 'Year', 'Total Damage (USD, original)', None)
        #faire histo avec détails argent original et estimé

    def get_layout(self):
        """
        Changement du layout de l'application

        Retourne:
            Div : Div html de l'application concernant l'accueil
        """

        self.layout = html.Div(
            children=[
                html.Div(
                    className='texts',
                    children=[
                        html.H1('Impact des catastrophes naturelles dans le monde'),
                    ]
                ),
                html.Div(
                    className='wrapper graph',
                    children=[
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H3('Nombre de morts en fonction de la catastrophe'),
                                dcc.Graph(figure=self.DeathPiechart.get_piechart()),
                            ]
                        ),
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H3("Total monétaire perdu en fonction de la catastrophe"),
                                dcc.Graph(figure=self.LossPiechart.get_piechart()),
                            ]
                        ),
                    ]
                ),
                html.Div(
                    className='texts',
                    children=[
                        html.H1('Détails sur le temps'),
                        html.P('Au fil des années, en fonction de la magnétude des tornades, on se rend compte que les pertes sont difficiles à minimiser et les dégâts restent toujours très voire plus conséquents.'),
                        html.P('Par exemple, en 1974, un total de 3 milliards de dollars ont été perdus pour une somme de 1236 des magnétudes des tornades. Par contre, en 2019, 3 milliards de dollars ont été perdus pour un cumul de 876 des magnétudes des tornades.'),
                        html.P("Le même phénomène se produit en 2011 car 10 milliards de dollars sont perdus avec un total des magnétudes de 1288, alors qu'en 1973, seulement 1.2 milliards sont perdus pour une somme de 1369 des magnétudes.")
                    ]
                ),
                html.Div(
                    className='wrapper graph',
                    children=[
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H2("Nombre de morts par année en fonction de l'échelle de richter"),
                                dcc.Graph(figure=self.DeathHistogram.get_histogram()),
                            ]
                        ),
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H2('Total de la puissance des séismes par an'),
                                dcc.Graph(figure=self.LossHistogram.get_histogram()),
                            ]
                        ),
                    ]
                ),
            ]
        ),

        return self.layout
