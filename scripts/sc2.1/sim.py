#!/usr/bin/env python
"""
PEER Lifelines program task 1A02, Problem SC2.1

SCEC Community Velocity Model, version 2.2 with double-couple point source.
http://peer.berkeley.edu/lifelines/lifelines_pre_2006/lifelines_princ_invest_y-7.html#day
http://www-rohan.sdsu.edu/~steveday/BASINS/Final_Report_1A02.pdf
"""
import os, json
import cst
prm = {}

# parameters
dx = 2000.0; prm['nproc3'] = [1, 1, 1]
dx = 200.0;  prm['nproc3'] = [1, 2, 30]
dx = 100.0;  prm['nproc3'] = [1, 4, 60]
dx = 500.0;  prm['nproc3'] = [1, 1, 2]

# mesh metadata
mesh = os.path.join('run', 'mesh', '%.0f' % dx) + os.sep
meta = json.load(open(mesh + 'meta.json'))
delta = meta['delta']
shape = meta['shape']

# dimensions
dt = dx / 16000.0
dt = dx / 20000.0
nt = int(50.0 / dt + 1.00001)
prm['delta'] = delta + [dt]
prm['shape'] = shape + [nt]

# boundary conditions
prm['bc1'] = [10, 10, 0]
prm['bc2'] = [10, 10, 10]

# material
prm['hourglass'] = [1.0, 1.0]
prm['vs1'] = 200.0
prm['vp1'] = 600.0
prm['fieldio'] = [
    ['rho', [], 'r', 'rho.bin'],
    ['vp',  [], 'r', 'vp.bin'],
    ['vs',  [], 'r', 'vs.bin'],
    ['gam', [], '=',  0.0],
]

# source
x = 56000.0 / dx + 1
y = 40000.0 / dx + 1
z = 14000.0 / dx + 1
prm['ihypo'] = [x, y, z]
prm['source'] = 'moment'
prm['pulse'] = 'integral_brune'
prm['tau'] = 0.2
prm['source1'] = [0.0, 0.0, 0.0]
prm['source2'] = [0.0, 0.0, 1e18]

# receivers
for i in range(8):
    j = (74000.0 - 6000.0 * i) / delta[0] + 1
    k = (16000.0 + 8000.0 * i) / delta[1] + 1
    prm['fieldio'] += [
        ['v1', [j,k,1,':'], 'wi', 'p%s-v1.bin' % i],
        ['v2', [j,k,1,':'], 'wi', 'p%s-v2.bin' % i],
        ['v3', [j,k,1,':'], 'wi', 'p%s-v3.bin' % i],
    ]

# run job
prm['rundir'] = d = os.path.join('run', 'sim', '%.0f' % dx)
os.makedirs(d)
for v in 'rho', 'vp', 'vs':
    os.link(mesh + v + '.bin', d + v + 'bin')
cst.sord.run(prm)

