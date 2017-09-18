import datetime
import json
import os
import re
import pkg_resources

TIME_RE = re.compile(r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
                     r'T(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})'
                     r'.(?P<microsecond>\d*)')


def _get_export_dirs():
    data_dirs = [
        pkg_resources.resource_filename('ranch', 'exports')
    ]
    for data_dir in data_dirs:
        if os.path.isdir(data_dir):
            yield data_dir


def _convert_export_filename(time_str):
    match = TIME_RE.match(time_str)
    return datetime.datetime(**{k: int(v)
                                for k, v in match.groupdict().items()})


def _get_latest_export():
    latest_file = ''
    latest_time = datetime.datetime(1970, 1, 1)
    for data_dir in _get_export_dirs():
        for item in os.listdir(data_dir):
            if not item.startswith('address-export.'):
                continue

            time_str = os.path.splitext(item)[0][len('address-export.'):]
            time = _convert_export_filename(time_str)
            if time > latest_time:
                latest_time = time
                latest_file = os.path.join(data_dir, item)

    return latest_file


class NoSpecsFileError(Exception):
    def __init__(self):
        self.searched_dirs = {data_dir: os.listdir(data_dir)
                              for data_dir in _get_export_dirs()}

        message = ['Could not find specs file.']
        if len(self.searched_dirs) == 0:
            message = ['No data directories found.']
        else:
            message.append('Searched in following directories:')

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
