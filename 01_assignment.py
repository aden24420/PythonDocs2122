# Aden Davis
# Assignment Examples

# You can assign values to variables by using an equal sign (right goes into left side)
x=5

# When Python reads a variable name, it replaces it with the variable's stored value
y=x+5

#There are four different primitive datatypes
#Integers: any WHOLE number, positive or negative
age=15
#Float: any number with a decimal, positive or negative
grade=98.6
#String: a string of human-readable characters
name="Aden"
#numbers in a string are not numbers, they are letters
favoriteNumber="69"
#Boolean: True or False
#True is any value that is not False or empty
isSmart=True

#You can output to the console by using 'print()'
print(age)
print(grade)
print(name)
print(favoriteNumber)
print(isSmart)

#You can concatenate values together
print("My name " + name)
#You can use functions to convert datatypes
print("and my age is " + str(age))
#Don't forget! If you want to convert a value permanently you must assign the converted value to a variable
age = str(age)
#You can convert back and forth with int(), str(), bool(), and float
print(int(age))
print(float(age))
print(bool(age))

