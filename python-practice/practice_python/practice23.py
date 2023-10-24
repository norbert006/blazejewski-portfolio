a = []
b = []

with open('primenumbers.txt', 'r') as prime_numbers:
        line = prime_numbers.readline()
        while line:
            line = line.strip()
            a.append(int(line))
            line = prime_numbers.readline()

with open('happynumbers.txt', 'r') as happynumbers:
        line = happynumbers.readline()
        while line:
            line = line.strip()
            b.append(int(line))
            line = happynumbers.readline()

print(list(set(a) & set(b)))

