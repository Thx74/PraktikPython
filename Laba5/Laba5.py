def read_lines_from_file(file, numLines):
    with open(file, 'r') as file:
        lines = file.readlines() 
        return lines[:numLines]

file = 'laba5/text.txt'
numLines = 5

lines = read_lines_from_file(file, numLines)
print(lines)
print("numLines: " + str(numLines))