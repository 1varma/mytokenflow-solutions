import re

def render(template, values):
    def fill(match):
        name = match.group(1)
        if name not in values:
            raise KeyError(name)
        return str(values[name])
    return re.sub(r"\{(\w+)\}", fill, template)
