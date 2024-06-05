import hashlib
import time
import itertools 

def crack_md5(md5_hash, charset, max_length):
    start_time = time.time()
    for length in range(1, max_length + 1):
        for password in itertools.product(charset, repeat=length):
            password = ''.join(password)
            if hashlib.md5(password.encode()).hexdigest() == md5_hash:
                end_time = time.time()
                return password, end_time - start_time
    return None, None

if __name__ == "__main__":
    md5_hash = input("MD5 hash: ")
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Şifre karakterleri
    max_length = 8  # Maksimum şifre uzunluğu
    password, time_taken = crack_md5(md5_hash, charset, max_length)
    if password:
        print(f"Şifre: {password}")
        print(f"Kırma süresi: {time_taken} saniye")
    else:
        print("Şifre bulunamadı.")

