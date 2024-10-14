# DUBER Fare Splitting
import fhm_unittest as unittest
import numpy as np

def findGroups(money, fare):#problem
    ungrouped = np.array([])  # Change ungrouped to a NumPy array
    count = 0

    for i in range(0, len(money)):
        if money[i] == fare:
            count += 1
            print(f"Group {count} : {money[i]}")
            money[i] = -1
        else:
            left = fare - money[i]
            for j in range(i + 1, len(money)):
                if money[j] == left:
                    count += 1
                    print(f"Group {count} : {money[i]}, {money[j]}")
                    money[i] = -1
                    money[j] = -1
                    break
            if money[i] != -1:
                new_ungrouped = np.array([0] * (len(ungrouped) + 1), dtype=int)
                new_ungrouped[:-1] = ungrouped
                new_ungrouped[-1] = money[i]
                ungrouped = new_ungrouped

    # Print ungrouped members
    if len(ungrouped) > 0:
        print("Ungrouped :", end=" ")
        for member in ungrouped:
            print(member, end=" ")
        print()

print("///  Task 03: DUBER Fare Splitting  ///")
money = np.array([120, 100, 150, 50, 30])
fare = 150
print(f'Task 3:')
findGroups(money, fare)  # This should print

# Group 1 : 120, 30
# Group 2 : 100, 50
# Group 3 : 150

money = np.array([60, 150, 60, 30, 120, 30])
fare = 180
print(f'Task 3:')
findGroups(money, fare)  # This should print

# Group 1 : 60, 120
# Group 2 : 30, 150
# Ungrouped : 30 60
