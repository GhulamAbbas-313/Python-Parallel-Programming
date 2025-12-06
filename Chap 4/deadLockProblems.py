# deadLockProblems.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Example of a potential deadlock situation with blocking sends
if rank == 0:
    data = 123
    comm.send(data, dest=1, tag=11)
    received = comm.recv(source=1, tag=12)
    print("Rank 0 received:", received)
elif rank == 1:
    data = 456
    comm.send(data, dest=0, tag=12)
    received = comm.recv(source=0, tag=11)
    print("Rank 1 received:", received)