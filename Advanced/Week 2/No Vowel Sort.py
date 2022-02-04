def novowelsort(the_list):
  # TODO perform no vowel sort on `the_list`.
  vowels = ["a", "e", "i", "o", "u"]
  totalwords = []
  diction = {}
  m = -1
  for i in the_list:
    l = i
    m += 1
    if i.isupper() == False:
      for o in vowels:
        i = i.replace(o, "")
    else:
      for o in vowels:
        o = o.upper()
        i = i.replace(o, "")
    if i in diction:
      i = l[-2:]
    totalwords.append(i)
    diction[i] = m
  sortedwords = sorted(totalwords)
  allthewords = []
  for v in sortedwords:
    allthewords.append(the_list[diction[v]])
  return allthewords


if __name__ == '__main__':
  # Example calls to your function.
  print(novowelsort(['ALPHA', 'BETA', 'GAMMA', 'DELTA', 'EPSILON', 'ZETA', 'ETA', 'THETA', 'IOTA', 'KAPPA', 'LAMBDA', 'MU']))
