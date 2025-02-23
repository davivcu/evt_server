import json
import logging

with open("config/config.json", "r") as config_file:
    config = json.load(config_file)

REBUILD = config.get("REBUILD", False)
EVT_PROJECTS = config.get("EVT_PROJECTS", [])
HOST = config.get("HOST", "0.0.0.0")
PORT = config.get("PORT", 5000)

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("evt.log", mode="a")
    ],
    format='%(asctime)s %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S %p', 
    style='%')

if config.get("LOGGING_ON_FILE", False) is not True:
    logging.disable(logging.INFO)