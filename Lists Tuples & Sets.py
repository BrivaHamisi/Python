#Lists and tuples allows working with sequential data
#Sets- Unordered collection of values with no duplicates

#lists
courses =['History', 'Maths', 'Physics', 'CompSci']
print(courses)
print(len(courses))

#Slicing
print(courses[-1]) #Getting the last item in the List
print(courses[0])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

#Modifying list
courses.append('Art')  #Inserts value to the end of the list

courses.insert(0, 'Art')  #Takes two arguments, the location and the value

courses.extend   #When we have multiple values in our list

courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)
courses.extend(courses_2) #Extends each individual items in the list

print(courses[0])

#Removing values from a list
print(courses.remove('Maths'))
popped = courses.pop() #Removes the last value in the List

#Sorting a list
courses.reverse()
print(courses)

courses =['History', 'Maths', 'Physics', 'CompSci']
courses.sort(reverse = True) #Not Supported between instances of a list

nums = [1,5,2,4,3]

nums.sort()
print(nums)
nums.sort(reverse = True)

print(popped)
print(courses)

print(nums)

sortted_courses = sorted(courses)
print(sortted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('CompSci'))
print(courses.index('Maths'))

print('Math' in courses)


#Enumearate returns the Index and the Value
for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = ', '.join(courses)
print(course_str)

new_list = course_str.split(', ')
print(new_list)



#Tuples and Sets
#Tuples cannot be modified- Lists are Immutable while Tuples are not

list_1 =['History', 'Maths', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)


list_1[0] = 'Art'
print(list_1)
print(list_2)


#Tuple
#Immutable
tuple_1 = ('History', 'Maths', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1) 
print(tuple_2)

# tuple_1[0] = 'Art'
# print(tuple_1) 
# print(tuple_2)

##Sets are values that are unordered and have no duplicates
cs_courses = {'History', 'Maths', 'Physics', 'CompSci', 'Maths'}
print(cs_courses)

#Membership Test
print('Maths' in cs_courses)

art_courses = {'History', 'Maths', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))

print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


#Empty Lists
empty_list= []
empty_list = list()

#Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty sets
empty_set = {} #This is not right, Its a dictionary
empty_set = set()