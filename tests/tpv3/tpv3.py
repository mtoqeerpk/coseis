#!/usr/bin/env python
"""
TPV3 - SCEC validation problem version 3, convergence test
"""

import sord

debug = 0
_reg = 1
_run = [ 
    500., (1, 1, 2),
    300., (1, 1, 2),
    250., (1, 1, 2),
    150., (1, 1, 2),
    100., (1, 1, 2),
]
_run = [ 
    500., (1, 4, 4),
    300., (1, 4, 4),
    250., (1, 4, 4),
    150., (1, 4, 4),
    100., (1, 4, 4),
    75.,  (1, 4, 4),
    50.,  (1, 4, 8),
    30.,  (1, 8, 8),
    25.,  (1, 8, 16),
    15.,  (1, 16, 16),
    10.,  (4, 16, 16),
]
_run = [ 500., (1, 1, 2), ]
vrup = -1.
faultnormal = 3	
hourglass = 1., 2.

mpout = 0

for _i in range( 0, len( _run ), 2 ):
    np3 = _run[_i+1]
    dx = _run[_i]
    dt = dx / 12500.
    nt = int( 12. / dt + 1.5 )
    nn = ( 
        int( 16500. / dx + 21.5 ),
        int(  9000. / dx + 21.5 ),
        int(  6000. / dx + 20.5 ),
    )
    bc1     =    10,    10, 10
    bc2     = -_reg,  _reg, -2
    ihypo   = -_reg, -_reg, -2
    fixhypo = -_reg

    _j, _k, _l = ihypo
    _jj = -int( 15000. / dx + 1.5 ),        -1
    _kk = -int(  7500. / dx + 1.5 ),        -1
    _ll = -int(  3000. / dx + 1.5 ),        -1
    _oo = -int(  1500. / dx + 1.5 ),        -1
    _xx = -int(  1500. / dx - 0.5 ) - _reg, -1

    fieldio = [
        ( '=',  'rho',  [],               2670.     ),
        ( '=',  'vp',   [],               6000.     ),
        ( '=',  'vs',   [],               3464.     ),
        ( '=',  'gam',  [],               0.2       ),
        ( '=',  'dc',   [],               0.4       ),
        ( '=',  'mud',  [],               0.525     ),
        ( '=',  'mus',  [],               1e4       ),
        ( '=',  'tn',   [],              -120e6     ),
        ( '=',  'ts',   [],                70e6     ),
       #( '=c', 'gam',  [], 0.02  (-15001., -7501., -4500.), (15001., 7501., 4500.) ),
       #( '=c', 'mus',  [], 0.677 (-15001., -7501.,    -1.), (15001., 7501.,    1.) ),
       #( '=c', 'ts',   [], 72.9e6 (-1501., -1501.,    -1.), (1501.,  1501.,    1.) ),
       #( '=c', 'ts',   [], 75.8e6 (-1501., -1499.,    -1.), (1501.,  1499.,    1.) ),
       #( '=c', 'ts',   [], 75.8e6 (-1499., -1501.,    -1.), (1499.,  1501.,    1.) ),
       #( '=c', 'ts',   [], 81.6e6 (-1499., -1499.,    -1.), (1499.,  1499.,    1.) ),
        ( '=',  'gam',  [_jj,_kk,_ll,0],  0.02      ),
        ( '=',  'mus',  [_jj,_kk,_l, 0],  0.677     ),
        ( '=',  'ts',   [_oo,_oo,_l, 0],  72.9e6    ),
        ( '=',  'ts',   [_xx,_oo,_l, 0],  75.8e6    ),
        ( '=',  'ts',   [_oo,_xx,_l, 0],  75.8e6    ),
        ( '=',  'ts',   [_xx,_xx,_l, 0],  81.6e6    ),
        ( '=w', 'x1',   [_jj,_kk,_l, 0], 'flt-x1'   ),
        ( '=w', 'x2',   [_jj,_kk,_l, 0], 'flt-x2'   ),
        ( '=w', 'tsm',  [_jj,_kk,_l,-1], 'flt-tsm'  ),
        ( '=w', 'su1',  [_jj,_kk,_l,-1], 'flt-su1'  ),
        ( '=w', 'su2',  [_jj,_kk,_l,-1], 'flt-su2'  ),
        ( '=w', 'psv',  [_jj,_kk,_l,-1], 'flt-psv'  ),
        ( '=w', 'trup', [_jj,_kk,_l,-1], 'flt-trup' ),
       #( '=w', 'tsm',  [_jj,_kk,_l, 1], 'flt-tsm0' ),
       #( '=w', 'tnm',  [_jj,_k, _l, 0], 'xt-tnm'   ),
       #( '=w', 'tsm',  [_jj,_k, _l, 0], 'xt-tsm'   ),
       #( '=w', 'sam',  [_jj,_k, _l, 0], 'xt-sam'   ),
       #( '=w', 'svm',  [_jj,_k, _l, 0], 'xt-svm'   ),
       #( '=w', 'sl',   [_jj,_k, _l, 0], 'xt-sl'    ),
       #( '=w', 'vm2',  [0,_k,0,(1,-1,10)], 'xh' ),
       #( '=w', 'vm2',  [_j,0,0,(1,-1,10)], 'xv' ),
    ]

    for _f in 'su1', 'su2', 'sv1', 'sv2', 'ts1', 'ts2':
        fieldio += [
            ( '=wx', _f, [], 'P1a-'+_f, (-7499.,  -1., 0.) ),
            ( '=wx', _f, [], 'P1b-'+_f, (-7451., -49., 0.) ),
            ( '=wx', _f, [], 'P2a-'+_f, ( -1., -5999., 0.) ),
            ( '=wx', _f, [], 'P2b-'+_f, (-49., -5951., 0.) ),
        ]

    rundir = 'run/%03.0f' % dx
    sord.run( locals() )

