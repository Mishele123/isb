import os

from serialization import serialize_private_key, serialize_public_key, load_private_key
from assymetric_crypto import generate_key_pair, encrypt_symmetric_key, decrypt_symmetric_key

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