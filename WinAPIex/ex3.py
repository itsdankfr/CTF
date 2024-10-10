import os
import psutil
import threading
import time

def count_words(results):
    start = time.time()

    with open(r"D:\ISP\xor_formatted.txt", 'r', encoding='utf-8') as file:
        word_count = len(file.read().split())
    results['Thread 1'] = time.time() - start

def count_files(results):
    start = time.time()
    file_count = len([name for name in os.listdir() if os.path.isfile(name)])
    results['Thread 2'] = time.time() - start

def count_threads(results):
    start = time.time()
    for proc in psutil.process_iter(['name']):
        if proc.info['name'].lower() == 'explorer.exe':
            thread_count = proc.num_threads()
            break
    results['Thread 3'] = time.time() - start

# Em cảm giác set up như này chưa phải là chạy đua do thực thi mỗi cái 1 lúc thế này thì biết cái nào nhanh hơn =))
# em định cho nó đếm tgian thực thi rồi lấy trừ đi mà trông k khả thi lắm ạ bài này mong được a chữa sâu hơn
def run_threads():
    results = {}
    threads = [
        threading.Thread(target=count_words, args=(results,)),
        threading.Thread(target=count_files, args=(results,)),
        threading.Thread(target=count_threads, args=(results,))
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    for thread, time_taken in results.items():
        print(f"{thread}: {time_taken:.2f}s")

if __name__ == "__main__":
    run_threads()
