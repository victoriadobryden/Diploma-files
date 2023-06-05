import os
import time

from ecc.curve import Curve25519
from ecc.key import gen_keypair
from ecc.cipher import ElGamal as elgamal_ell # elliptic elgamal

##################################################################################
##################################################################################
# Regular ElGamal
from Crypto.Util.number import getPrime, getRandomRange
from Crypto.PublicKey import ElGamal


# Генерація ключів
def generate_keys(num_bits = 256):
    # Створюємо об'єкт ключа ElGamal
    key = ElGamal.generate(num_bits, os.urandom)
    return key


# Шифрування повідомлення
def encrypt_message(message, public_key):
    # Розпаковуємо публічний ключ
    p = int(public_key.p)
    g = int(public_key.g)
    y = int(public_key.y)

    # Генеруємо випадковий параметр k
    k = getRandomRange(2, p)

    # Перетворюємо повідомлення на ціле число
    m = int.from_bytes(message, 'big')

    # Обчислюємо шифрований текст
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p

    return c1, c2


# Дешифрування шифрованого тексту
def decrypt_message(ciphertext, private_key):
    # Розпаковуємо приватний ключ
    p = int(private_key.p)
    x = int(private_key.x)

    # Розпаковуємо шифрований текст
    c1, c2 = ciphertext

    # Обчислюємо відкритий текст
    m = (c2 * pow(c1, p-1-x, p)) % p

    message = m.to_bytes((m.bit_length() + 7) // 8, 'big')
    return message
##################################################################################

##################################################################################
def read_file(file_size):
    current_directory = os.getcwd()  # Get the current working directory

    file_path = os.path.join(current_directory, f"{size}mb_file.txt")
    if os.path.exists(file_path):
        print(f"Reading file: '{file_path}'")
        with open(file_path, 'r') as file:
            content = file.read()
    else:
        print(f"File '{file_path}' does not exist.\n")
    return content

##################################################################################
# text_binary = b"Hello World"

################################################################################# key gen
print("Generating keys for elgamal...")
num_bits_in_key = 1048 #2048
key_reg = generate_keys(num_bits_in_key)
public_key_reg = key_reg.publickey()

print("Generating keys for elliptic elgamal...")
private_key_ell, public_key_ell = gen_keypair(Curve25519)
cipher_obj = elgamal_ell(Curve25519)

file_sizes = [10, 20]  # Sizes in MB

for size in file_sizes:
    filecontent = read_file(size)
    #convert plain text to bytes
    text_binary = filecontent.encode('utf-8')

    total_time_regular = 0
    total_time_elliptic = 0
    # split message into blocks
    # encrypt each block
    for i in range(0, len(text_binary), 100):
        message_block = text_binary[i:i + 100]

        # regular encryption of message block
        timestamp1_ns = time.time()
        ciphertext_reg = encrypt_message(message_block, public_key_reg)
        timestamp2_ns = time.time()
        total_time_regular += timestamp2_ns - timestamp1_ns

        # decrypted_message = decrypt_message(ciphertext_reg, key_reg) # decrypt with private key
        # print("Public key:", public_key_reg)
        # print("Ciphertext:", ciphertext_reg)
        # print("Decrypted message:", decrypted_message)

        # elliptic encryption of message block
        #timestamp1_ns = time.time()
        #C1, C2 = cipher_obj.encrypt(message_block, public_key_ell)
        #timestamp2_ns = time.time()
        #total_time_elliptic += timestamp2_ns - timestamp1_ns

        # print("C1: ", C1)
        # print("C2: ", C2)
        # new_plaintext = cipher_obj.decrypt(private_key_ell, C1, C2)
        # print("Decrypted plaintext: ", new_plaintext)
    
    print("Encryption time regular for ", size, "mb file with ", num_bits_in_key, "-bit key", round(1000*total_time_regular), 'ms')
    #print("Encryption time elliptic for ", size, "mb file with 256-bit key", round(1000* total_time_elliptic), 'ms')

print("Done")