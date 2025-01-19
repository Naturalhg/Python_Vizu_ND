from dashboard import DashBoard
import clean_data as cd
class Main:
    """
    Cette classe représente l'exécutable pour lancer l'application

    Méthodes :
        main(self) : Méthode pour lancer l'application
    """
    def main(self):
        """
        Méthode pour lancer l'application
        Créer une instance dashboard et l'exécute
        """
        cd.clean_csv_files()
        dashboard = DashBoard()
        app = dashboard.createDash()
        app.run_server(debug=True, use_reloader=False)

if __name__ == '__main__':
    main_instance = Main()
    main_instance.main()
