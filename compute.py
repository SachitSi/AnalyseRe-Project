import sys

#Global Variables/Constants
replacementFactor = float(0)
result = float(0)
roundto = 1
threshold = 0
limit = 0

#Helper Functions 
def aggregate(num):
    global result
    #If this condition is true, that means
    #we have exceeded the limit
    #keep the result to the limit
    if (num+result)>limit:
        print(round(limit-result,roundto))
        result=limit
    else:
        result = round(num + result,roundto)
        print(num)
    return num


# Read all the inputs from input file
# Currently it is an output from unix command 'cat input'
# Pre-Requisite
# - input file contains integers or float
# - tabular inputs seperated by new line

#You will find rounding code because
#given arg-1000.6-arg-1000000000.0-input6.TXT input file
#if i execute my code, the output is not accurate to the tenth place
def readLinesFromInputFile():
    global threshold
    global limit
    argThresholdIndex = 1
    argLimitIndex = 2
    # Get Paramters from Command Line
    # print ('Number of arguments:', len(sys.argv), 'arguments.')
    # print ('Argument List:', str(sys.argv))
    threshold=float(sys.argv[argThresholdIndex])
    limit=float(sys.argv[argLimitIndex])
    for eachInput in sys.stdin:
        number=float(eachInput)
        if number  <= threshold:
            print(replacementFactor)
        else:
            number = round(number - threshold,roundto)
            number = aggregate(number)
    return result

#(n+1) final print
print(readLinesFromInputFile())





