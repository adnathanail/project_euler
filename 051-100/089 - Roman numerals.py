import pathlib
import re

with open(pathlib.Path(__file__).parent / '089_roman.txt') as f:
  numerals = f.read().split('\n')

def minimize(s):
  s = re.sub("IIIII", "V", s)
  s = re.sub("IIII", "IV", s)
  s = re.sub("VIV", "IX", s)
  s = re.sub("VV", "X", s)
  s = re.sub("XXXXX", "L", s)
  s = re.sub("XXXX", "XL", s)
  s = re.sub("LXL", "XC", s)
  s = re.sub("LL", "C", s)
  s = re.sub("CCCCC", "D", s)
  s = re.sub("CCCC", "CD", s)
  s = re.sub("DCD", "CM", s)
  s = re.sub("DD", "M", s)
  return s

def saved(s):
  return len(s) - len(minimize(s))

print(sum([saved(n) for n in numerals]))