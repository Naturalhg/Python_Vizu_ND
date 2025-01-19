from dash import Dash, html, ctx, callback, Input, Output
from dashboard.pages.accueil import Accueil
from dashboard.pages.tornado import Tornado
from dashboard.pages.earthquake import Earthquake

class DashBoard:
    """
    Tableau de bord des données sur les catastrophes naturelles

    Méthodes :
        __init__(self) : Initialise l'objet DashBoard
        createDash(self) : Gère la mise en page concernant la page d'accueil
        switch_page(btn1, btn2, btn3) : Permet de changer de page en changeant le layout du contenu
    """
    def __init__(self):
        """
        Initialisation du Dashboard
        """

    def createDash(self):
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
                                    'Tornades',
                                    id='tornado',
                                ),
                                html.Button(
                                    'Séïsmes',
                                    id='earthquake',
                                ),
                            ]
                        ),
                        html.Img(
                            src=self.app.get_asset_url('logo_black.png'),
                            className='logo-navbar right',
                        ),
                    ]
                ),
                html.Div(id='app_output'),
            ]
        )

        # Ajout du fichier CSS
        self.app.css.append_css({'external_url': '/assets/style.css'})

        return self.app

    @callback(
        # ID da la Div dans laquelle afficher le contenu
        Output('app_output', 'children'),
        # IDS des boutons pour les différentes page
        Input('accueil', 'n_clicks'),
        Input('tornado', 'n_clicks'),
        Input('earthquake', 'n_clicks'),
    )

    def switch_page(btn1, btn2, btn3) :
        """
        Change la page de l'application

        Attributs :
            layout = Page à charger sur l'application

        param: btn1 : id de la page d'accueil
                btn2 : id de la page des tornades
                btn3 : id de la page des séïsmes

        Retourne:
            html.Div() : le layout complet avec les informations et données concernant la page sélectionnée
        """
        layout = html.Div(Accueil().get_layout())
        if 'accueil' == ctx.triggered_id :
            layout = html.Div(Accueil().get_layout())
        elif 'tornado' == ctx.triggered_id :
            layout = html.Div(Tornado().get_layout())
        elif 'earthquake' == ctx.triggered_id :
            layout = html.Div(Earthquake().get_layout())
        return layout
