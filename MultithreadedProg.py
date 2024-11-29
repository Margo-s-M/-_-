# import threading
#
# def print_Num():
#     for i in range(5):
#         print(f'Numbers{i}')
#
# def print_Let():
#     for i in 'abcdf':
#         print(f'letters:{i}')
#
# thread1 = threading.Thread(target=print_Num)
# thread2 = threading.Thread(target=print_Let, args=("Liza",))
#
#
# thread1.start()
# thread2.start()
#
# thread1.join()# чекає закінчення процесу
# thread2.join()
#
# print("The end")
#
# import random
# def gen_num(count, numbers):
#     for _ in range(count):
#         numbers.append(random.randint(1,10000))
#
# def sum_num(numbers, res):
#     res ["sum"] = sum(numbers)
# def averege(numbers, res):
#     if numbers:
#         res["averege"] = sum(numbers) / len(numbers)
#     else:
#         res["averege"] =0
#
# def main():
#     count = 10000
#     numbers = []
#     res = {}
#
#     gen_thread = threading.Thread(target=gen_num,args=(count,numbers))
#     gen_thread.start()
#     gen_thread.join()#чекавємо на завершення потоку
#
#     sun_thread = threading.Thread(target=sum_num,args=(numbers ,res))
#     avar_thread = threading.Thread(target=averege,args=(numbers,res))
#
#     sun_thread.start()
#     avar_thread.start()
#
#     sun_thread.join()
#     avar_thread.join()
#
#     print(f"Сума:{["sum"]},середнє: {res["averege"]}")
# main()
# import threading
#
#
# class WordCount():
#     def __init__(self,files):
#         self.files = files
#         self.word_count = {}
#
#     def count_word(self, file_path):
#         try:
#             with open(file_path,"r", encoding="utf-8") as f:
#                 text = f.read()
#                 word = len(text.split())
#                 self.word_count[file_path] = word
#         except Exception as e :
#             print(f"Помилка при читані {file_path}: {e}")
#
#     def paral(self):
#         threads =[]
#
#         for file_path in self.files:
#             thread = threading.Thread(target=self.count_word,args=(file_path,))
#             threads.append(thread)
#             thread.start()
#
#         for thread in threads:
#             thread.join()
#
# def main_2():
#     files = ["file1.txt","file2.txt","file3.txt"]
#     counter = WordCount(files)
#     counter.paral()
#     for file , count in counter.word_count.items():
#         print(f"{file}:{count}слів")
#
# main_2()
#
#
# class MyThread(threading.Thread):
#     def run(self):
#         print("thread is start")#кастимізувати, перевизначити
#
# t = MyThread()
# t.start()
# t.join()
#
# def hello(name):
#     print(f"{name}hello")
# t = threading.Thread(5.0, hello, args="Liza")
# t.start()
# t.cancel()


# import threading
#
# local_data = threading.local()
#
# def process_data():
#     local_data.value = threading.current_thread().name
#
#
#     print(f"Value{threading.current_thread().name} :{local_data.value}")
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=process_data)
#     threads.append(t)
#     t.start()
# for t in threads:
#     t.join()

#pr1
# -ввід користвувача
# -два потоки
# -1потік знахлдить максимум
# -2потік знаходить мінімум
# -вивести результат

import threading


def find_max(numbers):
    maximum = max(numbers)
    print("Maximum:", maximum)


def find_min(numbers):
    minimum = min(numbers)
    print("Minimum:", minimum)


def main():
    numbers = list(map(int, input("Enter number : ").split()))

    max_thread = threading.Thread(target=find_max, args=(numbers,))
    min_thread = threading.Thread(target=find_min, args=(numbers,))

    max_thread.start()
    min_thread.start()

    max_thread.join()
    min_thread.join()

    print("Count completed")


if __name__ == "__main__":
    main()


#pr4


# def search_word(file_path,word):
#     try:
#         with open(file_path, "r",encoding="utf8") as file:
#             content = file.readlines()
#
#
#         found_lines = []
#         for line_number , line in enumerate(content,start=1):
#             if word in line:
#                 found_lines.append(f"{line_number} :{line.strip()}")
#
#         if found_lines:
#             print(f"The word{word} was found")
#

#dz

import threading
import random

def fill_list(numbers, event):
    """Заповнює список випадковими числами."""
    for _ in range(10):
        numbers.append(random.randint(1, 100))
    print(f"Список заповнено: {numbers}")
    event.set()  # Сигнал для інших потоків

def calculate_sum(numbers, event):
    """Обчислює суму елементів списку."""
    event.wait()
    total = sum(numbers)
    print(f"Сума елементів списку: {total}")

def calculate_average(numbers, event):
    """Обчислює середнє арифметичне списку."""
    event.wait()
    average = sum(numbers) / len(numbers) if numbers else 0
    print(f"Середнє арифметичне: {average:.2f}")

if __name__ == "__main__":
    numbers = []
    event = threading.Event()

    fill_thread = threading.Thread(target=fill_list, args=(numbers, event))
    sum_thread = threading.Thread(target=calculate_sum, args=(numbers, event))
    avg_thread = threading.Thread(target=calculate_average, args=(numbers, event))

    fill_thread.start()
    sum_thread.start()
    avg_thread.start()

    fill_thread.join()
    sum_thread.join()
    avg_thread.join()
    print("Обчислення завершено.")



import threading
import random
import math

def fill_file(filename, event):
    """Заповнює файл випадковими числами."""
    with open(filename, "w") as file:
        for _ in range(10):
            file.write(f"{random.randint(1, 20)}\n")
    print(f"Файл {filename} заповнено.")
    event.set()

def find_primes(filename, output_file, event):
    """Знаходить усі прості числа."""
    event.wait()
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    with open(filename, "r") as file:
        numbers = list(map(int, file.readlines()))
    primes = [n for n in numbers if is_prime(n)]
    with open(output_file, "w") as file:
        for prime in primes:
            file.write(f"{prime}\n")
    print(f"Простые числа записаны в файл {output_file}.")


# Создаём событие для синхронизации потоков
event = threading.Event()

# Указываем имена файлов
input_file = "numbers.txt"
output_file = "primes.txt"

# Создаём и запускаем потоки
thread1 = threading.Thread(target=fill_file, args=(input_file, event))
thread2 = threading.Thread(target=find_primes, args=(input_file, output_file, event))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Программа завершена.")