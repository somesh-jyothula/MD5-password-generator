import hashlib
print("//////////***PASSWORD CONVERTER***//////////")
text = input("Enter the text/Password:")
hashing = hashlib.md5(text.encode())
print("The value of hash is : ", hashing.hexdigest())
