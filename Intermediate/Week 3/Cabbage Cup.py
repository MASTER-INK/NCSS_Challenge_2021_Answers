racers = ['Dash', 'Speedy', 'Lightning', 'Flash', 'Sonic']
print("And the line up is: " + ", ".join(racers))
sleepy = input("Who's gone to sleep? ")
if sleepy in racers:
  print(sleepy, "has been disqualified!")
  racers[racers.index(sleepy)] = "Disqualified"
else:
  print("All snails still awake.")
print("Remaining racers: " + ", ".join(racers))
