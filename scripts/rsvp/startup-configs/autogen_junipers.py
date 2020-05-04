import os
r = ['r1','r2','r3','r4','pe1','pe2']
y = ['r1.yaml','r2.yaml','r3.yaml','r4.yaml','pe1.yaml','pe2.yaml']
j = 'junos_template.j2'

for a,b in zip(r,y):
    os.system(f'python3 config_gen.py -r {a} -y {b} -j {j}')