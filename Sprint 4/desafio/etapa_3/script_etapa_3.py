import hashlib

while True:

    string = input("Digite a sua senha ou digite '0' para encerrar: ")

    if string == '0':
        print("Programa encerrado")
        break

    else:
        hash_string = hashlib.sha1(string.encode())
        hash_hex = hash_string.hexdigest()
        print(f"A hash SHA-1 da sua senha é: {hash_hex}\n")
