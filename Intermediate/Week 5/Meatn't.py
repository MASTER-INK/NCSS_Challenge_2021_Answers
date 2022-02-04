import collections
def make_stock_dict(stock_filename):
  # Take the name of a file containing key-value pairs of stocked products.
  # Return a dictionary containing stocked products as keys with a number as a value.
  stock = {}
  with open(stock_filename) as f:
    for i in f:
      sub, numb = i.strip().split(",")
      stock[sub] = int(numb)
  return stock

def restock(stock_dict, product, num_items):
  # Takes a stock dictionary, a product name and the number of items to add.
  # Updates the stock dictionary and prints an alert.
  num_items = num_items * 2
  newstock = stock_dict[product] + num_items
  print("We're running low on", product + "!","Restocking with", num_items,"items.")
  return newstock

# Write the rest of your program here
allstock = make_stock_dict("stock_start.txt")
minstock = make_stock_dict("stock_min.txt")
sold = collections.defaultdict(int)
print("Welcome to MEATN'T! We meatn't so you can!")
pro = input("Product: ")
while pro:
  num = int(input("Number sold: "))
  sold[pro] += num
  allstock[pro] = allstock[pro] - num
  if allstock[pro] < minstock[pro]:
    allstock[pro] = restock(allstock, pro, minstock[pro])
  pro = input("Product: ")
print("Let's see how much we sold!")
for ip in sold:
  print(sold[ip], "units of", ip)
