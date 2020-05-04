import sys

empleados = {}

for line in sys.stdin:
    line = line.strip()
    emp, sec = line.split('\t')

    if emp in empleados:
        empleados[emp].append(int(sec))
    else:
        empleados[emp] = []
        empleados[emp].append(int(sec))

for emp in empleados.keys():
    num_sec = len(empleados[emp])
    print(f'{emp}\t{num_sec}')
