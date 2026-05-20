import os
def phonenumbers():
  os.system("clear")
  question = input("Please enter a phone number to add: ")
  with open("phonenumbers.txt", "a") as f:
    if os.path.getsize("phonenumbers.txt") == 0:
      f.write(question)
    else:
      f.write("\n" + question)