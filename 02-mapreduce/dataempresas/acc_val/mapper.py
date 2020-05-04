import sys

for linenum, line in enumerate(sys.stdin):
    if linenum != 0:
        line = line.strip()
        line = line.split(',')

        if len(line) >= 2:
            acc = line[0]
            val = line[1]
            dte = line[2]

            print(f'{acc}\t{val}\t{dte}')
