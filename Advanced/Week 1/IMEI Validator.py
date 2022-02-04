number = input("Enter number: ")
nu = number[::-1]
dig = 1
total = 0
for i in nu:
  if dig == 2:
    ik = int(i) * 2
    if ik > 9:
      c = 0
      for l in str(ik):
        c = c + int(l)
    else:
      c = ik
    dig = 1
  else:
    c = i
    dig = 2
  total = total + int(c)
if total % 10 == int(0):
  print("Valid.")
else:
  print("Invalid.")
