f = input("Chapter file: ")
with open(f) as k:
  wor = []
  for i in k:
    for p in i.strip().split():
      wor.append(p)
  final = ""
  for l in range(0, 200, 5):
    final += wor[l] + " "
  print(final)
