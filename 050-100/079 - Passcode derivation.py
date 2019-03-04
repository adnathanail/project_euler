import pathlib, sys

with open(pathlib.Path(__file__).parent / '079_keylog.txt') as f:
  logins = f.read().split('\n')

chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
passcode = ""
found = False
while len(chars) > 0:
  for char in chars:
    x = [login.index(char) for login in logins if char in login]
    if x == []:
      chars.pop(chars.index(char))
    elif list(set(x)) == [0]:
      passcode += char
      logins = [login.replace(char,"") for login in logins]
      chars.pop(chars.index(char))

print(passcode)