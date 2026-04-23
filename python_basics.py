# Python Basics for automation (Variable, Data types, loops, functions)

# Variable: is like a container
name = 'Henry'         # string
age = 25               # integer
weight = 55.5          # float
is_adult = True        # boolean

# arithmatic operation
a = 9
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)


first_name = 'Matt'
last_name = 'Henry'

full_name = first_name + " " +last_name      # concatenation
print(full_name)




# Loop

for i in range(5):
    print(i)

fruits = ['apple','cherry', 'fig']
for fruit in fruits:
    print(f"I love {fruit}.")


# while

count = 6
while count > 0:
    print(count)
    count -= 1

print("Booom!")

# Function: reusable blocks of code

def great(name):
    return f"Hello, {name}!"

message = great('Hasnat')
print(message)

def add_num(a, b):
    return a + b
total = add_num(5,4)
print(total)
