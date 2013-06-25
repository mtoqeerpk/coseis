"""
KAUST Shaheen: IBM Blue Gene/P

module unload GNU
module load IBM
module load numpy
"""

maxcores = 4
maxram = 4096
ppn_range = [1, 2, 4]
nthread = 1

account = 'k68'
queue = 'default'
queue_opts = [
    ('development', {'maxnodes':  8 * 1024, 'maxtime':   30}),
    ('smallblocks', {'maxnodes':      1024, 'maxtime': 1440}),
    ('pset64',      {'maxnodes':  4 * 1024, 'maxtime': 1440}),
    ('pset128',     {'maxnodes': 12 * 1024, 'maxtime': 1440}),
    ('default',     {'maxnodes': 16 * 1024, 'maxtime': 1440}),
]

launch = 'mpirun -mode VN -np {nproc} -exe {command}'
submit = 'llsubmit {submit_flags} "{name}.sh"'
