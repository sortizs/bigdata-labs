import sys

for linenum, line in enumerate(sys.stdin):
    if linenum != 0:
        line = line.strip()
        line = line.split(',')

        if len(line) >= 2:
            emp = line[0]
            sal = line[2]

            print(f'{emp}\t{sal}')
