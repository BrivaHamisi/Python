def hello_func():
    print('Hello Fuction')
print(hello_func)
print(hello_func())


#Keeping your code dry
hello_func()
hello_func()
hello_func()
hello_func()


def hello_func():
    return 'Hello Fuction from Ruturn Statement'

print(hello_func())
print(len('Rest'))
print(hello_func().upper())
print(hello_func().lower())
print(hello_func().capitalize())

#Passing arguments to a Function
def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)

print(hello_func('Hi', name='Briva'))


def student_info(*args, **Kwargs):
    print(args)
    print(Kwargs)

courses = ['math', 'Art']
info = {'name': 'John', 'age': 23}
 
student_info(*courses, **info)

