import pathlib

with open(pathlib.Path(__file__).parent / '059_cipher.txt') as f:
  chars = list(map(int, f.read().split(',')))

# def char_to_string(l):
#   return "".join([chr(n) for n in l])

def most_common(lst):
  return max(set(lst), key=lst.count)

xor = lambda l, key: [l[n]^key[n%3] for n in range(len(l))]

k1 = most_common(chars[0::3]) ^ ord(" ")
k2 = most_common(chars[1::3]) ^ ord(" ")
k3 = most_common(chars[2::3]) ^ ord(" ")
key = [k1, k2, k3]
print("".join([chr(q) for q in key]))

print(sum(xor(chars, key)))