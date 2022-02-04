print("Let's get planting everyone!")
flo = input("What kind of flower did you plant? ")
flows = []
flaws = 0
while flo:
  floin = int(input("How many did you plant? "))
  if flo in flows:
    print("Fantastic! We just planted", floin ,"more", flo + "s!")
  else:
    print("Our first", flo + "s! We just planted", floin ,"of them!")
    flows.append(flo)
  flaws += floin
  flo = input("What kind of flower did you plant? ")
print("Nice work, everyone! We planted", flaws ,"flowers!")
print("These are all the kinds of flowers we planted today:")
flows.sort()
for lo in flows:
  print("🏵️", lo)
