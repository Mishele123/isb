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

