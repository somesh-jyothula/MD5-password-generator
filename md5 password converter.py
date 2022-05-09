import hashlib
print("//////////***PASSWORD CONVERTER***//////////")
text = input("Enter the text/Password:")   #Taking Input
hashing = hashlib.md5(text.encode())        #Encoding the input into md5 hash algorithm.
print("The value of hash is : ", hashing.hexdigest())  #hexdigest() is used to return given string which contains only hexadecimal digits.
