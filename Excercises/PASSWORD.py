from passlib.hash import pbkdf2_sha256 as pwd
from getpass import getpass
from os import system
from colored import fg, bg, attr

clear = system("clear")

p = (f"{attr(0)}{fg(72)}")
ad = (f"{attr(0)}{fg(124)}")
ag = (f"{attr(0)}{fg(35)}")

hash = '$pbkdf2-sha256$29000$RcjZu7d2bu1d653TWuu9Nw$P.as1TpMwwJ3b/CLL7tFzt5p5jcq6MuOz783QoYahBQ'

password = getpass(f"{p}Password: ")

if pwd.verify(password, hash) == True:
  print(f"{ag}ACCESS GRANTED")
  system("sleep 0.5")
else:
  print(f"{ad}ACESS DENIED")
  system("sleep 1")
  exec(open(__file__).read())

#generate new salt, and hash a password
#hash = pbkdf2_sha256.hash("toomanysecrets")

# verifying the password
#pbkdf2_sha256.verify("toomanysecrets", hash)



