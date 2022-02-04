with open("commentary.txt") as com:
  pol = {}
  for l in com:
    l = l.strip().split()
    for i in l:
      p = i.split(":")
      for b in p:
        if b.isupper() and b not in pol and b.isalpha():
          pol[b] = 0
      if len(p) > 1:
        k = l.index(i)
        k = k - 3
        team = l[k]
        pol[team] += 1
  dec = {}
  lpd = []
  for e in pol:
    dec[pol[e]] = e
    lpd += str(pol[e])
  opo, lvs = lpd
  if opo != lvs:
    dc = sorted(dec, reverse = True)
    for m in dc:
      print(dec[m], m)
  else:
    for s in pol:
      print(s, pol[s])



    
