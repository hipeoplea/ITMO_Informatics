import time


start_time = time.perf_counter()
for i in range(100):
    import task
    task.task()
print('0:', time.perf_counter() - start_time)

start_time = time.perf_counter()
for i in range(100):
    import dop1
    dop1.dop1()
print('1:', time.perf_counter() - start_time)

start_time = time.perf_counter()
for i in range(100):
    import dop2
    dop2.dop2()
print('2:', time.perf_counter() - start_time)

start_time = time.perf_counter()
for i in range(100):
    import dop3
    dop3.dop3()
print('3:', time.perf_counter() - start_time)