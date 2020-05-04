import sys

sececon = {}

for line in sys.stdin:
    line = line.strip()
    sec, sal = line.split('\t')

    if sec in sececon:
        sececon[sec].append(int(sal))
    else:
        sececon[sec] = []
        sececon[sec].append(int(sal))

for sec in sececon.keys():
    ave_sal = sum(sececon[sec])*1.0 / len(sececon[sec])
    print(f'{sec}\t{ave_sal}')
