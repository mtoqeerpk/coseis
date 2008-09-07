# PEER LOH.1 - Layer over a halfspace, buried double couple source

np = ( 1, 16, 1 )		# number of processors in each dimension
nn = ( 261, 301, 161 )		# number of mesh nodes, nx ny nz
nt = 2250			# number of time steps
dx = 50.			# spatial step size
dt = 0.004			# time step size

# Material properties
hourglass = ( 1., 2. )		# hourglass stiffness and viscosity
io = [
  ( 's0', 'rho', 2700. ),	# density
  ( 's0', 'vp',  6000. ),	# P-wave speed
  ( 's0', 'vs',  3464. ),	# S-wave speed
  ( 's0', 'gam', 0.    ),	# viscosity
]

# Material properties of the layer
io += [
  ( 'sz', 'rho', (1,1,1,0), (-1,-1,21,0), (1,1,1,1), 2600. ),
  ( 'sz', 'vp',  (1,1,1,0), (-1,-1,21,0), (1,1,1,1), 4000. ),
  ( 'sz', 'vs',  (1,1,1,0), (-1,-1,21,0), (1,1,1,1), 2000. ),
]

# Near side boundary conditions:
# Anti-mirror symmetry at the near x and y boundaries
# Free surface at the near z boundary
bc1 = ( -2, -2, 0 )	

# Far side boundary conditions:
# PML absorbing boundaries at x, y and z boundaries
bc2 = ( 10, 10, 10 )

# Source parameters
faultnormal = 0			# disable rupture dynamics
ihypo = ( 1, 1, 41 )		# hypocenter indices
xhypo = ( 0., 0., 2000. )	# hypocenter coordinates
fixhypo = -2			# fix source at element center
tfunc = 'brune'			# Brune pulse time function
tsource = 0.1			# dominant period
moment1 = ( 0., 0., 0. )	# moment tensor M_xx, M_yy, M_zz
moment2 = ( 0., 0., 1e18 )	# moment tensor M_yz, M_zx, M_yz

# Velocity time series output for surface station
io += [
  ( 'wx', 'v', 6000., 80000., 0. ),
]

