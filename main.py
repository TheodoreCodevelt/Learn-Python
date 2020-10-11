# Python Tutorial made by Jakob
# Learn Python

print("Hello World")  # the print function displays text on your screen

variable = "Hello World" # this is called a variable. it stores data inside of it for later use.
print(variable) # prints the data stored inside the variable

counter = 0 # assigns 0 to the variable 'counter'
while counter < 10: # while the variable 'counter' is less than 10 do
    print(counter) # print the data in the variable
    counter += 1 # add 1 to the variable

print('\n') # \n means new line so it skips to a new line

list = ['1','2','3'] # this is how you store lists / multiple strings in a variable
for nums in list: # you can print all of the strings of a list 1 by 1 by doing this
    print(nums)

new_variable = input("User Input: ") # asks the user for their input and stores in the variable 'new_variable'
print(new_variable) # prints the data inside the variable

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
total = number1 + number2 # adds the two variables and stores in the variable 'total'
print(total) # prints the variable

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
total = number1 - number2 # subtracts the two variables and stores in the variable 'total'
print(total) # prints the variable

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
total = number1 * number2 # multiplys the two variables and stores it in the variable 'total'
print(total) # prints it

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
total = number1 // number2 # divides the two
print(total)

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
total = number1 / number2 # divides variables leaves remander
print(total) 

new_list = ['apple','grapes','kiwi','oranges'] # list
print(new_list) # prints the list
add_item = input("Enter a new fruit: ") # input
add_item.lower() # makes the input all lowercase
new_list.append(add_item) # adds the data in variable 'add_item' to 'new_list'
print(new_list)

if 1 > 0: # if statement (if 1 is more than 0 do)
    print('hello world')
    break # stops the program
else: # else condition of the statement (else do)
    print("joe mama")
    break
