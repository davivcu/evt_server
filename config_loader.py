import json

with open("config/config.json", "r") as config_file:
    config = json.load(config_file)

REBUILD = config.get("REBUILD", False)
ANGULAR_PROJECTS = config.get("ANGULAR_PROJECTS", [])
HOST = config.get("HOST", "0.0.0.0")
PORT = config.get("PORT", 5000)
