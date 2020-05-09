import os
os.system("clear")

link = (input()).split("/")

if link[2] == 'youtu.be':
 id = link[len(link) - 1]
 print(id)

elif link[2] == 'www.youtube.com':
  id = link[len(link) - 1].split("=")
  id = id[1]
  print(id)


