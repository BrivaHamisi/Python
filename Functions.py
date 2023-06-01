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
    return '{}, {} Function'.format(greeting, name)

print(hello_func('Hi', name='Briva'))

