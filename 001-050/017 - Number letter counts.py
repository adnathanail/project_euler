units = lambda n: ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"][n]
tens = lambda n: ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"][n]
teens = lambda n: ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"][n-10]
hundreds = lambda n: ["","OneHundred","TwoHundred","ThreeHundred","FourHundred","FiveHundred","SixHundred","SevenHundred","EightHundred","NineHundred"][n]

def numToStr(n):
  if 0 <= n <= 9:
    return units(n)
  elif 10 <= n <= 19:
    return teens(n)
  elif 20 <= n <= 99:
    t,u = [int(x) for x in list(str(n))]
    return tens(t) + units(u)
  elif 100 <= n <= 999:
    x = hundreds(int(str(n)[0]))
    y = numToStr(int(str(n)[1:]))
    return x + (("and" + y) if y != "" else "")
  elif n == 1000:
    return "OneThousand"

print(sum([len(numToStr(i)) for i in range(1,1001)]))