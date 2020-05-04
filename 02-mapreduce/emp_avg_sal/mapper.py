import sys

inputdir = "../datasets/"

for linenum, line in enumerate(sys.stdin):
    if linenum != 0:
        line = line.strip()
        line = line.split(',')

        if len(line) >= 2:
            sec = line[1]
            sal = line[2]

            print(f'{sec}\t{sal}')