#This program takes 1 arguement.  Then prints the next largest number available
#using the same digits as the arguement provided. leading zeros are ignored
#If it is already the largest number possible, -1 is returned.

#note: My strategy was to basically increment the number until I found the next
#number with all the same digits.  The loop below does just that. 

import sys

def findNextNum(n):

    #Check if it is already the largest number possible
    if n == int(''.join(sorted(str(n))[::-1])):    
        #if so, return -1
        return -1
    
    #Create copy of number to increment
    i = int(n)
     
    #Keep looping through each number until max possible number is reached
    while i < int(''.join(sorted(str(n))[::-1])):    
        # increment the number
        i += 1
        #Check if the incremented number contains all the digits of the original number
        if sorted(str(i)) == sorted(str(n)):
            #If so, then i is the next largest number
            return i
        
#Call function and print result 
print(findNextNum((int(sys.argv[1]))))
