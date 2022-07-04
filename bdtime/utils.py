import json


def show_json(data: (dict, str), sort_keys=False):
    if isinstance(data, dict):
        for k, v in data.items():
            print(k, ' --- ', v)
    else:
        try:
            print(json.dumps(data, sort_keys=sort_keys, indent=4, separators=(', ', ': '), ensure_ascii=False))
        except Exception as e:
            try:
                for k, v in data:
                    print(k, ' --- ', v)
            except Exception as e:
                raise e


def show_ls(data: list, ks=None):
    for dc in data:
        if ks:
            if isinstance(ks, str):
                ks = [ks]
            d = [dc.get(k) for k in ks]
        else:
            d = dc
        print(d)

