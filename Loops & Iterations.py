nums = [1,2,3,4,5]
for num in nums:
    print(num)

#Break _ Completely breaks out of a loop
#Continue _ Skips the given value and proceeds to complete the loop

nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print('Found')
        break

    print(num)


for num in nums:
    if num == 3:
        print('Found')
        continue
    
    print(num)


for num in nums:
    for letter in 'abc':
        print(num, letter)

for i in range (10):
    print(i)

#Evaluates until a condion is true
x = 5

while x < 10:
    if x == 8:
        break
    print(x)
    x +=1
