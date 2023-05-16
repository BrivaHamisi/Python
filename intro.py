print("Hello, World!")

message = "Hello World"
print(message)

print(""" This is a multiple
liner code in Python """)
print(len(message))

#Slicing in python
print(message[1])
print(message[0:5])
print(message[:5])

print(message[6:])

# Methods/Functions
print(message.lower())
print(message.upper())
print(message.capitalize())

print(message.count("o"))
print(message.find('o'))

new_message = message.replace('World', 'Universe')
print(new_message)


greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name + ". Welcome"

message = '{}, {}. Welcome'.format(greeting, name)

new_formating = f'{greeting}, {name.upper()}. Welcome'

print(message)
print(new_formating)
print(dir(name))

print(help(str))