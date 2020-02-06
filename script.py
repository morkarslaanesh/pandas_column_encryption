## import libraries

import cryptography
from cryptography.fernet import Fernet

## load data
test_data = pd.read_excel('data.xlsx')
test_data.head()

## generate key
key = Fernet.generate_key()
print(key)

## create data copy
test_data_fernet = test_data

fernet = Fernet(key)

## concert target column to bytes
test_data_fernet['物件名-bytes'] = test_data_fernet['物件名'].apply(lambda x: bytes(x, "utf-8"))
test_data_fernet['物件名-bytes']

test_data_fernet['物件名-string'] = test_data_fernet['物件名-bytes'].str.decode("utf-8")


## encrypt column

test_data_fernet['物件名-encrypt'] = test_data_fernet['物件名-bytes'].apply(lambda x: fernet.encrypt(x))

## decrypt column

test_data_fernet['物件名-decrypt'] = test_data_fernet['物件名-encrypt'].apply(lambda x: fernet.decrypt(x))


## save decrypted data
test_data_fernet['物件名-decrypt'].str.decode("utf-8").to_excel("test.xlsx")
