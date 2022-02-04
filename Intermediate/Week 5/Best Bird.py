city = input("Enter a city file: ")
with open(city) as noms:
  birds = []
  for i in noms:
    if i.strip() not in birds:
      birds.append(i.strip())
  print("And the nominees are...")
  for names in sorted(birds):
    print("🐦", names)
