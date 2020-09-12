from random import randint
from threading import Thread
from time import time, sleep

def download_pdf(filename):
    print('Start download %s...' % filename)
    time_to_download_pdf = randint(5, 10)
    sleep(time_to_download_pdf)
    print('%s download success! Take %d seconds' % (filename, time_to_download_pdf))
    
def main():
    start = time()
    # 使用 threading 模組的 Thread 類別來創建 thread
    t1 = Thread (target = download_pdf, args =('test1.pdf',))
    t1.start()

    t2 = Thread (target = download_pdf, args =('test2.pdf',))
    t2.start()

    t1.join()
    t2.join()

    end = time()
    print('Total take %.3f seconds.' % (end - start))

if __name__ == '__main__':
    main()