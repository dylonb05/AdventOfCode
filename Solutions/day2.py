# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# This example data contains six reports each containing five levels.
#
# The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:
#
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
# In the example above, the reports can be found safe or unsafe by checking those rules:
#
# 7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
# 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
# 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
# 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
# 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
# 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
# So, in this example, 2 reports are safe.


def isSafe(line, n):
    if isDecreasing(line, n) or isIncreasing(line, n):
        print(line, n)
        return True
    else:
        return False


def isDecreasing(line, n):
    for i in range(len(line) - 1):
        increment = int(line[i]) - int(line[i + 1])
        if increment != -1 and increment != -2 and increment != -3:
            if n == 0:
                temp1 = line.copy()
                temp2 = line.copy()
                temp2.pop(i)
                temp1.pop(i + 1)
                return isSafe(temp1, 1) or isSafe(temp2, 1)
            return False
    return True

def isIncreasing(line, n):
    for i in range(len(line) - 1):
        increment = int(line[i]) - int(line[i + 1])
        if increment != 1 and increment != 2 and increment != 3:
            if n == 0:
                temp1 = line.copy()
                temp2 = line.copy()
                temp2.pop(i)
                temp1.pop(i + 1)
                return isSafe(temp1, 1) or isSafe(temp2, 1)
            return False
    return True



f = open("../day2Input.txt", "r")




totalSafe = 0
for currentLine in f:
    allChar = currentLine.split()
    if isSafe(allChar, 0):
        totalSafe += 1
print(totalSafe)


