with open("morsecode.txt") as morse:
  mrcode = {}
  for lines in morse:
    let, mor = lines.strip().split()
    mrcode[let] = mor
  mes = input("Message: ")
  allmes = ""
  for i in mes.upper():
    if i == " ":
      allmes += "/" + " "
    else:
      allmes += mrcode[i] + " "
  print(allmes[:-1])
