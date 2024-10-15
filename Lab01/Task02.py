# Task 02: Discard Cards
import fhm_unittest as unittest
import numpy as np
def leftshift(array,index):#problem
  for i in range(index,len(array)-1):
    array[i] = array[i+1]
  return array
def discardCards(cards, t):
    # TO DO
  count = 0
  for i in range(len(cards)):
    if cards[i] == t:
      if count%2 == 0:
        cards[i] = 0
      count += 1
  for i in range(len(cards)):
    if cards[i] == 0:
      cards = leftshift(cards,i)
  return cards

print("///  Task 02: Discard Cards  ///")
cards = np.array([1,3,7,2,5,2,2,2,0])
returned_value = discardCards(cards, 2)
print(f'Task 2: {returned_value}') # This should print [1,3,7,5,2,2,0,0,0]
unittest.output_test(returned_value, np.array([1,3,7,5,2,2,0,0,0]))

cards = np.array([5,5,5,0,0])
returned_value = discardCards(cards, 5)
print(f'Task 2: {returned_value}') # This should print [5,0,0,0,0]
unittest.output_test(returned_value, np.array([5,0,0,0,0]))