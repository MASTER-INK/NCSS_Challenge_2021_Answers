import collections
totals = collections.defaultdict(int)
item = input("Item: ")
while item:
  sold = int(input("Number sold: "))
  totals[item] += sold
  item = input("Item: ")
print("Total sales for today:")
for things in totals:
  print(things, ":", totals[things])
