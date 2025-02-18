import os
from flask import Blueprint, send_from_directory
from config_loader import ANGULAR_PROJECTS

routes = Blueprint("routes", __name__)

@routes.route("/<project_name>/<path:path>")
def serve_static(project_name, path):
    project = next((proj for proj in ANGULAR_PROJECTS if proj["name"] == project_name), None)
    if project:
        dist_path = os.path.join(project["path"], project["build_output"])
        return send_from_directory(dist_path, path)
    else:
        return "Progetto non trovato", 404
