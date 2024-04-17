import argparse
from work_with_files import *
from enum import Enum


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Mode(Enum):
    """
    Attributes
    ----------
    encrypt: int
        So you need to encrypt the text
    decrypt: int
        So you need to decrypt the text
    """
    ENCRYPT = 0
    DECRYPT = 1


def decription_and_encyption(path_to_text: str, path_to_json: str, path_to_result_file, mode: Enum) -> None:
    """decription or encyption the proposed text
        parametres:
        path_to_text: the path to the file where the text is located
        path_to_json: path to json file with step for encrypt/decrypt
        path_to_result_file: the path to the file to write the received text to,
        mode: mode decryption = 1; encyption = 0
    """

    step = int(read_json(path_to_json)["step"])
    text = read_file(path_to_text).upper()
    output = ""
    for i in text:
        place = ALPHABET.find(i)
        new_place = None
        match mode:
            case Mode.ENCRYPT:
                new_place = place + step 
            case Mode.DECRYPT:
                new_place = place - step
            case _:
                print("wrong action")
        if i in ALPHABET:
            output += ALPHABET[new_place]
        else:
            output += i
    write_file(path_to_result_file, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="encryption/decryption")
    parser.add_argument("encryption_key", help="Path to the encryption key file")
    parser.add_argument("original_text", help="Path to the original text")
    parser.add_argument("mode", type=int, default=int, help="Mode of operation: encryption or decryption")
    parser.add_argument("result_file", help="Path to the encrypted file")
    args = parser.parse_args()

    decription_and_encyption(args.original_text, args.encryption_key, args.result_file, Mode(args.mode))