from tamagotchi_class import Tamagotchi
import collections

commands = ["create", "feed", "play", "wait"]
tamagots = {}
deadppl = []
wait = False
com = input("Command: ")
while com:
  commandyes = False
  nocom = True
  for comms in commands:
    if com.startswith(comms):
      commandyes = True
      break
  if commandyes == True:
    if com.startswith("c") and len(com.split()) > 1 and com.split()[1] not in tamagots:
      tama = Tamagotchi(com.split()[1])
      tamagots[com.split()[1]] = tama
    elif com.startswith("c") and len(com.split()) > 1 and com.split()[1] in deadppl:
      tama = Tamagotchi(com.split()[1])
      tamagots[com.split()[1]] = tama
      deadppl[deadppl.index(com.split()[1])] = ""
    elif com.startswith("c") and com.split()[1] in tamagots:
      print("You already have a Tamagotchi called that.")
      nocom = False
      commandyes = False
    elif com.startswith("w"):
      wait = True
    elif len(com.split()) > 1 and com.split()[1] in tamagots:
      tama = tamagots[com.split()[1]]
      if com.startswith("f"):
        tama.feed()
      elif com.startswith("p"):
        tama.play()
    else:
      commandyes = False
      print("No Tamagotchi with that name.")
      nocom = False
  if commandyes == True:
    for tas in sorted(tamagots):
      task = tamagots[tas]
      print(task)
      task.increment_time()
      if task.is_dead() == True:
        deadppl.append(tas)
  elif nocom == True:
    print("Invalid command.")
  com = input("Command: ")
  tamagoyes = True
