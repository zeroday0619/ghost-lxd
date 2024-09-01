import yaml

def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file)  # 파일을 안전하게 불러오기
    return data

load_yaml("./profiles/ghost-base.yaml")
load_yaml("./profiles/ghost-mysql.yaml")