from multiprocessing import Process, Value
from time import sleep,localtime,strftime

def process(id, counter):
    local_time = 0
    while True:
        # Request critical section
        t = localtime()
        current_time = strftime("%H:%M:%S", t)
        local_time += 1
        counter.value = local_time
        print(f"Process {id} requests the critical section (timestamp {current_time})")
        sleep(1)

        # Enter critical section
        time = strftime("%H:%M:%S",localtime())
        print(f"Process {id} enters the critical section (timestamp {time})")
        sleep(3)

        # Release critical section
        time = strftime("%H:%M:%S",localtime())
        print(f"Process {id} releases the critical section (timestamp {time})")
        counter.value = 0
        sleep(1)

if __name__ == '__main__':
    num_processes = 3
    counter = Value('i', 0)
    processes = [Process(target=process, args=(i, counter)) for i in range(num_processes)]
    for p in processes:
        p.start()
        sleep(2)
    for p in processes:
        p.join()
