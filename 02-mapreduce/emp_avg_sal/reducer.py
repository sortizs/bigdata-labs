import sys

empleados = {}

for line in sys.stdin:
    line = line.strip()
    emp, sal = line.split('\t')

    if emp in empleados:
        empleados[emp].append(int(sal))
    else:
        empleados[emp] = []
        empleados[emp].append(int(sal))

for emp in empleados.keys():
    ave_sal = sum(empleados[emp])*1.0 / len(empleados[emp])
    print(f'{emp}\t{ave_sal}')
