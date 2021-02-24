import random

def stalinSort(prisoners):
  gulag = []

  i = 1
  while i < len(prisoners):
    if prisoners[i] < prisoners[i-1]:
      gulag.append(prisoners[i])
      prisoners.pop(i)
    else:
      i += 1

  release = True
  i = 1
  while i < len(gulag) and release:
    if gulag[i] < gulag[i-1]:
      release = False
      stalinSort(gulag)
    else:
      i += 1

  i2 = 0
  while i2 < len(prisoners) and len(gulag) > 0:
    if gulag[0] <= prisoners[i2]:
      prisoners.insert(i2, gulag[0])
      gulag.pop(0)
    else:
      i2 += 1

  return prisoners

if __name__ == "__main__":
  numbers = []
  for i in range(50):
      numbers.append(random.randint(0, 100))

  print(numbers)

  thing = stalinSort(numbers)
  print(thing)
  print(len(thing))
