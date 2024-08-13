# declare and fill out function here
def replace_spaces(sentence, replacement):
  return sentence.replace(' ', replacement)

# test case
sentence = "Test  This is a test   Testing "
sentence2 = replace_spaces(sentence, "_")
print(sentence2) # -> Test__This_is_a_test__Testing_
