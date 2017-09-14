import os
import json
import datetime
import dateutil.parser
import sys


def _get_export_dirs():
    ranch_dir = os.path.dirname(os.path.split(__file__)[0])
    data_dirs = [
        os.path.join(sys.prefix, 'data'),
        os.path.join(ranch_dir, 'data'),
    ]
    for data_dir in data_dirs:
        if os.path.isdir(data_dir):
            yield data_dir


def _get_latest_export():
    latest_file = ''
    latest_time = datetime.datetime(1970, 1, 1)
    for data_dir in _get_export_dirs():
        for item in os.listdir(data_dir):
            if not item.startswith('address-export.'):
                continue

            time_str = os.path.splitext(item)[0][len('address-export.'):]
            time = dateutil.parser.parse(time_str)
            if time > latest_time:
                latest_time = time
                latest_file = os.path.join(data_dir, item)

    return latest_file


class NoSpecsFileError(Exception):
    def __init__(self):
        self.searched_dirs = {data_dir: os.listdir(data_dir)
                              for data_dir in _get_export_dirs()}

        message = ['Could not find specs file. Looked in:']
        for data_dir, items in self.searched_dirs.items():
            message.append('- {}/'.format(data_dir))
            for n, item in enumerate(items):
                char = '└' if n == len(items) - 1 else '├'
                ftype = '/' if os.path.isdir(item) else ''

                message.append('  {}── {}{}'.format(char, item, ftype))

        super().__init__('\n'.join(message))


def _get_default_specs():
    try:
        f = open(_get_latest_export(), 'r')
    except FileNotFoundError as e:
        raise NoSpecsFileError() from e
    else:
        with f as data:
            specs = json.load(data)
    return specs
