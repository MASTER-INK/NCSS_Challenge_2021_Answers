def is_crowd(people):
  # Write your function here.
  people = int(people)
  if people > 30:
    return "a crowd"
  if people is 3:
    return "a crowd"
  else:
    return "no crowd"

# Write the rest of your program here.
n = input("Number of people: ")
l = is_crowd(n)
if l == "a crowd":
  print("There's a crowd here!")
else:
  print("There's no crowd here!")
