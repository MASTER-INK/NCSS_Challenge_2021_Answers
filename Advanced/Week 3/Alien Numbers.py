def alien2float(string):
  al = {"a":0, "e":1, "i":2, "o":3, "u":4}
  caps = []
  lows = []
  d = ""
  for i in string:
    if i.lower() in al:
      if i.isupper() is True:
        caps.append(i)
      else:
        lows.append(i)
  for l in caps + lows:
    d = d + l
  if string != d:
    return None
  else:
    total = 0
    tot = 0
    for p in caps:
      tot += 1
      power = len(caps) - tot
      power = 5 ** power
      total += al[p.lower()] * power
    total = float(total)
    indp = 0
    for k in lows:
      indp = indp - 1
      ind = 5 ** indp
      total += float(al[k]) * float(ind)
  return total


if __name__ == '__main__':
  # Run the examples in the question.
  print(repr(alien2float('Eeeee')))
