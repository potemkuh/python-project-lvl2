ADDED = 'added'
CHILDREN = 'children'
KEY = 'key'
NESTED = 'nested'
ORIGIN = 'origin'
REMOVED = 'removed'
TYPE = 'type'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
VALUE = 'value'

def to_list(items):
    items_list = []

    if not isinstance(items, list):
        return [items]
    for item in items:
        items_list.extend(to_list(item))

    return items_list

def render_plain(diff):
    diff_type = diff[TYPE]
    key = diff.get(KEY)
    children = diff.get(CHILDREN)

    if diff_type == ORIGIN:
        rows = [render_plain(child) for child in children]
        return '\n'.join(to_list(rows))

    if diff_type == NESTED:
        rows = []
        for child in children:
            child[KEY] = '{0}.{1}'.format(key, child[KEY])
            rows.append(render_plain(child))
        return rows

    if diff_type == ADDED:
        return "Property '{0}' was added with value: {1}".format(key, value = to_string(diff['value']))


    if diff_type == REMOVED:

        return "Property '{0}' was removed".format(key)

    if diff_type == UPDATED:
        
        return "Property '{0}' was updated. From {1} to {2}".format(key, to_string(diff['old_value']), to_string(diff['new_value']))

    if diff_type == UNCHANGED:
        return []


def to_string(value_to_str, depth):
    if value_to_str is None:
        return 'null'

    if isinstance(value_to_str, dict):

        return '[complex value]'

    if isinstance(value_to_str, str):
        
        return "'{0}'".format(value_to_str)
    
    return str(value_to_str).lower()