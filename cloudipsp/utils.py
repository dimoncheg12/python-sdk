import re
import json
import base64

from urllib import urlencode


def data2xml(d):
    result_list = list()

    json_obj_type = type(d)

    if json_obj_type is list:
        for sub_elem in d:
            result_list.append(data2xml(sub_elem))

        return ''.join(d)

    if json_obj_type is dict:
        for tag_name in d:
            sub_obj = d[tag_name]
            result_list.append("<%s>" % tag_name)
            result_list.append(data2xml(sub_obj))
            result_list.append("</%s>" % tag_name)

        return ''.join(result_list)

    return "%s" % d


def to_base64(data):
    return base64.b64encode(json.dumps(data))


def to_xml(data, start='<?xml version="1.0" encoding="UTF-8"?>'):
    return start + data2xml(data)


def to_json(data):
    return json.dumps(data)


def to_form(data):
    return urlencode(data)


def merge_dict(data, *override):
    result = {}
    for current_dict in (data,) + override:
        result.update(current_dict)
    return result


def join_url(url, *paths):
    for path in paths:
        url = re.sub(r'/?$', re.sub(r'^/?', '/', path), url)
    return url