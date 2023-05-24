#Dictionaries help us work with key value pairs
#Two linked values where the key is a Unique Identifier and the value is that data

student = {'name': 'John', 'age': '25', 'courses': ['Maths', 'CompSci']}
print(student)

print(student['name'])
print(student['courses'])


#Get returns None instead of an error
print(student.get('phone'))

#Parsing a default value is key doesnt exist
print(student.get('phone','Not Found'))

#Adding Values to our Dictionary
student['phone'] = '555-555'
print(student.get('phone','Not Found'))

#If key exists it updates the value of that Key
student['name'] = 'Jane'
print(student['name'])
print(student)


#Update a Dictionary
student.update({'name': 'Briva', 'age':'23','phone': '555-5555'})
print(student)

del student['age']
print(student)

name = student.pop('name')
print(name)

#Looping through values in Our Dictinary
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

#Looping through the keys
for key in student:
    print(key)

#Looping through the Items
for key, value in student.items():
    print(key, value)