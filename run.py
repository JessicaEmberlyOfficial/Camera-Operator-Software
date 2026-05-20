import os
from feeds import feeds
from report import report

os.system("clear")
question = input("(f)eeds, or (r)eport: ")

if question == "f":
  feeds()
  
if question == "r":
  report()