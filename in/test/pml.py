# PML test problem

nt = 500
dx = 100.
dt = 0.0075
hourglass = ( 1., 1. )

faultnormal = 0
tfunc = 'sbrune'
tfunc = 'brune'
rsource = 50.
tsource = 0.056
moment1 = ( 1e18, 1e18, 1e18 )
moment2 = ( 0, 0, 0 )
fixhypo = -2

np = ( 1, 1, 2 )
io = [
  ( 'wx', 'x', ( -6001.,    -1.,    -1. ) ),
  ( 'wx', 'v', ( -6001.,    -1.,    -1. ) ),
  ( 'wx', 'x', ( -6001., -6001.,    -1. ) ),
  ( 'wx', 'v', ( -6001., -6001.,    -1. ) ),
  ( 'wx', 'x', ( -6001., -6001., -6001. ) ),
  ( 'wx', 'v', ( -6001., -6001., -6001. ) ),
  ( 'wz', 'x', (1,1,0,0), (-1,-1,0, 0), (1,1,1,1), 1 ),
  ( 'wz', 'v', (1,1,0,1), (-1,-1,0,-1), (1,1,1,1), 1 ),
]


if 1:

  # Rect
  ihypo = ( -1, -1, -1 )
  nn = ( 81, 81, 81 )
  bc1 = ( 10, 10, 10 )
  bc2 = ( 2, 2, 2 )
  bc2 = ( 0, 0, 0 )
  ihypo = ( 0, 0, 0 )

if 0:

  # Non-rect
  ihypo = ( 0, 0, 0 )
  nn = ( 41, 41, 41 )
  affine = ( ( 1.,0.,0.), (0.,1.,1.), (0.,0.,1.) ) # shear, 1
  affine = ( ( 1.,0.,1.), (0.,1.,0.), (0.,0.,1.) ) # shear, 2
  affine = ( ( 1.,1.,0.), (0.,1.,0.), (0.,0.,1.) ) # shear, 3
  # affine = ( ( 25., 0., 9. ), ( 0., 10., 0. ), ( 0., 0., 16. ), 10. ) # 2D, strain, FIXME
  # affine = ( (  4., 0., 0. ), ( 0.,  1., 0. ), ( 0., 0.,  1. ),  1. ) # 1D, strain, FIXME
  # affine = ( ( 12., 3., 3. ), ( 0.,  9., 1. ), ( 0., 0.,  8. ),  6. ) # 3D, strain, FIXME
  bc1 = ( 10, 10, 10 )
  bc2 = ( 10, 10, 10 )
  bc1 = ( 0, 0, 0 )
  bc2 = ( 0, 0, 0 )

  # Junk
  tfunc = 'sbrune'
  ihypo = ( 0, 0, 0 )
  nn = ( 51, 51, 51 )
  bc1 = ( 10, 10, 10 )
  bc2 = ( 10, 10, 10 )

  # Mixed rect
  ihypo = ( 0, 0, 0 )
  nn = ( 161, 161, 161 )
  bc1 = ( 10, 10, 10 )
  bc2 = ( 0, 0, 0 )

