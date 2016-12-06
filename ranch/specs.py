import os
import json
import datetime
from iso8601utils.parsers import datetime as iso8601


def _get_latest_export():
    ranch_dir = os.path.dirname(os.path.split(__file__)[0])
    data_dir = os.path.join(ranch_dir, 'data')

    return os.path.join(data_dir, "address-export.json")


def _get_default_specs():
    with open(_get_latest_export(), 'r') as data:
        specs = json.load(data)
    return specs
