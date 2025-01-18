from dash import Dash, html, dcc
from dashboard import DashBoard

class Main:
    """
    Cette classe représente l'exécutable pour lancer l'application

    Méthodes :
        main(self) : Méthode principale pour lancer l'application
    """
    def main(self):
        """
        Méthode principale pour lancer l'application
        Créer une instance dashboard et l'exécute
        """
        dashboard = DashBoard()
        app = dashboard.createDashApplication()
        app.run_server(debug=True, use_reloader=False)

if __name__ == '__main__':
    main_instance = Main()
    main_instance.main()
