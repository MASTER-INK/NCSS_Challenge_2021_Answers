name = input("Tour name: ")
cities = input("Cities: ")
print("Announcing the national " + name + " tour!")
print("Visiting these cities...")
for cit in cities.split():
  print("🏙️ " + cit)
print("Get excited for " + name + "!")
