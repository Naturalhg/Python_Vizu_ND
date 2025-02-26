from dash import html, dcc
from dashboard.components.piechart import PieChart
from dashboard.components.histogram import Histogram

class Tornado:
    """
    Tableau de bord des données sur les tornades

    Attributs :
        GenHistogram = Instance de la classe Histogram qui permet l'affichage de l'histogramme général des tornades les plus dangereuses en fonction de leur magnitude
        CurPiechart = Instance de la classe PieChart qui permet l'affichage du pichart de la fréquence d'apparition des tornades par magnitude
        YearHistogram = Instance de la classe Histogram qui permet l'affichage de l'histogramme des pertes monétaires chaque année par magnitude des tornades
        MagHistogram = Instance de la classe Histogram qui permet l'affichage de l'histogramme de la fréquence de magnitude des tornades par an
    """
    def __init__(self):
        """
        Initialisation de l'affichage en implémentant un diagramme circulaire et trois histogrames
        """
        self.GenHistogram = Histogram('tornados.csv', 'mag', 'loss', None)
        self.CurPiechart = PieChart('tornados.csv', None, 'mag')
        self.YearHistogram = Histogram('tornados.csv', 'yr', 'loss', 'mag')
        self.MagHistogram = Histogram('tornados.csv', 'yr', 'mag', 'mag')

    def get_layout(self):
        """
        Changement du layout de l'application

        Retourne:
            html.Div : Une division html de l'application concernant les tornades
        """

        self.layout = html.Div(
            children=[
                html.Div(
                    className='texts',
                    children=[
                        html.H1('Impact des tornades aux États-Unis'),
                        html.P("On voit que les tornades touchent principalement les États-Unis et font perdre beaucoup d'argent et d'informations à ce pays chaque année."),
                        html.P('Grâce aux histogrammes et au diagramme circulaire ci-dessous, on comprend que les tornades les plus courantes sont celles de magnitude 0 et 1 qui représentent 80% des tornades mais seulement 14% des pertes totales.'),
                        html.P("On remarque également qu'une tornade à magnitude élevée est forcément synonyme de dégâts plus importants, sûrement parce que cela signifie qu'elle va parcourir une plus grande distance avant de s'arrêter."),
                    ]
                ),
                html.Div(
                    className='wrapper graph',
                    children=[
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H3('Pertes monétaires en fonction de la magnitude des tornades'),
                                dcc.Graph(figure=self.GenHistogram.get_histogram()),
                            ]
                        ),
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H3("Fréquence des tornades en fonction de leur magnitude"),
                                dcc.Graph(figure=self.CurPiechart.get_piechart()),
                            ]
                        ),
                    ]
                ),
                html.Div(
                    className='texts',
                    children=[
                        html.H1('Détails sur le temps'),
                        html.P('Au fil des années, en fonction de la magnitude des tornades, on se rend compte que les pertes sont difficiles à minimiser et les dégâts restent toujours très voire plus conséquents.'),
                        html.P('Par exemple, en 1974, un total de 3 milliards de dollars ont été perdus pour une somme de 1236 des magnitudes des tornades. Par contre, en 2019, 3 milliards de dollars ont été perdus pour un cumul de 876 des magnitudes des tornades.'),
                        html.P("Le même phénomène se produit en 2011 car 10 milliards de dollars sont perdus avec un total des magnitudes de 1288, alors qu'en 1973, seulement 1.2 milliards sont perdus pour une somme de 1369 des magnitudes.")
                    ]
                ),
                html.Div(
                    className='wrapper graph',
                    children=[
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H2("Pertes monétaires par année en fonction de leur magnitude"),
                                dcc.Graph(figure=self.YearHistogram.get_histogram()),
                            ]
                        ),
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H2('Total des magnitudes des tornades par an'),
                                dcc.Graph(figure=self.MagHistogram.get_histogram()),
                            ]
                        ),
                    ]
                ),
            ]
        ),

        return self.layout
