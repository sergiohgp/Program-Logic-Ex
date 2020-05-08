import math
#One line comment

'''
multiple lines comment
yes

'''

#print I'm Sergio and I learn "Python"
print('I\'m Sergio and I learn "Python"')
#use the back slash or triple single quotation to use quotations on a print

#how to print in seperate lines
#one
#two
#three
print('One\ntwo\n\tthree')
print('''one
two
three''')

#variables! Dynamic
age = 27
money = 23.46
name = 'Sergio'
print(age, money,name)
print('My name is {} and I am {} years old and I have {:.2f} dollars.'.format(name,age,money))
print('My name is %s and I am %d years old and I have %.2f dollars.' %(name,age,money))

#operations
a = 7
b = 2
c = a+b
d = a**b #to the power of
e = a/b
f = a//b #integer part
g = a%b #reminder of the division

#inputs in python
name = input('What is your name? ')
print('Hello ',name,)
last_name = input('What is your last name? ')
print('Your full name is ',name,last_name)
n1 = input('Give me a number and I double it for you! ')
# int()
# float()
# str()

# 3 numbers
n1 = int(input('Please, enter the first number: '))
n2 = int(input('Please, enter the second number: '))
n3 = int(input('Please, enter the third number: '))
avg = (n1+n2+n3)/3
print('The average of {}, {} and {} is {}'.format(n1,n2,n3,avg))













