# Nama      : Aliya Sania
# NPM       : 140810210035
# Kelas     : A
# Deskripsi : Tugas 3 Program Hill Chipher

import numpy as np

def hill_cipher(method, text, key, n):
    # Menghitung determinan matriks kunci
    key_det = int(np.linalg.det(key))
    
    # Cek jika determinan adalah genap atau 13
    if key_det % 2 == 0 or key_det == 13:
        print("Det atau bernilai 13. Tidak ada invers.")
        return
    
    if len(text) % n != 0:
        last_char = text[-1]
        text = last_char * (n - len(text) % n)
    
    text_in_number = list(map(char_to_number, list(text)))
    text_vector = np.array(text_in_number).reshape(int(len(text) / n), n)
    result = np.array([], dtype=int)

    if method == 'dekripsi':
        det_inverse = mod_inverse(key_det % 26, 26)
        key = (det_inverse * np.round(key_det * np.linalg.inv(key)).astype(int) % 26)

    for i in range(len(text_vector)):
        temp = np.matmul(key, text_vector[i].reshape(n, 1)) % 26
        result = np.append(result, temp)

    result = list(map(number_to_char, result))
    output = ''.join(result)
    return output

def minor(m, i, j):
    m = np.array(m)
    minor = np.zeros(shape=(len(m) - 1, len(m) - 1))
    p = 0
    for s in range(len(minor)):
        if p == i:
            p += 1
        q = 0
        for t in range(len(minor)):
            if q == j:
                q += 1
            minor[s][t] = m[p][q]
            q += 1
        p += 1
    return minor

def find_key(x, y):
    if len(x) != len(y):
        print("Jumlah huruf plaintext dan ciphertext tidak sama!")
        return 0
    
    m = np.sqrt(len(x)).astype(int)
    x = list(x[:(m * m)].upper())
    mx = list()
    
    for i in x:
        mx.append(int(ord(i)) - 65)
    
    mx = np.array(mx).reshape(int(len(x) / m), m)
    adj = np.zeros(shape=(m, m))
    
    for i in range(m):
        for j in range(m):
            adj[i][j] = (-1) ** (i + j) * int(round(np.linalg.det(minor(mx, j, i)))) % 26
    
    y = list(y[:(m * m)].upper())
    my = list()
    
    for i in y:
        my.append(int(ord(i)) - 65)
    
    my = np.array(my).reshape(int(len(y) / m), m)
    k = np.dot((int(mod_inverse(round(np.linalg.det(mx)), 26)) * adj.astype(int) % 26), my) % 26
    return k

def char_to_number(x):
    x = ord(x) - 65
    return x

def number_to_char(x):
    x = chr(x + 65)
    return x

def mod_inverse(A, M):
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

def input_key(n):
    key = list(map(int, input("Input nilai matriks kunci (space-separated): ").split()))
    key = np.array(key).reshape(n, n) % 26
    print("Matriks kunci:")
    print(key)
    return key

def input_text(string):
    text = input("Masukkan " + string + ": ")
    text = text.replace(' ', '').upper()
    return text

while True:
    print("\n=== Program Hill Cipher ===")
    print("Menu:")
    print("1. Enkripsi\n2. Dekripsi\n3. Cari Key\n4. Exit")
    pilihan = input("Input opsi: ")
    
    if pilihan == '1' or pilihan == '2':
        n = int(input("\nSilahkan input ordo matriks kunci (n x n): "))
        key = input_key(n)
        print("\n")
        text = ''
        
        while len(text) < n:
            text = input_text("teks")
            if len(text) < n:
                print("n harus bil prima terkecil sebagai faktor dari jumlah karakter")
            
        if pilihan == '1':
            print("\nPlaintext: " + text)
            output = hill_cipher("enkripsi", text, key, n)
            print("Ciphertext: " + output)
        elif pilihan == '2':
            print("\nCiphertext: " + text)
            output = hill_cipher("dekripsi", text, key, n)
            print("Plaintext: " + output)
    
    elif pilihan == '3':
        print("\n")
        pt = input_text("plaintext")
        ct = input_text("ciphertext")
        print("\nPlaintext: " + pt + "\nCiphertext: " + ct)
        key = find_key(pt, ct)
        print("key:")
        print(key)
    
    elif pilihan == '4':
        print("\nTerima kasih sudah memakai program ini. ")
        exit()
    
    else:
        print("\nInput tidak sesuai.\n")
