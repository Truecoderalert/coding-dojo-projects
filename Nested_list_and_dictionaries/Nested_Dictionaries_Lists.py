x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
(x[1][0]) = 15
print (x)
#COMPLETE


# Change the last_name of the first student from 'Jordan' to 'Bryant'
(students[0]['last_name']) = 'Bryant'
print (students)
#COMPLETE


# In the sports_directory, change 'Messi' to 'Andres'
(sports_directory['soccer'][0]) = 'Andres'
print (sports_directory)
# COMPLETE


# Change the value 20 in z to 30
(z [0]['y']) = 30
print (z)
#COMPLETE

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the associated value. 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the associated value. 
students = [
        {'first_name':  'Brandon', 'last_name' : 'Graham'},
        {'first_name' : 'John', 'last_name' : 'Cena'},
        {'first_name' : 'Mark', 'last_name' : 'Hunter'},
        {'first_name' : 'KB', 'last_name' : 'Durant'}
]
def iterateDictionary():
    for x in range(0,len(students)):
        while len(students)>0:
            print(students[x]['first_name'],'-',students[x]['last_name'])
            break
iterateDictionary()

def iterateDictionary2():
    for x in range(0,len(students)):
        while len(students)>0:
            print(students[x]['first_name'])
            break



def printInfo_dictionary():
# that given a dictionary whose values are all lists, prints the name of each key along 
# with the size of its list, and then prints the associated values within each key's list.
    dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
    length = (len('locations'))
    for x in range(0,len(['locations'])):
        while x <= 100:
            print (dojo['locations'][x],length,('Locations'))
        break
    length = (len('instructors'))
    for x in range(0,len(['instructors'])):
        while len('instructors')>1:
            print (dojo['instructors'][x],length,('instructors'))
            break
printInfo_dictionary()
        


