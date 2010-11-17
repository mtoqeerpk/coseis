#!/usr/bin/env python
"""
SORD tests
"""
import subprocess, shutil
import cst

def test_sord_parallel():
    """
    Test SORD parallelization with point source
    """

    # parameters
    run = 'exec'
    argv = []
    force = True
    debug = 0
    itstats = 1
    shape = 5, 2, 2, 2
    delta = 100.0, 100.0, 100.0, 0.0075
    bc1 = 0, 0, 0
    bc2 = 0, 0, 0

    # source
    source = 'potency'
    ihypo = 1.5, 1.5, 1.5
    ihypo = 3.0, 1.5, 1.5
    source1 = 1e10, 1e10, 1e10
    source2 =  0.0,  0.0,  0.0
    timefunction = 'delta'

    # material
    hourglass = 1.0, 1.0
    fieldio = [
        ( '=', 'rho', [], 2670.0 ),
        ( '=', 'vp',  [], 6000.0 ),
        ( '=', 'vs',  [], 3464.0 ),
        ( '=', 'gam', [], 0.3 ),
    ]

    # output
    for f in cst.sord.fieldnames.volume:
        fieldio += [ ('=w', f, [], f) ]

    # run
    d = []
    for i in 1, 3:
        nproc3 = i, 1, 1
        rundir = 'tmp/%s' % i
        d += [rundir]
        cst.sord.run( locals() )

    # diff
    cmd = (
        'diff',
        '--recursive',
        '--exclude=prof',
        '--exclude=conf.py',
        '--exclude=meta.py',
        '--exclude=parameters.py',
        '--exclude=sord-sO4',
        '--exclude=sord-mO4',
        d[0], d[1],
    )
    pid = subprocess.Popen( cmd, stdout=subprocess.PIPE )
    out = pid.communicate()[0]
    print out

    # cleanup and test for empty diff
    #shutil.rmtree( 'tmp' )
    assert out == ''

# continue if command line
if __name__ == '__main__':
    test_sord_parallel()
