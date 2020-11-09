my_dictionary = [
  {
    "name": "Albert Einstein",
    "born": "14/03/1879"
  },
  {
    "name": "Ada Lovelace",
    "born": "10/12/1815"
  },
  {
    "name": "Benjamin Franklin",
    "born": "17/01/1706"
  }
]
print("Welcome to the birthday dictionary. We know the birthdays of:")
i = 0
for elem in my_dictionary:
  print('\t', i, elem['name'])
  i += 1

choice = int(input("Who's birthday do you want to look up?"))
print("\t"+my_dictionary[choice]['name']+"'s is "+ my_dictionary[choice]['born'])
