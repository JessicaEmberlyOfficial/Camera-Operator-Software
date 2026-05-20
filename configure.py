import os
from textbelt import textbelt
from phonenumbers import phonenumbers
os.system("clear")
question = input("(t)extbelt, or (p)honenumbers?: ")
if question == "t":
  textbelt()

if question == "p":
  phonenumbers()