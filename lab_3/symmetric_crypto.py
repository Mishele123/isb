import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms


def encrypt_data(symmetric_key, text):
    """
    Encrypt text using Chacha20 symmetric ecryption algorithm
    Args:
        symmetric_key (bytes) : symmetric key for encryption
        text (bytes) : text for encrypted
    Return:
        result encrypted text (bytes) 
    """
    try:
        iv = os.urandom(16)
        cipher = Cipher(algorithms.ChaCha20(symmetric_key, iv), mode=None)
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(text) + encryptor.finalize()
        return iv + ciphertext
    except Exception as ex:
        print(f"Error: {ex}")


def decrypt_data(symmetric_key, ciphertext, iv):
    """
    decrypt text using Chacha20 symmetric ecryption algorithm
    Args:
        symmetric_key (bytes): symmetric key for decryption
        ciphertext (bytes): The ciphertext for decryption
        iv (bytes): initializatioin vector used for encryption
    return:
        decrypted text (bytes)
    """
    try:
        cipher = Cipher(algorithms.ChaCha20(symmetric_key, iv), mode = None)
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()
    except Exception as ex:
        print(f"Error: {ex}")