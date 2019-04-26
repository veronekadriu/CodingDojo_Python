# 1.
# How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  
def changeItems(x):
    x[1][0] = 15
    print(x)
changeItems(x=[ [5,2,3], [10,8,9] ])  

# How would you change the last_name of the first student from 'Jordan' to "Bryant"?
def changeStudent(students):
    students[0]['last_name'] = "Bryant"
    print(students)
changeStudent(students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
])
# How would you change the last_name of the first student from 'Jordan' to "Bryant"?
def changeSports(sports_directory):
    sports_directory['soccer'][0] = "Andres"
    print(sports_directory)
changeSports(sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
})
# For z, how would you change the value 20 to 30?
def changeValue(z):
    z[0]['y'] = 30
    print(z)
changeValue(z = [ {'x': 10, 'y': 20} ])
    
# 2.Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.


def iterateDictionary(students):
    for value in students:
        print("first_name -", value['first_name'],  ",  " ,"last_name - ", value['last_name'])
iterateDictionary(students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}])    
        
        
# 3.Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary. 

def getNames(students):
    for value in students:
        print(value['first_name'])        
getNames(students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}])

# 4.Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has. 

def printDojoInfo(dojo):
    
    for key in dojo:
        print(len(dojo[key]), key.upper())
        for x in dojo[key]:
            print(x)
    
        
printDojoInfo(dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
})

