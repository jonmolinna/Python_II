# Process: An instance of a program (e.g a Python interpreter)

# Takes advantage of multiple CPUs and cores
# Separate memory space -> Memory is not shared between processes
# Great for CPU-bound processing
# New process is stated independently from other processes
# Processes are interruptable/killable
# One gil for each process -> avoids gil limitation

# Heavyweight
# Starting a process is slower than starting a thread
# More memory
# IPC (inter-process communication) is more complicated

#----------------------------------------------------------------------------------------------------

# Threads: An entity within a process that can he scheduled (also know as "leightweight process")
#           A process can spawn multiple threads.

# All threads within a process share the same memory
# Leightweight
# Starting a thread is faster than starting a process
# Great for I/0-bound tasks

# Threading is limited by GIL: Only one thread at a time
# No effect for CPU-bound tasks
# Not interruptable / killable
# Careful with race conditions

#----------------------------------------------------------------------------------------------------

# GIL: Global interpreter lock

# A lock that allows only one thread at a time to execute in python
# Needed in CPython beacuse memory managment in not thread-safe
# Avoid:
#   - Use multiprocessing
#   - Use a different, free-threaded Python implementation (Jython, IronPython)
#   - Use python as a wrapper for third-party libraries (C/C++) -> numpy, scipy


#from multiprocessing import Process
from threading import Thread
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

#processes = []
#num_processes = os.cpu_count()
threads = []
num_threads = 10

# Create processes
#for i in range(num_processes):
    #p = Process(target=square_numbers)
    #processes.append(p)

for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)
    

# Start
#for p in processes:
#    p.start()

for t in threads:
    t.start()

# Join
#for p in processes:
#    p.join()

for t in threads:
    t.join()

print('end main')