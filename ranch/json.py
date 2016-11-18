import json
from .address import FieldType


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, FieldType):
            return {
                'key': o.key.name,
                'label': o.label,
                'required': o.required,
                'options': o.options,
            }
        return super().default(o)
