from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

token = f.encrypt(b"Some secret stuff")


decrypted = f.decrypt(token)
print(token)
print(decrypted)
