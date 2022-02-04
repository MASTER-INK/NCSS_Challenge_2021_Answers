def cups_to_grams(cups, density):
  # Convert cups to grams here.
  # The density is in grams-per-cup.
  c = cups * density
  c = round(c, 1)
  return c

# Write the rest of your program here
food = input("What food? ")
cu = float(input("How much in cups? "))
gr = float(input("How many grams per cup? "))
p = cups_to_grams(cu, gr)
print(cu,"cups of", food, "is", p, "grams.")
