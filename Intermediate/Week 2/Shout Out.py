sent = input("Sentence: ")
shout = 0
for i in sent.split():
  if i.isupper():
    shout += 1
print("Number of shouted words: " + str(shout))
