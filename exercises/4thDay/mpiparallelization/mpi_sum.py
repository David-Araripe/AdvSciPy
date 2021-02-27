from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

result = 1
data = rank
data = comm.gather(data, root=0)
if rank == 0:
    for i in range(size):
        result = result + i
    print("Rank of this process is: ", rank)
    print("The sum of all ranks is: ", result)
    print("Ranks are: ", data)
else:
    assert data is None
