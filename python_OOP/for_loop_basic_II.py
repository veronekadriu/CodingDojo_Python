# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

def makeItBig(list):
  list2 = []
  for x in list: 
    if x > 0:
        list2.append('big')
    else:
        list2.append(x)
        print(list2)        
makeItBig([3,5,-5])

# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
def greaterThanSecond(list):
  only_pos = [num for num in list if num >= 1] 
  pos_count = len(only_pos)
  list.remove(list[-1])
  list.append(pos_count)
  print(list)

greaterThanSecond([-1,1,1,1])

# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10

def sumTotal(list):
    print(sum(list))
sumTotal([1,2,3,4])

# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5
def average(list):
    print(sum(list)/len(list))
average([1,2,3,4])

# Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4

def length(list):
    print(len(list))
length([1,2,3,4])

# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def minimum(list):
    if len(list) == 0:
        return False
    else:
        print(min(list))
minimum([-1,-2,-6])

# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maximum(list):
    if len(list) == 0:
        return False
    else:
        print(max(list))
maximum([-1,-2,-6])

# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
def ultimateAnalyze(list):
    dictionary = {1:sum(list), 2:sum(list)/len(list), 3:min(list), 4:max(list), 5:len(list)}
    print(dictionary)
ultimateAnalyze([1,2,3,4])

# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
def reverseList(list):
    list.reverse()
    print(list)
reverseList([1,2,3,4])