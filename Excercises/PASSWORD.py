from passlib.hash import pbkdf2_sha256
import locale

hash = '$pbkdf2-sha256$29000$k3LO.V8r5ZxzLgVgjLHW2g$nhE7Fs7VzUnao/QyczWMQkt2DdtzNlZxRonPjtz/Hcs'

while True:
  password = input("Password: ")
  if pbkdf2_sha256.verify(password, hash) == True:
    print("ACCESS GRANTED")
    break
  else:
    print("ACESS DENIED")

#generate new salt, and hash a password
#hash = pbkdf2_sha256.hash("toomanysecrets")

# verifying the password
#pbkdf2_sha256.verify("toomanysecrets", hash)



