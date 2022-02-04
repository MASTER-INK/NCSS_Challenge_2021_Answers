streams = {}
while len(streams) < 5:
  friend = input("Friend: ")
  streamer = input("Which stream did they recommend? ")
  if streamer not in streams:
    print(friend ,"recommended", streamer + "!")
    streams[streamer] = friend
  else:
      print("Someone else already recommended that.")
print("Playlist complete! Subscribe to:")
for things in streams:
  print(things + ":", "recommended by", streams[things])
