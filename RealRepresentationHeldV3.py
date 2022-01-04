# By GAP, the unique dimensions of real representations
# are [1, 102, 306, 680, 1029, 1275, 1920, 2058, 2550, 2601, 4080]

import itertools
import sys
import getopt

# Numbers without the 1 and 102 elements for computational purposes
numbersModified = [306, 680, 1029, 1275, 1920, 2058, 2550, 2601, 4080]
target = 4119;
final = []      # Stores the final list of representations
temp = []

# Generates lists of length 7 (since 680 * 7 > 4119) with elements
# from numbersModified and then filters out the lits with sum greater than 4119
# and appends the remaining lists to the list temp.
for n in range(7):
    potentials = list(itertools.combinations_with_replacement(numbersModified, n))
    for x in range(len(potentials)):
        if sum(potentials[x]) <= target:
            temp.append(potentials[x])
    #print('finished one')

# Temp contains all of the lists with sums <= 4119 with combinations from
# numbersModified. The only element left to get to get to a sum of 4119 is 1,
# and 102, so add however many of them to get to 4119
differenceElement = [102]
secondPass = [] # Stores the combinations of temp and 102

# This loop generates all possible lists up to length 102 with entries of 102
# such that the sum of the list is less than the difference between 4119 and
# the list that was under consideration from above

for i in range(len(temp)):
    difference = 4119 - sum(temp[i])
    differenceList = []
    for n in range(102):
        potentialDifferences = list(itertools.combinations_with_replacement(differenceElement, n))
        for j in range(len(potentialDifferences)):
            if sum(potentialDifferences[j]) <= difference:
                differenceList.append(potentialDifferences[j])
    for k in range(len(differenceList)):
        # Realized that append returns a value. need a placeholder
        placeHolder = list(differenceList[k])
        placeHolder.extend(temp[i])
        secondPass.append(placeHolder)

# Now go through adding the trivial representation
for n in range(len(secondPass)):
    difference = target - sum(secondPass[n])  # How many 1's are needed
    item = list(secondPass[n])
    item.extend([1 for k in range(difference)])
    final.append(item)

# Input takes the max number of ones to fix
numberOfOnesInput = int(sys.argv[1:][0])
for n in range(1, int(numberOfOnesInput + 1)):
    #Fix number of trivial reprsentations
    fixedFinal = []        # Stores the list of final but with fixed trivials
    for j in range(len(final)):
        numberOfOnes = final[j].count(1)
        #print(numberOfOnes)
        if numberOfOnes == n:
            fixedFinal.append(final[j])
    f = open('heldRealRepresentations' + str(n) + '.txt',
            'w+')
    f.write('Number of real representations with ' +
            str(n) + ' trivial representations: ' +
            str(len(fixedFinal)) + '\n\n')
    # Real representations using only the direct sum
    for j in range(len(fixedFinal)):
        f.write(str(fixedFinal[j]) + '\n\n')
    f.close()
