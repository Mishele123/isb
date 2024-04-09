import argparse
from work_with_files import *




ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"


def decription_and_encyption(path_to_text: str, path_to_json: str, path_to_result_file, mode: str) -> None:
    """decription or encyption the proposed text
        parametres:
        path_to_text: the path to the file where the text is located
        path_to_json: path to json file with step for encrypt/decrypt
        path_to_result_file: the path to the file to write the received text to,
        mode: mode decryption = "decryption"; encyption = "encryption"
    """

    step = int(read_json(path_to_json)["step"])
    text = read_file(path_to_text).upper()
    output = ""
    for i in text:
        place = ALPHABET.find(i)
        new_place = None
        match mode:
            case "encryption":
                new_place = place + step
            case "decryption":
                new_place = place - step
        if i in ALPHABET:
            output += ALPHABET[new_place]
        else:
            output += i
    write_file(path_to_result_file, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="encryption/decryption")
    parser.add_argument("encryption_key", help="Path to the encryption key file")
    parser.add_argument("original_text", help="Path to the original text")
    parser.add_argument("mode", choices=['encryption', 'decryption'], help="Mode of operation: encryption or decryption")
    parser.add_argument("result_file", help="Path to the encrypted file")
    args = parser.parse_args()

    decription_and_encyption(args.original_text, args.encryption_key, args.result_file, args.mode)