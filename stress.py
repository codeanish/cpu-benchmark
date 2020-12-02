import time


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    print("----------------------------------------------------")    
    print(f"Starting single threaded process")
    iterations = range(0,100000)
    start = time.perf_counter()
    for iteration in iterations:
        factorial(900)    
    end = time.perf_counter()
    print(f"Completed single threaded process in {end-start:0.4f} seconds")
    print("----------------------------------------------------")