from multiprocessing import Pool
import time
import os


def call_factorial(n):
    factorial(900)

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    print("----------------------------------------------------")
    cpu_count = os.cpu_count()
    print(f"Starting multi threaded process on {cpu_count} threads")
    pool = Pool(cpu_count)
    start = time.perf_counter()
    pool.map(call_factorial, range(1000000))
    end = time.perf_counter()
    print(f"Completed multi threaded process in {end-start:0.4f} seconds")
    print("----------------------------------------------------")