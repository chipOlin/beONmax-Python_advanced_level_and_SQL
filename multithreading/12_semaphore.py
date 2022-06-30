import concurrent.futures
import random
import threading
import time


def work(semaphore):
    time.sleep(random.randint(5, 10))
    print('Releasing 1 connection')
    semaphore.release()


def connect(semaphore, reached_max_connection):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
        while True:
            connections_counter = 0
            while not reached_max_connection.is_set():
                print(f'\nConnection n={connections_counter}')
                semaphore.acquire()
                connections_counter += 1

                ex.submit(work, semaphore)

                time.sleep(0.8)

            time.sleep(5)


def connection_guard(semaphore, reached_max_connection):
    while True:
        print(f'[guard] semaphore={semaphore._value}')
        time.sleep(1.5)

        if semaphore._value == 0:
            reached_max_connection.set()
            print(f'[guard] Reached max connections!')
            time.sleep(2)
            reached_max_connection.clear()


if __name__ == '__main__':
    max_connections = 10
    reached_max_connection = threading.Event()

    semaphore = threading.Semaphore(value=max_connections)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(connection_guard, semaphore, reached_max_connection)
        executor.submit(connect, semaphore, reached_max_connection)
