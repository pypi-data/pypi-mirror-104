FTTCrypt Encryption, Encrypt Text to Cipher or any File to Cipher
#
FTTCrypt stands for File to Text Encryptor, it is a software library built for text encryption and Files converting & encryption to a small ciphertext purposely to enhance file upload and transfer. Imagine sending a file from User A to user B, the file has to be uploaded into a server or network then the receiver to downloads the file. According to FTTCrypt, you are not uploading a File, but a small, encrypted cipherText that represents the file which means you can store the cipher in a database level and access
the file using the cipher anywhere the FTTCrypt runs. No need for a large file or blob storage for your next application. Save
your files within your database as a cipher.
##
```
from fttcrypt import FTTCryptor

key = "SecretKeyGoesHere"
text="Secured Text to to be encrypted"

# Encrypt a plain Text to Cipher
cipherText = FTTCryptor.encryptText(text, key)
print(cipherText)


# Decrypt Cipher to Plain Text
decryptedText = FTTCryptor.decryptText(cipherText, key)
print(decryptedText)


# Encrypt a file to Cipher
cipherText = FTTCryptor.encryptFile(filePath, key)
print(cipherText)

# Decrypt Cipher to File
filePath = FTTCryptor.decryptFile(cipherText, key)
print(filePath)
```