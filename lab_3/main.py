import argparse
import json
import os

from work_with_crypt import generate_keys, encrypt_datafile, decrypt_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    parser.add_argument('-j',
                       '--json_file_path', 
                       type= str, 
                       default= os.path.join("datas", "settings.json"), 
                       help= 'Path to json file for custom settings')
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
        generate_keys(settings['private_key'], settings['public_key'], settings['symmetric_key'])
        # генерируем ключи
    elif args.encryption is not None:
        encrypt_datafile(settings['initial_file'], settings['private_key'], settings['symmetric_key'], settings['encrypted_file'])
        # шифруем
    else:
        decrypt_file(settings['encrypted_file'], settings['private_key'], settings['symmetric_key'], settings['decrypted_file'])
        # дешифруем