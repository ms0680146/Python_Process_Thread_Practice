from random import randint
from time import time, sleep

def download_pdf(filename):
    print('Start Download %s' % filename)
    time_to_download_pdf = randint(5, 10)
    sleep(time_to_download_pdf)
    print('%s download success! Take %d seconds' % (filename, time_to_download_pdf))

def main():
    start = time()
    download_pdf('test1.pdf')
    download_pdf('test2.pdf')
    end = time()
    print('Total take %.2f seconds' % (end - start))

if __name__ == '__main__':
    main()