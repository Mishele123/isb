from cryptography.hazmat.primitives.asymmetric import rsa


def generate_key_pair():
    """
    Generate RSA key pair.
    return:
        RSAPrivateKey: RSA private key.
    """
    try:
        return rsa.generate_private_key(public_exponent=65537, key_size=2048)
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")