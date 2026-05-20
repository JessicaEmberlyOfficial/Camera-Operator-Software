import os
def textbelt():
  os.system("clear")
  id = input("Please paste the code given to you from Jessica: ")
  with open("textbelt.txt", "w") as f:
    f.write(id)