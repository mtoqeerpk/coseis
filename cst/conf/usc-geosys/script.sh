#!/bin/bash -e

#PBS -N %(name)s
#PBS -M %(email)s
#PBS -l nodes=%(nodes)s:ppn=%(ppn)s
#PBS -l walltime=%(walltime)s
#PBS -e %(rundir)s/%(name)s-err
#PBS -o %(rundir)s/%(name)s-out
#PBS -m abe
#PBS -q mpi
#PBS -V

cd "%(rundir)s"
set > env

echo "$( date ): %(name)s started" >> log
%(pre)s
#mpiexec -n %(nproc)s -machinefile $PBS_NODEFILE %(command)s
mpiexec -n %(nproc)s %(command)s
%(post)s
echo "$( date ): %(name)s finished" >> log
