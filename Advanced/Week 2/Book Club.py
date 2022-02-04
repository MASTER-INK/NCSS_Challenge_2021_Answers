books = input("Book read: ")
diction = {}
sortingppl = {}
people = []
while books:
  book, person = books.split(":")
  if book not in diction:
    diction[book] = person
  else:
    diction[book] = diction.get(book) + "," + person
  people.append(person)
  books = input("Book read: ")
for bookings in diction:
  totalppl = set(people)
  bookppl = set(diction[bookings].split(","))
  readingppl = totalppl - bookppl
  readingppl = sorted(readingppl)
  bookings = bookings + ":"
  if len(readingppl) <= 0:
    readingfin = "Everyone has read this!"
  else:
    n = ""
    for p in readingppl:
      if len(n) < 1:
        n += p
      else:
        n += ", " + p
    readingfin = n
  sortingppl[bookings] = readingfin
sortedppl = sorted(sortingppl)
for bookers in sortedppl:
  print(bookers, sortingppl[bookers])

  
