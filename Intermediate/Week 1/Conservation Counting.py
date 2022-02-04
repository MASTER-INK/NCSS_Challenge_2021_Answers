plan = input("Which plant did you survey? ")
coun = int(input("Count: "))
plan = plan.lower()
if "fern" in plan:
  print("Fantastic! Keep looking for ferns!")
elif coun < 6:
  print("That's low. We'll put", plan, "on the watch list.")
else:
  print("Great! Recorded", str(coun) + " " + plan + "s", "in this area.")
