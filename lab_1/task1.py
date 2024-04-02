
from work_with_files import *
import argparse


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
    write_file(path_to_result_file, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="encryption/decryption")
    parser.add_argument("encryption_key", help="Path to the encryption key file")
    parser.add_argument("original_text", help="Path to the original text")
    parser.add_argument("encrypted_file", help="Path to the encrypted file")
    parser.add_argument("decrypted_file", help="Path to the decrypted file")
    args = parser.parse_args()

    encyption(args.original_text, args.encryption_key, args.encrypted_file)
    decription(args.encrypted_file, args.encryption_key, args.decrypted_file)
