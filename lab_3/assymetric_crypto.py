from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


def generate_key_pair():
    """
    Generate RSA key pair.
    return:
        RSAPrivateKey: RSA private key.
    """
    try:
        return rsa.generate_private_key(public_exponent=65537, key_size=2048)
    except Exception as ex:
        raise Exception(f"Error: {ex}")
    

def encrypt_symmetric_key(rsa_key, symmetric_key):
    """
    encrypt symmetric key using rsa algoritm
    args:
        rsa_key (RSAPrivateKey): rsa key using for encryption
        symmetric_key (bytes): symmetric key for encryption
    return:
        encrypted symmetric key (bytes) 
    """
    try:
        encrypted_key = rsa_key.public_key().encrypt(symmetric_key, 
                                padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), 
                                                algorithm=hashes.SHA256(), label=None))
        return encrypted_key                                                                      
    except Exception as ex:
        raise Exception(f"Error: {ex}")