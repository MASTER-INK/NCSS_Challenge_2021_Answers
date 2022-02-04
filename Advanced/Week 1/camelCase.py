def to_camel(ident):
  # TODO implement this function.
  p = []
  c = 0
  cam = ""
  cop = False
  for lets in ident:
    p = p + [lets]
    if cop == True:
      p[c] = p[c].upper()
      cop = False
    if lets == "_":
      p[c] = ""
      cop = True
    c += 1
  for i in p:
    if i != "":
      cam += i
  return cam


if __name__ == '__main__':
  # Run the example inputs in the question.
  print(to_camel('num_to_SMS'))
