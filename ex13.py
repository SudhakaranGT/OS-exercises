import threading
import random

global x  # Shared Data
x = 0
readers_count = 0
write_lock = threading.Lock()
read_lock = threading.Lock()
printcondition = threading.Condition()


def Reader(reader_num):
    global x, readers_count
    with printcondition:
        while readers_count == -1:
            printcondition.wait()
        print(f'Reader {reader_num} is waiting')
        readers_count += 1
    print(f"Reader {reader_num} is Reading!")
    print('Shared Data:', x)
    print()
    with printcondition:
        readers_count -= 1
        if readers_count == 0:
            printcondition.notify()  # Notify waiting writers
    print("No readers are reading")
    print()


def Writer(writer_num):
    global x
    global readers_count
    with printcondition:
        while readers_count > 0:
            printcondition.wait()
        print(f'Writer {writer_num} is waiting')
        readers_count = -1  # Mark that a writer is active
    print(f'Writer {writer_num} is Writing!')
    x += 1  # Write on the shared memory
    with printcondition:
        readers_count = 0
        printcondition.notify()  # Notify waiting readers
    print(f'Writer {writer_num} is Releasing the lock!')
    print()


if __name__ == '__main__':
    reader_threads = [threading.Thread(target=Reader, args=(i + 1,)) for i in range(5)]
    writer_threads = [threading.Thread(target=Writer, args=(i + 1,)) for i in range(5)]
    all_threads = reader_threads + writer_threads
    random.shuffle(all_threads)
    for thread in all_threads:
        thread.start()
    for thread in all_threads:
        thread.join()
