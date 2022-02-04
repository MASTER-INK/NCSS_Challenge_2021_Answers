import collections
def buy_slinkies(tickets):
  # Finish the function to convert tickets to slinkies
  slinkies = round(int(tickets/3))
  return slinkies

# Write the rest of your program here
carn = collections.defaultdict(int)
print("Who's here at the carnival today?")
name = input("Name: ")
while name:
  tick = int(input("Starting tickets: "))
  print(name + "'s here, starting with", buy_slinkies(tick), "slinkies worth of tickets!")
  carn[name] = tick
  name = input("Name: ")
print("Let the games begin!")
who = input("Who played? ")
while who:
  loss = int(input("Tickets won/lost: "))
  carn[who] = carn[who] + loss
  who = input("Who played? ")
print("End of the day! Let's see how everyone did!")
for ls in carn:
  print(ls, "can buy", buy_slinkies(carn[ls]) ,"slinkies.")
