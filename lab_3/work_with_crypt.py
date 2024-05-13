import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from serialization import serialize_private_key, serialize_public_key, load_private_key
from assymetric_crypto import generate_key_pair, encrypt_symmetric_key, decrypt_symmetric_key
from symmetric_crypto import encrypt_data


def generate_keys(private_key_path, public_key_path, symmetric_key_path):
    """
    generate keys for any encryptions
    args:
        private_key_path (str): path to private key
        public_key_path (str): path to public key
        symmetric_key_path (str): path to symmetric key
    """
    try:
        private_key = generate_key_pair()
        public_key = private_key.public_key()
        symmetric_key = os.urandom(32)
        with open(private_key_path, "wb") as file:
            file.write(serialize_private_key(private_key))
        with open(public_key_path, "wb") as file:
            file.write(serialize_public_key(public_key))
        with open(symmetric_key_path, "wb") as file:
            file.write(symmetric_key)
    except Exception as ex:
        print(f"Error: {ex}")


def encrypt_datafile(sourse_file_path, private_key_path, symmetric_key_path, encrypted_file_path):
    """
    Encrypt file
    args:
        sourse_file_path (str): path to data to encrypt
        private_key_path (str): path to private key
        symmetric_key_path (str): path to symmetric key
        encrypted_file_path (str): path to save encrypt data file
    """
    try:
        with open(private_key_path, "rb") as file:
            private_key_bytes = file.read()
        private_key = load_private_key(private_key_bytes)
        with open(symmetric_key_path, "rb") as file:
            symmetric_key = file.read()
        encrypted_symmetric_key = encrypt_symmetric_key(private_key, symmetric_key)
        with open(symmetric_key_path, "wb") as file:
            file.write(encrypted_symmetric_key)
        with open(sourse_file_path, "rb") as file_from:
            with open(encrypted_file_path, "wb") as file_to:
                text = file_from.read()
                encrypted_text = encrypt_data(symmetric_key, text)
                file_to.write(encrypted_text)
    except Exception as ex:
        print(f"Error: {ex}")


def decrypt_file(encrypted_file_path, private_key_path, symmetric_key_path, decrypted_file_path):
    """
    decrypt file
    args:
        encrypted_file_path (str): path to encrypt data file
        private_key_path (str): path to private key
        symmetric_key_path (str): path to symmetric key
        decrypted_file_path (str): path to save decrypted data file
    """
    try:
        with open(private_key_path, "rb") as file:
            private_key_bytes = file.read()
        private_key = load_private_key(private_key_bytes)
        with open(symmetric_key_path, "rb") as file:
            encrypted_symmetric_key = file.read()
        symmetric_key = decrypt_symmetric_key(private_key, encrypted_symmetric_key)
        with open(encrypted_file_path, "rb") as file_from:
            with open(decrypted_file_path, "wb") as file_to:
                iv = file_from.read(16)
                cipher = Cipher(algorithms.ChaCha20(symmetric_key, iv), mode=None)
                decryptor = cipher.decryptor()
                while chunk := file_from.read(128):
                    decrypted_chunk = decryptor.update(chunk)
                    file_to.write(decrypted_chunk)
                file_to.write(decryptor.finalize())
    except Exception as ex:
        print(f"Error: {ex}")