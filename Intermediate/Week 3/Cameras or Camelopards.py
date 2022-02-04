shop = input("Shop stock: ")
cam = []
while len(cam) != 3:
  if "cam" in shop.lower():
    cam.append(shop)
  if len(cam) == 3:
    break
  shop = input("Shop stock: ")
cam.sort(reverse = True)
print("Proposals: " + ", ".join(cam))
