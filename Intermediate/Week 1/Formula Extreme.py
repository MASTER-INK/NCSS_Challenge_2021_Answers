def to_kmh(knots):
  # Calculate the speed in km/h
  kmhp = 1.852 * knots
  kmhp = round(kmhp, 1)
  return kmhp

# Write the rest of your program here
spe = float(input("Speed (kn): "))
k = to_kmh(spe)
if k < float(60):
  msg = "Go faster!"
elif k >= float(60) and k < float(100):
  msg = "Nice one."
if k >= float(100) and k < float(120):
  msg = "Radical!"
if k >= float(120):
  msg = "Whoa! Slow down!"
k = str(k)
print(k + " km/h -", msg)
