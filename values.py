import sys, math

if len(sys.argv) != 3:
    print "Usage: python values.py <filename> <number of classes>"
    sys.exit()

# Takes file and pulls out all of the numerical values.
# Counts how many of eachvalue is in the file, and 
# returns a dictionary with the format
#{"value":n} where n is the number of times the value 
# shows up in the file
def fillDictionary(f):
    dictionary = {}
  
    for line in f:
        if line.strip() != "":
            if line.strip() in dictionary:
                dictionary[line.strip()] += 1
            else:
                dictionary[line.strip()] = 1
  
    return dictionary

# Accepts a dictionary with integers or integer strings
def getSumAndEntries(dictionary):
    sum = 0
    numEntries = 0
    for i in dictionary:
        numEntries += float(dictionary[i])
        sum += int(i) * dictionary[i]

    return sum, numEntries

def printFrequency(dictionary, numEntries):
    print "Number\tFrequency\tRelative Frequency"
    for i in dictionary:
        print "{0}:\t{1}\t\t{2:.2%}".format(i, dictionary[i], (dictionary[i] / numEntries))
    print("")

def mean(sum, numEntries):
    return float(sum) / numEntries

def getMaxMin(dictionary):
    maximum = 0.0
    for i in dictionary:
        if float(i) > maximum:
            maximum = float(i)

    minimum = maximum

    for i in dictionary:
        if float(i) < minimum:
            minimum = float(i)

    return maximum, minimum

def getClassWidth(dictionary, nClasses):
    #(maximum - Min) / nClasses
    maximum, minimum = getMaxMin(dictionary)
    
    return int(math.ceil((maximum - minimum) / float(nClasses)))

# Takes a minimum and maximum value, and returns a list of tuples,
# indicating the minmum and maximum values of each class
def getClassIntervals(minimum, maximum, interval):
    ranges = []
    for i in range(int(minimum), int(maximum), interval):
        ranges.append((i, (i + interval) - 1))
    return ranges


# Takes a list of tuples and a dictionary with integers or integer strings
# as the key and number of occurences as values and creates a dictionary 
# populated by occurrences of each value in the original dictionary.
def populateClasses(classes, values):
    filledClasses = {}


    # Fill the dictionary with each of the intervals
    for classInterval in classes:
        filledClasses[classInterval] = 0

    for key in values:
        for classInterval in filledClasses:
            print "comparing {0} with {1} and {2}".format(key, classInterval[0], classInterval[1])
            if int(key) >= classInterval[0] and int(key) <= classInterval[1]:
                print "Adding {0} to {1}".format(values[key], filledClasses[classInterval])
                filledClasses[classInterval] += values[key]

    return filledClasses

def main():
    f = open(sys.argv[1], "r")

    dictionary = fillDictionary(f)

    f.close()

    sum, numEntries = getSumAndEntries(dictionary)

    printFrequency(dictionary, numEntries)

    print "The mean is " + str(mean(sum, numEntries)) + ".\n"

    print "Entries: {0}\n".format(numEntries)

    classWidth = getClassWidth(dictionary, sys.argv[2])

    print "Class width is {0}\n".format(classWidth)

    maximum, minimum = getMaxMin(dictionary)

    print "maximum = {0}\nminimum = {1}\n".format(maximum, minimum)

    classIntervals = getClassIntervals(minimum, maximum, classWidth)

    #print classIntervals

    populatedClasses = populateClasses(classIntervals, dictionary)

    for classInterval in populatedClasses:
        print "{0} : {1}".format(classInterval, populatedClasses[classInterval])

if __name__ == "__main__":
    main()