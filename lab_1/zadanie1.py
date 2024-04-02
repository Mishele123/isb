
import os
from work_with_files import *

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encyption(path_to_text: str, path_to_json: str, path_to_result_file) -> None:
    """encrypt the proposed text"""

    step = int(read_json(path_to_json)["step"])
    text = read_file(path_to_text).upper()
    output = ""

    for i in text:
        if i in ALPHABET:
            new_position = ALPHABET.find(i) + step # get new position
            output += ALPHABET[new_position]
        else:
            output += i
    write_file(path_to_result_file, output)

def decription(path_to_text: str, path_to_json: str, path_to_result_file) -> None:
    """decription the proposed text"""

    step = int(read_json(path_to_json)["step"])
    text = read_file(path_to_text).upper()
    output = ""

    for i in text:
        if i in ALPHABET:
            new_position = ALPHABET.find(i) - step # get new position
            output += ALPHABET[new_position]
        else:
            output += i
    print(output)
    write_file(path_to_result_file, output)


encyption("D:\\allLabs\\isb\\lab_1\\original_text1.txt", "D:\\allLabs\\isb\\lab_1\\encryption_key.json", "D:\\allLabs\\isb\lab_1\\encrypted1.txt")
decription("D:\\allLabs\\isb\lab_1\\encrypted1.txt", "D:\\allLabs\\isb\\lab_1\\encryption_key.json", "D:\\allLabs\\isb\\lab_1\\decrypted.1txt")
