y1 = float(input("Start (g): "))
y2 = float(input("Finish (g): "))
hour = 0
while y1 < y2:
  y1 = y1 + 0.6 * y1
  hour += 1
hour = round(hour)
print("The loaf would need to rise for", hour, "hours.")
