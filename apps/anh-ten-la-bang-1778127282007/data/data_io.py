import json

def load_json_data(filename):
    list_data = list()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            json_data  = json.load(file)
        list_data.extend(json_data)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return list_data


def write_json_data(json_data, fileName):
    with open(fileName, "w", encoding="utf-8") as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)
