import getpass
username = input('what\'s your user name?')
from getpass import getpass
password = getpass(prompt = 'what\'s your password?')

pwlength = len(password)

print(f"{username} , your {'*'* pwlength} is {pwlength} long")

