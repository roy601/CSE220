# Task 04: Get Those Hobbies
import fhm_unittest as unittest
import numpy as np
def add(array, elem):#problem
  size = len(array)
  if array[size - 1] is None:
    new_array = np.array([None] * (size + 1))
    for i in range(size):
      new_array[i] = array[i]
    array = new_array
  array[size - 1] = elem
  return array

def analyzeHobbies(* participants): #(* arguments) is used for variable number of parameters
    # TO DO
    # Print outputs inside the method
    hobbies = np.array([None])
    for p in participants:
      for i in p:
        if i not in hobbies:
          hobbies = add(hobbies, i)
    print("Unique Activities in the Town:")
    print(f"['{hobbies[0]}'", end='')
    for i in range(1,len(hobbies)-1):
        print(f", '{hobbies[i]}'", end='')
    print(']')
    print("Statistics:")
    for i in hobbies:
      if i is None:
        break
      count = 0
      for p in participants:
        for j in p:
          if j == i:
            count += 1
      print(f"{count} participant(s) like(s) {i}.")

print("///  Task 04: Get Those Hobbies  ///")
participant_1 = np.array( ["Hiking", "Reading", "Photography", "Cooking"])
participant_2 = np.array( ["Reading", "Hiking", "Painting"])
participant_3 = np.array( ["Hiking", "Cooking", "Photography"])
print(f'Task 4:')
analyzeHobbies(participant_1, participant_2, participant_3) #This should print

#Unique Activities in the Town:
#['Photography', 'Painting', 'Cooking', 'Reading', 'Hiking']

#Statistics:
#2 participant(s) like(s) Photography.
#1 participant(s) like(s) Painting.
#2 participant(s) like(s) Cooking.
#2 participant(s) like(s) Reading.
#3 participant(s) like(s) Hiking.



participant_1 = np.array( ["Gardening", "Traveling"])
participant_2 = np.array( ["Singing", "Gardening", "Painting"])
print(f'Task 4:')
analyzeHobbies(participant_1, participant_2) #This should print

#Unique Activities in the Town:
#[Gardening, Traveling, Singing, Painting]

#Statistics:
#2 participant(s) like(s) Gardening.
#1 participant(s) like(s) Traveling.
#1 participant(s) like(s) Singing.
#1 participant(s) like(s) Painting.