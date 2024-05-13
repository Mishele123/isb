from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def serialize_private_key(rsa_key):
    """
    Serialize private key (rsa) to PEM format
    args:
        ras_key (RSAPrivateKey): key to serialize
    return:
        serialized rsa key in PEM format (bytes)
    """
    try:
        return rsa_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    except Exception as ex:
        print(f"Error: {ex}")

def serialize_public_key(public_key):
    """serialize public key to PEM format
    args:
        public_key (bytes) : public key to serialize
    return:
        serialized public key (bytes) 
    """
    try:
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
    except Exception as ex:
        print(f"Error: {ex}")


def load_private_key(private_key_bytes):
    """
    load private key from PEM file
    args:
        private_key_bytes (bytes): PEM file
    return:
        private key (bytes)
    """
    try:
        return serialization.load_pem_private_key(private_key_bytes, password=None, backend=default_backend())
    except Exception as ex:
        print(f"Error: {ex}")