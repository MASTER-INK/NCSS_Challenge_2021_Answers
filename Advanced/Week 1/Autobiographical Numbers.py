import collections
auto = input("Number: ")
autob = True
lop = collections.defaultdict(int)
if len(auto) > 10:
  autob = False
if autob == True:
  f = 0
  for nums in auto:
    lop[f] = nums
    f += 1
  ak = sorted(auto, reverse = True)
  c = ""
  for k in ak:
    c += k
  for i in lop:
    if str(lop[i]) == "0":
      if str(i) in c:
        autob = False
    elif str(i) * int(lop[i]) not in c:
      autob = False
if autob == False:
  print(auto, "is not autobiographical.")
elif autob == True:
  print(auto, "is autobiographical.")
