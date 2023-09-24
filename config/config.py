import json
import os
import sys

def get_config():
    config_path = os.path.join(get_basedir(), 'config.json')
    with open(config_path, 'r') as f:
        return json.load(f)

def get_basedir():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.realpath(__file__))
