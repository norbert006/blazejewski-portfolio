names_and_freq = {}

with open('names.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        line = line.strip() #Takes the string read in from the line and gets rid of all whitespaces
        if line not in names_and_freq:
            names_and_freq[line] = 1
        else:
            names_and_freq[line] += 1
        line = open_file.readline()

print(names_and_freq)