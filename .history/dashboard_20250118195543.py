from dash import Dash, html, dcc, ctx, callback, Input, Output
from piechart import PieChart
from accueil import Accueil
from tornado import Tornado
from earthquake import Earthquake

class DashBoard:
    """
    Tableau de bord des données sur les catastrophes naturelles
    """
    def __init__(self):
        """
        Initialisation du Dashboard en implémentant une carte et les deux histogrammes
        """

    def createDashApplication(self):
        """
        Création de l'application pour afficher les données concernant les catastrophes naturelles

        Retourne:
            Dash : Objet qui représente l'application Dashboard
        """
        self.app = Dash(__name__)

        self.app.layout = html.Div(
            className='App',
            id='app-container',
            children=[
                html.Nav(
                    className='wrapper',
                    children=[
                        html.Div(
                            children=[
                                html.Button(
                                    'Accueil',
                                    id='accueil',
                                ),
                                html.Button(
                                    'Tornado',
                                    id='tornado',
                                ),
                            ]
                        ),
                        html.Img(
                            src=r'img/logo_black.png',
                            className='logo-navbar',
                        ),
                        html.Div(
                            className='right',
                            children=[
                                html.Button(
                                    'Earthquake',
                                    id='earthquake',
                                ),
                                html.Button(
                                    'Earthquakes',
                                    id='earthquakes',
                                ),
                            ]
                        ),
                    ]
                ),
                html.Div(id='app_output'),
            ]
        )

        # fichier CSS
        self.app.css.append_css({'external_url': '/assets/style.css'})

        return self.app

    @callback(
        Output('app_output', 'children'),
        Input('accueil', 'n_clicks'),
        Input('tornado', 'n_clicks'),
        Input('earthquake', 'n_clicks'),
        Input('earthquakes', 'n_clicks'),
    )

    def switch_page(btn1, btn2, btn3, btn4) :
        layout = html.Div(Accueil().get_layout())
        if 'accueil' == ctx.triggered_id :
            layout = html.Div(Accueil().get_layout())
        elif 'tornado' == ctx.triggered_id :
            layout = html.Div(Tornado().get_layout())
        elif 'earthquake' == ctx.triggered_id :
            layout = html.Div(Earthquake().get_layout())
        elif 'earthquakes' == ctx.triggered_id :
            layout = html.Div(Earthquake().get_layout())
        return layout
