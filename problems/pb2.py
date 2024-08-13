# declare and fill out function here
def max_values2(numbers):
  sortedList = sorted(numbers, reverse = True)
  topTwo = (sortedList[0], sortedList[1])
  return topTwo
# test case
print(max_values2([-5, -2, -1, -11])) # -> [1, 2]
