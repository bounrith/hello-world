# import required module
from cryptography.fernet import Fernet

##

# using the key
fernet = Fernet("3awsEjGs4IEtaz7-NfFVVwifww92CTuISVa72-t1GV4=")

# opening the encrypted file
with open('nba.csv', 'rb') as enc_file:
	encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open('nba.csv', 'wb') as dec_file:
	dec_file.write(decrypted)
