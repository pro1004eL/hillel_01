from pathlib import Path
import logging
import json


logging.basicConfig(
    filename='json_kolomiiets.log',
    level=logging.ERROR,
    format='%(asctime)s - %(message)s - %(levelname)s'
)


parent_dir = Path('work_with_json')

for file in parent_dir.iterdir():
    if file.is_file():

        try:
            with open(file) as f:
                data = json.load(f)

        except json.JSONDecodeError as er:
            logging.error(f'В файлі {file} помилка розбору JSON: {er}')


