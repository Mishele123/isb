import argparse
import json
import os

# Что то вызвать


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-gen','--generation',help='Run key generation mode')
    group.add_argument('-enc','--encryption',help='Run encryption mode')
    group.add_argument('-dec','--decryption',help='Run decryption mode')
    SETTINGS_FILE = os.path.join("datas", "settings.json")
    try:
        with open(SETTINGS_FILE) as json_file:
            settings = json.load(json_file)
    except Exception as ex:
        print(f"Error with open json file: {ex}")
    args = parser.parse_args()
    if args.generation is not None:
        pass
        # генерируем ключи
    elif args.encryption is not None:
        pass
        # шифруем
    else:
        pass
        # дешифруем