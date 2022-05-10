import json

def read_json_file(file) -> json:
    with open(f"data/{file}", "r" , encoding="utf-8") as read_file:
        data = json.load(read_file)
    return data

def write_json_file(file, data):
    with open(f"data/{file}", "w", encoding="utf-8") as write_file:
        json.dump(data, write_file, ensure_ascii=False, indent=4)