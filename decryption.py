from cryptography.fernet import Fernet
from typing import List, Union
import os


def read_dir(directory: str) -> str:
    if not os.path.exists(directory):
        raise Exception('Please make sure you have executed the encryption script')
    return os.getcwd()+'/files'


def decrypt(items: List[str], input_key: bytes) -> None:
    fernet = Fernet(input_key)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_file_data = file.read()
        decrypted_data = fernet.decrypt(encrypted_file_data)
        with open(item, 'wb') as file:
            file.write(decrypted_data)


def read_key() -> bytes:
    if not os.path.exists("pass.key"):
        raise Exception('Please make sure you have executed the encryption script')
    return open("pass.key", "rb").read()


pwd = read_dir('files')
read_me_file = f"{pwd}/README.txt"
if os.path.exists(read_me_file):
    os.remove(read_me_file)
files = os.listdir(pwd)
file_paths = [f'{pwd}/{item}' for item in files]
key = read_key()
decrypt(file_paths, key)
print("Target files decryption completed successfully...")
