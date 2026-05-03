with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# read line by line

with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())