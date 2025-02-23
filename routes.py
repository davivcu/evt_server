import os
import logging
from flask import Blueprint, send_from_directory, render_template
from config_loader import EVT_PROJECTS

routes = Blueprint("routes", __name__)

@routes.route('/')
def serve_list():
    projects = [project["name"] for project in EVT_PROJECTS] or []
    return render_template("index.html", projects=projects)

@routes.route('/<project_name>')
@routes.route('/<project_name>/')
@routes.route("/<project_name>/<path:path>")
def serve_project(project_name, path=''):
    project = next((proj for proj in EVT_PROJECTS if proj["name"] == project_name), None)
    if project:
        dist_path = os.path.join(project["path"], project["build_output"])
        if not path:
            return send_from_directory(dist_path, "index.html")
        return send_from_directory(dist_path, path)
    else:
        logging.warning(f"Richiesta per progetto non esistente: {project_name}")
        return "Progetto non trovato", 404
