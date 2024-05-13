from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding


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
        print(f"Error: {ex}")


def decrypt_symmetric_key(rsa_key, encrypted_symmetric_key):
    """
    decrypts encrypted symmetric key using rsa decryption.
    args:
        rsa_key (RSAPrivateKey): rsa key using for decryption.
        encrypted_symmetric_key (bytes): encrypted symmetric key for decryption.
    return:
        The decrypted symmetric key (bytes)
    """
    try:
        return rsa_key.decrypt(encrypted_symmetric_key, asymmetric_padding.OAEP(
            mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        ))
    except Exception as ex:
        print(f"Error: {ex}")