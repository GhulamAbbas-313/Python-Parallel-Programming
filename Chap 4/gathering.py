# gathering.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = (rank + 1) ** 2  # Example: square of (rank+1)

gathered_data = comm.gather(data, root=0)

if rank == 0:
    print("Rank = %s : gathered data = %s" % (rank, gathered_data))
    print("\n[Reacting data to other processes]")
    for i in range(1, size):
        value = gathered_data[i]
        print("Process %s reacting %s from process %s" % (rank, value, i))