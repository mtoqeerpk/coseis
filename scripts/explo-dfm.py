#!/usr/bin/env python
"""
Explosion test problem for comparison with DFM
"""

import sord

np3 = 1, 2, 1
nn = 101, 101, 61
dx = 100., 100., 100.
nt = 200
dt = 0.008
fieldio = [
    ( '=', 'rho', [], 2700. ),
    ( '=', 'vp',  [], 6000. ),
    ( '=', 'vs',  [], 3464. ),
    ( '=', 'gam', [], 0.3   ),
]

hourglass = 1., 0.3
rexpand = 1.06
n1expand = 20, 20, 20
n2expand = 20, 20, 20
moment1 = 1e18, 1e18, 1e18
moment2 =   0.,   0.,   0.
tfunc = 'brune'
tsource = 0.1
xihypo = 30., 30., 30.
xihypo = 30.5, 30.5, 30.5
fixhypo = -1

for _f in 'x1', 'x2', 'x3', 'v1', 'v2', 'v3':
    fieldio += [
        ( '=wx', _f, [], 'p1_'+_f, (   0., 3999., -1.) ),
        ( '=wx', _f, [], 'p2_'+_f, (2999., 3999., -1.) ),
        ( '=wx', _f, [], 'p3_'+_f, (3999., 3999., -1.) ),
    ]


sord.run( locals() )

