#!/usr/bin/env python
"""
Kostrov circular crack test.
"""
import cst

# parameters
nproc3 = 1, 1, 2
delta = 100.0, 100.0, 100.0, 0.0075
shape = 101, 101, 32, 300

# boundary conditions
bc1 = 10, 10, 10
bc2 = -1, 1, -2

# material model
hourglass = 1.0, 1.0
fieldio = [
    ('=', 'rho', [], 2670.0),
    ('=', 'vp',  [], 6000.0),
    ('=', 'vs',  [], 3464.0),
    ('=', 'gam', [], 1.0),
]

# rupture parameters
ihypo = -1, -1, -1.5
faultnormal = 3
vrup = 0.9 * 3464.0
rcrit = 1e9
trelax = 0.0
fieldio += [
    ('=', 'rho', [], 2670.0),
    ('=', 'vp',  [], 6000.0),
    ('=', 'vs',  [], 3464.0),
    ('=', 'gam', [], 1.0),
    ('=', 'mud', [], 1.0),
    ('=', 'mus', [], 1e9),
    ('=', 'dc',  [], 1e9),
    ('=', 'tn',  [],  -90e6),
    ('=', 'ts',  [], -100e6),
]

# receivers
fieldio += [
    ('=w', 'svm', [ -1, -21, -1, ()], 'p20a.bin'),
    ('=w', 'svm', [-13, -17, -1, ()], 'p20b.bin'),
    ('=w', 'svm', [-17, -13, -1, ()], 'p20c.bin'),
    ('=w', 'svm', [-21,  -1, -1, ()], 'p20d.bin'),
    ('=w', 'svm', [ -1, -41, -1, ()], 'p40a.bin'),
    ('=w', 'svm', [-25, -33, -1, ()], 'p40b.bin'),
    ('=w', 'svm', [-33, -25, -1, ()], 'p40c.bin'),
    ('=w', 'svm', [-41,  -1, -1, ()], 'p40d.bin'),
]

# launch SORD
cst.sord.run( locals() )

