time = int(input("Times table: "))
step = int(input("Step: "))
for i in range(3, 13, step):
  print(str(time) + " x" + " [ ] = " + str(i * time))
