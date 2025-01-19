from dash import html, dcc
from dashboard.components.histogram import Histogram
from dashboard.components.piechart import PieChart

class Earthquake:
    """
    Tableau de bord des données sur les séïsmes

    Attributs :
        GenHistogram = Instance de la classe Histogram qui permet l'affichage de l'histogramme général des séïsmes les plus mortels en fonction de l'échelle de Richter
        CurPiechart = Instance de la classe PieChart qui permet l'affichage du pichart de la fréquence d'apparition des séïsmes sur l'échelle de Richter
        YearHistogram = Instance de la classe Histogram qui permet l'affichage de l'histogramme des morts chaque année des séïsmes en fonction de leur puissance
        RicHistogram = Instance de la classe Histogram qui permet l'affichage de l'histogramme des séïsmes par an sur l'échelle de Richter
    """
    def __init__(self):
        """
        Initialisation de l'affichage en implémentant un diagramme circulaire et trois histogrammes
        """
        self.GenHistogram = Histogram('earthquakes.csv', 'richter', 'deaths', None)
        self.CurPiechart = PieChart('earthquakes.csv', None, 'richter')
        self.YearHistogram = Histogram('earthquakes.csv', 'year', 'deaths', 'richter')
        self.RicHistogram = Histogram('earthquakes.csv', 'year', 'richter', None)

    def get_layout(self):
        """
        Changement du layout de l'application

        Retourne:
            html.Div : Une division html de l'application concernant les séïsmes
        """

        self.layout = html.Div(
            children=[
                html.Div(
                    className='texts',
                    children=[
                        html.H1('Impact des séïsmes sur le monde'),
                        html.P('On voit que les séïsmes touchent une grande partie du monde et tuent de nombreuses personnes chaque année.'),
                        html.P('Grâce aux histogrammes et au diagramme circulaire ci-dessous, on comprend que les séïsmes les plus mortels sont ceux de 7.3 à 8.2 de puissance mais que les séïsmes de puissance 7.3 à 7.7 sont très nombreux en comparaison.'),
                        html.P('En effet, ceux de puissance 7.8 à 8.2 représentent seulement 7% des séïsmes contrairement à ceux de 7.3 à 7.7 de puissance qui représentent plus de 33% des séïsmes.'),
                    ]
                ),
                html.Div(
                    className='wrapper graph',
                    children=[
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H3('Nombre de morts en fonction de la puissance des séïsmes'),
                                dcc.Graph(figure=self.GenHistogram.get_histogram()),
                            ]
                        ),
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H3("Fréquence des séïsmes en fonction de leur puissance"),
                                dcc.Graph(figure=self.CurPiechart.get_piechart()),
                            ]
                        ),
                    ]
                ),
                html.Div(
                    className='texts',
                    children=[
                        html.H1('Détails sur le temps'),
                        html.P('Au fil des années, en fonction de la puissance des séïsmes, on se rend compte que les chances de survie grandissent dèrnièrement.'),
                        html.P('Par exemple, dans les années 70, on recense 1 million de morts pour un cumul de 134 des puissances des séïsmes. Par contre, dans les années 90, un total de 100 000 morts pour une somme de 151 des puissances de richter sur les 10 ans.'),
                        html.P('On se rend également compte que les séïsmes les plus mortels ne sont pas les plus puissants, cela peut être dû à des raisons géographiques par exemple ou des systèmes de détection des séïsmes.'),
                    ]
                ),
                html.Div(
                    className='wrapper graph',
                    children=[
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H2("Nombre de morts par année en fonction de l'échelle de richter"),
                                dcc.Graph(figure=self.YearHistogram.get_histogram()),
                            ]
                        ),
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H2('Total de la puissance des séismes par an'),
                                dcc.Graph(figure=self.RicHistogram.get_histogram()),
                            ]
                        ),
                    ]
                ),
            ]
        ),

        return self.layout