with open("puzzle.txt") as puz:
  codelet = input("Letter: ")
  lines = []
  for i in puz:
    lines.append(i.strip())
  code = ""
  for k in lines:
    if k[0].lower().startswith(codelet.lower()):
       code += k[-1]
  print("Hidden message:", code)
