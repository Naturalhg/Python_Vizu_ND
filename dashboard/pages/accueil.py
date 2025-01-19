from dash import html, dcc, callback, Input, Output
from dashboard.components.piechart import PieChart
from dashboard.components.histogram import Histogram
from dashboard.components.map import Map
import plotly.express as plt

class Accueil:
    """
    Tableau de bord des données sur les catastrophes naturelles

    Attributs :
        GenMap = Instance de la classe Map qui permet l'affichage d'une carte générale sur la fréquence d'apparition des catastrophes naturelles
        CurPiechart = Instance de la classe PieChart qui permet l'affichage d'un pichart général sur les fréquences d'apparition des catastrophes naturelles
        LossPiechart = Instance de la classe PieChart qui permet l'affichage d'un pichart sur les pertes monétaires des catastrophes naturelles
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
                        html.H1('Détails des pertes')
                    ]
                ),
                html.Div(
                    className='wrapper graph',
                    children=[
                        html.Div(
                            className='wrapper-2-part',
                            children=[
                                html.H2("Pertes pour chaque catastrophe"),
                                dcc.Graph(id='DeathPiechart'),
                                html.P("Pertes :"),
                                dcc.Dropdown(id='loss',
                                    options=['Total Deaths', 'Total Damage (USD, original)', 'Total Damage (USD, adjusted)'],
                                    value='Total Deaths'
                                ),
                                html.P("Type :"),
                                dcc.Dropdown(id='type',
                                    options=['Disaster Type', 'Disaster Subgroup', 'Disaster Subtype'],
                                    value='Disaster Type'
                                ),
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

    @callback(
        # ID de sortie pour afficher la figure du piechart
        Output("DeathPiechart", "figure"),
        # IDS des valeurs du piechart
        Input("loss", "value"),
        Input("type", "value")
    )

    def generate_chart(names, values):
        """
        Créer le diagramme circulaire interactif concernant les catastrophes naturelles

        param: names: premier paramètre du diagramme circulaire
                values: second paramètre du diagramme circulaire

        Retourne:
            PieChart : Un piechart qui s'actualise en fonction des choix de l'utilisateur
        """
        pie = PieChart('All_Natural_Disasters.csv', names, values)
        return pie.get_piechart()
