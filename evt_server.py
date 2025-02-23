import subprocess
from flask import Flask
from routes import routes
from config_loader import *

app = Flask(__name__)
app.register_blueprint(routes)

if REBUILD:
    for project in EVT_PROJECTS:
        angular_path = project.get("path", "")
        build_output = project.get("build_output", "")
        logging.info(f" * Eseguendo 'npm run build' per il progetto: {project['name']} nella cartella: {angular_path}")
        try:
            subprocess.call("npm run build", cwd=angular_path, shell=True)
            logging.info(f" * Build completata per il progetto {project['name']}")
        except subprocess.CalledProcessError as e:
            logging.error(f" ** Errore durante l'esecuzione di 'npm run build' per il progetto {project['name']}: {e}")
        except FileNotFoundError as e:
            logging.error(f" ** Comando non trovato per il progetto {project['name']}: {e}")
        except NotADirectoryError as e:
            logging.error(f" ** Il path non sembra corretto per {project['name']}: {e}")

if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
