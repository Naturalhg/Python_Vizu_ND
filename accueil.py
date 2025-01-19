from dash import html, dcc
from piechart import PieChart
from histogram import Histogram
from map import Map

class Accueil:
    """
    Tableau de bord des données sur les catastrophes naturelles

    Attributs :
        GenMap = Instance de la classe Map qui permet l'affichage d'une carte générale sur la fréquence d'apparition des catastrophes naturelles
        CurPiechart = Instance de la classe PieChart qui permet l'affichage d'un pichart général sur les fréquences d'apparition des catastrophes naturelles
        LossPiechart = Instance de la classe PieChart qui permet l'affichage d'un pichart sur les pertes monétaires des catastrophes naturelles
        DeathPiechart = Instance de la classe PieChart qui permet l'affichage d'un pichart sur le nombre de morts par catastrophes naturelles
        DeathHistogram = Instance de la classe Histogram qui permet l'affichage d'un histogramme sur le nombre de morts par an par pays des catastrophes naturelles

    Méthodes :
        __init__(self) : Initialise l'objet Accueil
        get_layout(self) : Récupère toutes les données et la mise en page concernant la page d'accueil
    """
    def __init__(self):
        """
        Initialisation de l'affichage en implémentant une carte, des diagrammes circulaires et un histogramme
        """
        self.GenMap = Map('All_Natural_Disasters_with_Coordinates.csv')
        self.CurPiechart = PieChart('All_Natural_Disasters.csv', 'Total Events', 'Disaster Type')
        self.LossPiechart = PieChart('All_Natural_Disasters.csv', 'Total Damage (USD, original)', 'Disaster Type')
        self.DeathPiechart = PieChart('All_Natural_Disasters.csv', 'Total Deaths', 'Disaster Type')
        self.DeathHistogram = Histogram('All_Natural_Disasters.csv', 'ISO', 'Total Deaths', 'Disaster Type')

    def get_layout(self):
        """
        Changement du layout de l'application

        Retourne:
            html.Div : Une division html de l'application concernant l'accueil
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
                                html.H3('Fréquence des catastrophes dans le monde entier'),
                                dcc.Graph(figure=self.CurPiechart.get_piechart()),
                            ]
                        ),
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H3("Carte des catastrophes naturelles dans le monde"),
                                html.Iframe(srcDoc=self.GenMap.get_map().get_root().render())
                            ]
                        ),
                    ]
                ),
                html.Div(
                    className='texts',
                    children=[
                        html.H1('Détails sur la mortalité')
                    ]
                ),
                html.Div(
                    className='wrapper graph',
                    children=[
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H2("Nombre de morts pour chaque catastrophe"),
                                dcc.Graph(figure=self.DeathPiechart.get_piechart()),
                            ]
                        ),
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H2('Détail du nombre de morts par an pour chaque catastrophe'),
                                dcc.Graph(figure=self.DeathHistogram.get_histogram()),
                            ]
                        ),
                    ]
                ),
            ]
        ),

        return self.layout
