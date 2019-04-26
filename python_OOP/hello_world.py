# Basic - Print all the numbers/integers from 0 to 150

for numbers in range (0,151):
    print("Number ", numbers)


# Multiples of Five-Print all the multiples of 5 from 5 to 1,000,000.

for count in range (0,1000000):
    if count%5 == 0:
        print(count)


# Counting, the Dojo Way -Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

for integers in range (1,101):
    if integers%5 == 0:
        print("Coding")
    elif integers%10 == 0:
        print("Coding Dojo")
    else:
        print(integers)


# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum=0
for nr in range (0, 500000):
    if  nr%2 == 1:
        sum += nr 
    else:
        nr = nr+1
print(sum)

#Countdown by Fours- Print positive numbers starting at 2018, counting down by fours (exclude 0).


countdown = 2018
while (countdown >= 0):
    if countdown != 0:
        print(countdown)
        countdown = countdown - 4
    else:
        break

# Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)

def flex_countdown(lowNum, highNum, mult):
    for i in range(highNum, lowNum, -mult):
        print(x)
flex_countdown(2,9,3)











        




          


