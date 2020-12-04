import json

def is_json(json_date):
    try:
        real_json = json.loads(json_date)
        is_valid = True
    except:
        is_valid = False
    return is_valid
