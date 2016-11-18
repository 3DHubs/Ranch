import os
import json
import datetime
from iso8601utils.parsers import datetime as iso8601


def _get_latest_export():
    ranch_dir = os.path.dirname(os.path.split(__file__)[0])
    data_dir = os.path.join(ranch_dir, 'data')

    latest_file = ''
    latest_time = datetime.datetime(1970, 1, 1)
    for item in os.listdir(data_dir):
        if not item.startswith('address-export.'):
            continue

        time = iso8601(os.path.splitext(item)[0][len('address-export.'):])
        if time > latest_time:
            latest_time = time
            latest_file = item

    return os.path.join(data_dir, latest_file)


def _get_default_specs():
    with open(_get_latest_export(), 'r') as data:
        specs = json.load(data)
    return specs
