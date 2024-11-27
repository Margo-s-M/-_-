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



