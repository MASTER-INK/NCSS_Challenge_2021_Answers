Name = input("What is your surname? ")
name = Name.lower()
Name2 = name.capitalize()
cap = False
if "q" in name:
  if "Q" in Name2:
    print("You have an extremely rare surname!")
    cap = True
  if cap == False:
    print("You have a rare surname!")
else:
  print("No Qs here.")
