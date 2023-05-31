if False:
    print("Conditiona was True")


language = 'Java'
if language == 'Python':
    print("Language is Python")
elif language == 'Java':
    print("Language is Java")
elif language == 'JavaScript':
    print("Language is JavaScript")
else:
    print("No Match!")

#Python doesnt have the Switch case
#and
#or
#not

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')


if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')


a=[1,2,3]
b=[1,2,3]
print(a==b)

print(id(a))
print(id(b))
print(a is b)

b = a
print(id(a))
print(id(b))
print(a is b)


#False evaluates to False
#None evaluates to False
#In Numericals 0 evaluates to False
#Any Empty Sequence/String/Mapping or dictionary evaluates to False
