notes = """
UMN/MSI Blade
IBM Bladecenter Linux cluster
268 x 2 dual-core 2.6 GHz AMD Opteron
8 GB
/scratch1
/scratch2
ulimit -s unlimited
ulimit -n 4096
~/.modulerc
#%Module1.0
module load pathmpi
"""
login = 'blade.msi.umn.edu'
hosts = [ 'blade287' ]
nodes = 268
cores = 8
ram = 7000
timelimit = 48, 00
sfc = [ 'pathf95' ]
mfc = [ 'mpif90' ]
_ = [ '-o' ]
g = [ '-g' ] + _
p = [ '-O', '-p' ] + _
O = [ '-i8', '-O3', '-OPT:Ofast', '-fno-math-errno' ] + _
