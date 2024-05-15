import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from serialization import serialize_private_key, serialize_public_key, load_private_key
from assymetric_crypto import generate_key_pair, encrypt_symmetric_key, decrypt_symmetric_key
from symmetric_crypto import encrypt_data
from work_with_datafile import read_data_from_file, write_data_in_file


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
        write_data_in_file(private_key_path, serialize_private_key(private_key))
        write_data_in_file(public_key_path, serialize_public_key(public_key))
        write_data_in_file(symmetric_key_path, symmetric_key)
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
        private_key_bytes = read_data_from_file(private_key_path)
        private_key = load_private_key(private_key_bytes)
        symmetric_key = read_data_from_file(symmetric_key_path)
        encrypted_symmetric_key = encrypt_symmetric_key(private_key, symmetric_key)
        write_data_in_file(symmetric_key_path, encrypted_symmetric_key)
        text = read_data_from_file(sourse_file_path)
        encrypted_text = encrypt_data(symmetric_key, text)
        write_data_in_file(encrypted_file_path, encrypted_text)
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
        private_key_bytes = read_data_from_file(private_key_path)
        private_key = load_private_key(private_key_bytes)
        encrypted_symmetric_key = read_data_from_file(symmetric_key_path)
        symmetric_key = decrypt_symmetric_key(private_key, encrypted_symmetric_key)
        data = read_data_from_file(encrypted_file_path)
        iv = data[:16]
        cipher = Cipher(algorithms.ChaCha20(symmetric_key, iv), mode=None)
        decryptor = cipher.decryptor()
        encrypted_data = data[16:]
        decrypted_data = b""
        while chunk := encrypted_data[:128]:
            encrypted_data = encrypted_data[128:]
            decrypted_chunk = decryptor.update(chunk)
            decrypted_data += decrypted_chunk
        decrypted_data += decryptor.finalize()
        write_data_in_file(decrypted_file_path, decrypted_data)
    except Exception as ex:
        print(f"Error: {ex}")