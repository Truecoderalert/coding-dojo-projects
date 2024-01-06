# Basic - Print all integers from 0 to 150.
for x in range (150):
    print (x)
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range (5,1000,5):
    print (x)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".


for k in range (1,101):
    print(k)
    if k % 5 == 0:
        print('coding')
    if k % 10 == 0:
        print ('coding dojo')
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
for u in range (0,500000 ):
        print (u)
        break

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range (2018,-1,-4):
    print (i)
# Flexible Counter - 
# Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
low = 2
highNum = 9
mult = 3
for i in range (low,highNum + 1):
    if i % mult == 0:
        print(i)
# print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

