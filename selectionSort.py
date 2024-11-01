def findSmallest(arr):
  smallest = arr[0][1]
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i][1] < smallest:
      smallest = arr[i][1]
      smallest_index = i
  return smallest_index

def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
    smallest = findSmallest(arr)
    newArr.append(arr.pop(smallest))

  return newArr

print(selectionSort([
    ("RadioHead",156),
    ("Kishore Kumar",141),
    ("The Black Keys",35),
    ("Neutral Milk Hotel",94),
    ("Beck",88),
    ("The Strokes",61),
    ("Wilco",111),
]))