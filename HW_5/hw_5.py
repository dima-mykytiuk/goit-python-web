from multiprocessing import Process, Pool
from threading import Thread
from time import time


def factorize(*number):
    num_list = []
    for i in number:
        for num in range(1, i + 1):
            if i % num == 0:
                num_list.append(num)
    return num_list


def proc_factorize(numbers):
    proc_list = {}
    for number in numbers:
        proc_list[number] = Process(target=factorize, args=(number,))
        proc_list[number].start()


def thread(numbers):
    thread_list = {}
    for number in numbers:
        thread_list[number] = Thread(target=factorize, args=(number,))
        thread_list[number].start()


if __name__ == '__main__':
    nums = [128, 255, 99999, 10651060]
    pool_start = time()
    with Pool(processes=4) as pool:
        print(pool.map(factorize, nums))
    print(f'Pool: {time()-pool_start}')
    thread_start = time()
    thread(nums)
    print(f'Thread: {time() - thread_start}')
    proc_start = time()
    proc_factorize(nums)
    print(f'Process: {time() - proc_start}')
    