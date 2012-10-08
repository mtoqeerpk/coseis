#!/usr/bin/env python

def make():
    import subprocess
    import cst
    d = cst.util.configure()
    m = open('Makefile.in').read().format(**d)
    open('Makefile', 'w').write(m)
    subprocess.check_call(['make'])
    return

def test(argv=[]):
    import os, shutil
    import cst
    make()
    d = 'run/hello-c'
    os.makedirs(d)
    shutil.copy2('hello.c.x', d)
    cst.util.launch(
        rundir = d,
        run = 'exec',
        argv = argv,
        command = './hello.c.x',
        nthread = 2,
        nproc = 2,
        ppn_range = [2],
        minutes = 10,
    )
    d = 'run/hello-f'
    os.makedirs(d)
    shutil.copy2('hello.f.x', d)
    cst.util.launch(
        rundir = d,
        run = 'exec',
        argv = argv,
        command = './hello.f.x',
        nthread = 2,
        nproc = 2,
        ppn_range = [2],
        minutes = 10,
    )
    return

# continue if command line
if __name__ == '__main__':
    import sys
    test(sys.argv[1:])

