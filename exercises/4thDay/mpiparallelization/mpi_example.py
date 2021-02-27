# a. Write a simple MPI script mpi_ranks.py that prints the rank of the different processes when running
# mpirun python mpi_ranks.py
# b. Write a small script mpi_sum.py which calculates the sum over all ranks and prints the result from the process with rank 0.
import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
randNum = numpy.zeros(1)
if rank == 1:
    randNum = numpy.random.random_sample(1)
    print("Process", rank, "drew the number", randNum[0])
    comm.Send(randNum, dest=0)
if rank == 0:
    print("Process", rank, "before receiving has the number", randNum[0])
    comm.Recv(randNum, source=1)
    print("Process", rank, "received the number", randNum[0])