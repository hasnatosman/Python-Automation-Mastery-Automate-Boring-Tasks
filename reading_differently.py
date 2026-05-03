with open('example.txt', 'r') as file:
    partial_content = file.read(14)
    print(f"First 15 characters: {partial_content}")

    file.seek(0)

    first_line = file.readline()
    print(f'First line: {first_line.strip()}')

    remaining_lines = file.readlines()
    print('Remaining Line: ')
    for line in remaining_lines:
        print(f' - {line.strip()}')
