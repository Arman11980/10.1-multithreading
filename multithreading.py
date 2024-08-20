from threading import Thread
from time import sleep
from datetime import datetime

def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print((f'Завершилась запись в файл {file_name}'))

time_start_1 = datetime.now()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end_1 = datetime.now()

print(f'Работа функций {time_end_1 - time_start_1}')

time_start_2 = datetime.now()

thr_first = Thread(target= wite_words, args=(10, 'example5.txt'))
thr_second = Thread(target= wite_words, args=(30, 'example6.txt'))
thr_three = Thread(target= wite_words, args=(200, 'example7.txt'))
thr_four = Thread(target= wite_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_three.start()
thr_four.start()

thr_first.join()
thr_second.join()
thr_three.join()
thr_four.join()

time_end_2 = datetime.now()

print(f'Работа потоков{time_end_2 - time_start_2}')