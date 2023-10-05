from flet.security import encrypt, decrypt
import dotenv, os

dotenv.load_dotenv()

class encrypter():

    def __init__(self) -> None:
        self.secret = os.getenv("SECRET") 

    def encrypt(self, plainText):
        encrypted = encrypt(plainText, self.secret)
        return encrypted
    

    def decrypt(self, cipherText):
        decrypted = decrypt(cipherText, self.secret)
        return decrypted


if __name__ == "__main__":
    ec = encrypter()
    e = ec.encrypt("lashav19")
    p = ec.decrypt(os.getenv("feidepassord"))
    print(e)
    