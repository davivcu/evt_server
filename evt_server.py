import subprocess
import os
import json
from flask import Flask
from routes import routes
from config_loader import *

app = Flask(__name__)
app.register_blueprint(routes)

if REBUILD:
    for project in ANGULAR_PROJECTS:
        angular_path = project.get("path", "")
        build_output = project.get("build_output", "")
        print(f"Eseguendo 'npm run build' per il progetto: {project['name']} nella cartella: {angular_path}")
        try:
            # Esegui il comando npm run build per ogni progetto Angular utilizzando subprocess.call
            subprocess.call("npm run build", cwd=angular_path, shell=True)
            print(f"Build completata per il progetto {project['name']}")
        except subprocess.CalledProcessError as e:
            print(f"Errore durante l'esecuzione di 'npm run build' per il progetto {project['name']}: {e}")
        except FileNotFoundError as e:
            print(f"Comando non trovato per il progetto {project['name']}: {e}")
        except NotADirectoryError as e:
            print(f"Il path non sembra corretto per {project['name']}: {e}")

if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
