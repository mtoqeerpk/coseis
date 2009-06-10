#!/usr/bin/env python
"""
Build SORD binaries and documentation
"""
import os, sys, getopt, util, configure

def build( mode=None, optimize=None ):
    """
    Build SORD code.
    """
    cfg = configure.configure()
    if not optimize:
        optimize = cfg['optimize']
    if not mode:
        mode = cfg['mode']
    if not mode:
        mode = 'sm'
    base = (
        'globals.f90',
        'diffcn.f90',
        'diffnc.f90',
        'hourglass.f90',
        'bc.f90',
        'surfnormals.f90',
        'util.f90',
        'frio.f90', )
    common = (
        'arrays.f90',
        'fieldio.f90',
        'stats.f90',
        'parameters.f90',
        'setup.f90',
        'gridgen.f90',
        'material.f90',
        'source.f90',
        'rupture.f90',
        'resample.f90',
        'checkpoint.f90',
        'timestep.f90',
        'stress.f90',
        'acceleration.f90',
        'sord.f90', )
    cwd = os.getcwd()
    srcdir = os.path.realpath( os.path.dirname( __file__ ) )
    try:
        os.mkdir( os.path.join( srcdir, 'bin' ) )
    except:
        pass
    new = False
    os.chdir( os.path.join( srcdir, 'src' ) )
    if 's' in mode:
        source = base + ( 'serial.f90', ) + common
        for opt in optimize:
            object_ = os.path.join( '..', 'bin', 'sord-s' + opt )
            compiler = cfg['fortran_serial'] + cfg['fortran_flags'][opt]
            new |= util.compile( compiler, object_, source )
    if 'm' in mode and cfg['fortran_mpi']:
        source = base + ( 'mpi.f90', ) + common
        for opt in optimize:
            object_ = os.path.join( '..', 'bin', 'sord-m' + opt )
            compiler = cfg['fortran_mpi'] + cfg['fortran_flags'][opt]
            new |= util.compile( compiler, object_, source )
    if new:
        try:
            os.link( '.ignore', '.bzrignore' )
            os.system( 'bzr export sord.tgz' )
        except:
            pass
    os.chdir( cwd )
    return

def docs():
    """
    Prepare documentation.
    """
    import re
    from docutils.core import publish_string
    out = '\nExamples\n--------\n'
    sources = [ 'loh1.py', 'tpv3.py', 'saf.py', ]
    for f in sources:
        doc = open( 'examples/' + f, 'r' ).readlines()[2].strip()
        out += '| `%s <examples/%s>`_: %s\n' % ( f, f, doc )
    out += '\nFortran source code\n-------------------\n'
    sources = [
        'sord.f90',
        'globals.f90',
        'parameters.f90',
        'setup.f90',
        'arrays.f90',
        'gridgen.f90',
        'material.f90',
        'resample.f90',
        'timestep.f90',
        'stress.f90',
        'source.f90',
        'rupture.f90',
        'acceleration.f90',
        'hourglass.f90',
        'bc.f90',
        'diffcn.f90',
        'diffnc.f90',
        'surfnormals.f90',
        'fieldio.f90',
        'checkpoint.f90',
        'stats.f90',
        'serial.f90',
        'mpi.f90',
        'frio.f90',
        'util.f90',
    ]
    for f in sources:
        doc = open( 'src/' + f, 'r' ).readlines()[0].strip().replace( '! ', '' )
        out += '| `%s <src/%s>`_: %s\n' % ( f, f, doc )
    out += '\nPython wrappers\n---------------\n'
    sources = [
        '__init__.py',
        'default-cfg.py',
        'default-prm.py',
        'fieldnames.py',
        'configure.py',
        'setup.py',
        'remote.py',
        'util.py',
    ]
    for f in sources:
        doc = open( f, 'r' ).readlines()[2].strip()
        out += '| `%s <%s>`_: %s\n' % ( f, f, doc )
    download = ( "Latest source code version `%s <sord.tgz>`_"
             % open( 'version', 'r' ).read().strip() )
    open( 'download.txt', 'w' ).write( download )
    open( 'sources.txt', 'w' ).write( out )
    settings = dict(
        datestamp = '%Y-%m-%d',
        generator = True,
        strict = True,
        toc_backlinks = None,
        cloak_email_addresses = True,
        initial_header_level = 3,
        stylesheet_path = 'doc/style.css',
    )
    rst = open( 'doc/readme.rst', 'r' ).read()
    html = publish_string( rst, writer_name='html4css1', settings_overrides=settings )
    html = re.sub( '<col.*>\n', '', html )
    html = re.sub( '</colgroup>', '', html )
    open( 'index.html', 'w' ).write( html )
    os.unlink( 'download.txt' )
    os.unlink( 'sources.txt' )
    return

# Command line
if __name__ == '__main__':
    opts, args = getopt.getopt( sys.argv[1:], 'smgtpO' )
    mode = None
    optimize = None
    for o, v in opts:
        if   o == '-s': mode = 's'
        elif o == '-m': mode = 'm'
        elif o == '-g': optimize = 'g'
        elif o == '-t': optimize = 't'
        elif o == '-p': optimize = 'p'
        elif o == '-O': optimize = 'O'
    if not args:
        build( mode, optimize )
    else:
        if args[0] == 'docs':
            docs()
        elif args[0] == 'path':
            util.install_path()
        elif args[0] == 'unpath':
            util.uninstall_path()
        elif args[0] == 'install':
            util.install()
        elif args[0] == 'uninstall':
            util.uninstall()
        else:
            sys.exit( 'Error: unknown option: %r' % sys.argv[1] )

