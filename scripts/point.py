#!/usr/bin/env python
"""
Miniature point source test
"""

import sord

debug = 0
np3 = 1, 2, 1
np3 = 1, 1, 1
nn = 2, 2, 2
nt = 10
dx = 100.0, -100.0, -100.0
dt = 0.0075
bc1 = 0, 0, 0
bc2 = 0, 0, 0
hourglass = 1.0, 0.0
src_type = 'moment'
src_w1 = 1e16, 1e16, 1e16
src_w2 =  0.0,  0.0,  0.0
ihypo = 1.5, 1.5, 1.5

fieldio = [
    ( '=', 'rho', [], 2670.0 ),      
    ( '=', 'vp',  [], 6000.0 ),      
    ( '=', 'vs',  [], 3464.0 ),      
    ( '=', 'gam', [],    0.0 ),      
]
for _f in sord.fieldnames.volume:
    fieldio += [ ( '=w', _f, [], _f ) ]

sord.run( locals() )

