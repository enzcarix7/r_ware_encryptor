from getpass import getpass
from os import walk, remove
from os.path import join, isdir
from sys import argv
from typing import Final, Callable
from Crypto.Cipher.AES import new, MODE_CBC, block_size
from Crypto.Cipher._mode_cbc import CbcMode
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Constants for key derivation and encryption
SALT_SIZE: Final[int] = 16
KEY_SIZE: Final[int] = 32
PBKDF2_ITERATIONS: Final[int] = 100_000
CHUNK_SIZE: Final[int] = 64 * 1024

# Function to derive a strong key from a password and a salt
derive_key: Callable[[str, bytes], bytes] = lambda password, salt: PBKDF2(
    password,
    salt=salt,
    dkLen=KEY_SIZE,
    count=PBKDF2_ITERATIONS
)

# Encrypt a single file using AES CBC mode
def encrypt_file(filepath: str, password: str) -> None:
    iv: bytes = get_random_bytes(16)
    salt: bytes = get_random_bytes(SALT_SIZE)
    key = derive_key(password, salt)
    cipher: CbcMode = new(key, MODE_CBC, iv)
    out_filepath: str = f'{filepath}.enc'

    with open(filepath, 'rb') as f_in, open(out_filepath, 'wb') as f_out:
        f_out.write(iv)       # store IV at the beginning
        f_out.write(salt)     # store salt right after IV
        while chunk := f_in.read(CHUNK_SIZE):
            padded = pad(chunk, block_size)
            f_out.write(cipher.encrypt(padded))

    # Uncomment the line below if you want to delete the original file
    # remove(filepath)

# Decrypt a single encrypted file and write the output
def decrypt_file(filepath: str, password: str) -> None:
    if not filepath.endswith('.enc'):
        raise ValueError('Invalid file path for decryption')

    out_filepath: str = filepath.replace('.enc', '.dec')

    with open(filepath, 'rb') as f_in:
        iv = f_in.read(16)
        salt = f_in.read(SALT_SIZE)
        key = derive_key(password, salt)
        cipher: CbcMode = new(key, MODE_CBC, iv)

        with open(out_filepath, 'wb') as f_out:
            while chunk := f_in.read(CHUNK_SIZE):
                decrypted = cipher.decrypt(chunk)
                try:
                    # unpad only the last block (handled below)
                    unpadded = unpad(decrypted, block_size)
                    f_out.write(unpadded)
                except ValueError:
                    f_out.write(decrypted)

    # Uncomment the line below if you want to delete the encrypted file
    # remove(filepath)

# Recursively find and encrypt all files in the folder (excluding .enc)
def scan_and_encrypt(folder: str, password: str) -> None:
    for root, _, files in walk(folder):
        for file in files:
            if not file.endswith('.enc'):  # Exclude already encrypted files
                fullpath = join(root, file)
                print(f'Encrypting: {fullpath}')
                encrypt_file(fullpath, password)

# Recursively find and decrypt all .enc files in the folder
def scan_and_decrypt(folder: str, password: str) -> None:
    for root, _, files in walk(folder):
        for file in files:
            if file.endswith('.enc'):  # Decrypt only .enc files
                fullpath = join(root, file)
                print(f'Decrypting: {fullpath}')
                decrypt_file(fullpath, password)

# Show usage instructions
def usage():
    print('Usage:')
    print(f'\t{argv[0]} encrypt <folder>')
    print(f'\t{argv[0]} decrypt <folder>')
    exit(1)

# Entry point
if __name__ == '__main__':
    if len(argv) != 3:
        usage()

    mode = argv[1]
    folder = argv[2]

    if not isdir(folder):
        print(f'The folder "{folder}" does not exist or is not a valid path.')
        exit(2)

    password = getpass('Enter password: ')

    if mode == 'encrypt':
        scan_and_encrypt(folder, password)
    elif mode == 'decrypt':
        scan_and_decrypt(folder, password)
    else:
        usage()
