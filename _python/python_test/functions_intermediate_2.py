#1
x = [ [5,2,3], [10,8,9] ] 
students = [{'first_name':  'Michael', 'last_name' : 'Jordan'},{'first_name' : 'John', 'last_name' : 'Rosales'}]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.1
x[1][0]=15
print(x)

#1.2
students[0]['last_name']='Bryant'
print(students)

#1.3
sports_directory['soccer'][0]='Andres'
print(sports_directory)

#1.4
z[0]['y']=30
print(z)

#------------------------------------
#2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for x in range(len(some_list)):
        print("first_name - "+some_list[x]['first_name']+", last_name - "+some_list[x]['last_name'])
iterateDictionary(students)


#------------------------------------
#3
def iterateDictionary2(key_name,some_list):
    for x in range(0,len(some_list),1):
        print(some_list[x][key_name])
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

#------------------------------------
#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printDojoInfo(some_dict):
    for x in some_dict:
        print(len(some_dict[x]), some_dict[x])
printDojoInfo(dojo)
