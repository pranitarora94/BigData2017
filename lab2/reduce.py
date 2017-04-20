#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string

#number  of columns of A/rows of B
n = int(sys.argv[1])

#Create data structures to hold the current row/column values (if needed; your code goes here)

MyAValues = [0 for i in range(n)]
MyBValues = [0 for i in range(n)]


currentkey = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

        #Remove leading and trailing whitespace
        line = line.strip()

        #Get key/value
        key, value = line.split('\t',1)

        #Parse key/value input (your code goes here)




        #If we are still on the same key...
        if key==currentkey:

                #Process key/value pair (your code goes here)
                entry = value.split(",")
                index = int(entry[1])
                value = int(entry[2])
                if (entry[0] == "A"):
                        MyAValues[index] = value
                else:
                        MyBValues[index] = value




        #Otherwise, if this is a new key...
        else:
                #If this is a new key and not the first key we've seen
                if currentkey:

                        #compute/output result to STDOUT (your code goes here)
                        MySum = 0
                        keyEntry = currentkey.split(",")
                        row = int(keyEntry[0])
                        col = int(keyEntry[1])
                        for x in range(n):
                                MySum+=MyAValues[x] * MyBValues[x]
                        print '(%s, %s), %d' % (keyEntry[0], keyEntry[1], MySum)



                currentkey = key

                #Process input for new key (your code goes here)
                entry = value.split(",")
                index = int(entry[1])
                value = int(entry[2])
                if (entry[0] == "A"):
                        MyAValues[index] = value
                else:
                        MyBValues[index] = value



#Compute/output result for the last key (your code goes here)
MySum = 0
keyEntry = currentkey.split(",")
row = int(keyEntry[0])
col = int(keyEntry[1])
for x in range(n):
        MySum+=MyAValues[x] * MyBValues[x]
print '(%s, %s), %d' % (keyEntry[0], keyEntry[1], MySum)



