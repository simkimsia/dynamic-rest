from django.utils.six import string_types

FALSEY_STRINGS = (
    '0',
    'false',
    '',
)


def is_truthy(x):
    if isinstance(x, string_types):
        return x.lower() not in FALSEY_STRINGS
    return bool(x)


def unpack(content):
    if not content:
        # empty values pass through
        return content

    keys = [k for k in content.keys() if k != 'meta']
    unpacked = content[keys[0]]
    return unpacked


def replace_methodname(format_string, methodname):
     """
     This function was originally from DRF but was removed in DRF 3.8
     Easiest fix was simply to duplicate the function within DREST
     
     Partially format a format_string, swapping out any
     '{methodname}' or '{methodnamehyphen}' components.
     """
     methodnamehyphen = methodname.replace('_', '-')
     ret = format_string
     ret = ret.replace('{methodname}', methodname)
     ret = ret.replace('{methodnamehyphen}', methodnamehyphen)
     return ret
