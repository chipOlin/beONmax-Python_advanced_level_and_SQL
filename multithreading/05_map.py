import concurrent.futures

from multithreading.count_three_sum import read_ints, count_three_sum

if __name__ == '__main__':
    print('started main')

    data = read_ints('..\\data\\1Kints.txt')
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        result = executor.map(count_three_sum, (data, data), ('t1', 't2'))
        for r in result:
            print(f'{r=}')

    print('ended main')
