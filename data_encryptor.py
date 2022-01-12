from cryptography.fernet import Fernet
import os
def make_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Load the previously generated key
    """
    key_path = os.path.join(os.path.dirname(__file__), 'secret.key')
    return open(key_path, "r").read()

def encrypt(message):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message.decode()

def decrypt(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    encrypted_message = encrypted_message.encode()
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()


