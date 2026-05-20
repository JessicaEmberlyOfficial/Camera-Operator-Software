import os
import requests
import datetime

def report():
  pn = open("phonenumbers.txt", "r")
  for phonenumber in pn:
    phonenumbers = [phonenumber]
  tbk = open("textbelt.txt", "r")
  key = tbk.read()
  name = input("What is your name?: ")
  state = input("What city and state was ICE Spotted?: ")
  address = input("Do you know the address? (y), or (n): ")
  details = input('Please type in some details (If none put, "N/A"): ')
  if address == "y":
    wa = input("What is the address?: ")
    resp = requests.post('https://textbelt.com/text', {
      'phone': phonenumbers,
      'message': 'ICE WAS SPOTTED IN: ' + state + ' AT AN ADDRESS OF: ' + wa + ''' WITH DETAILS INCLUDING: ''' + details,
      'key': key,
    })
    print(resp.json())
    with open ("OP-M-RL.txt", "a") as f:
      f.write("""
      \n
      REPORTER: """ + name + """
      TIME OF REPORT: """ + str(datetime.datetime.now()) + """
      ICE WAS SPOTTED IN: """ + state + """
      AT AN ADDRESS OF: """ + wa + """
      WITH DETAILS INCLUDING: """ + details)
    
  if address == "n":
    resp = requests.post('https://textbelt.com/text', {
      'phone': phonenumbers,
      'message': 'ICE WAS SPOTTED IN: ' + state + ' AT AN ADDRESS OF: ' + 'N/A ' + ''' WITH DETAILS INCLUDING: ''' + details,
      'key': key,
    })
    print(resp.json())
    with open ("OP-M-RL.txt", "a") as f:
      f.write("""
      \n
      REPORTER: """ + name + """
      TIME OF REPORT: """ + str(datetime.datetime.now) + """
      ICE WAS SPOTTED IN: """ + state + """
      AT AN ADDRESS OF: N/A
      WITH DETAILS INCLUDING: """ + details)