# declare and fill out function here
def youngest_student2(dict):
  sortedDict = sorted(dict.values())
  for k, v in dict.items():
    if v == sortedDict[0]:
      return k


# test case
students = {"Drake": 21, "Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
print(youngest_student2(students))  # Expected output: "Alice"
