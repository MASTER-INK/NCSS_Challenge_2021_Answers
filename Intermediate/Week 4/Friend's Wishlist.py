wishlist = {'PS5': 750, 'Phone case': 30, 'Oodie': 90, 'LEGO Hogwarts Castle': 650, 'JBL Headphones': 130, 'Drum kit': 520, 'Phone recharge': 30, 'Earrings': 110, 'Spotify subscription': 60, 'Hockey stick': 130, 'Big Toblerone': 16, 'Volleyball': 90, 'Fitbit': 99, 'Harry Potter box set': 65, 'New Chucks': 70}
mon = int(input("How much money do you have to spend? "))
print("The presents you can afford are:")
for i in wishlist:
  if wishlist[i] <= mon:
    print(i)
