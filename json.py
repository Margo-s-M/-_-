# import json
#
# data = {"c":3,"b":6,"a":2,(3,6):6,6:8, None:90}
# #js_str = json.dumps(data,indent=4,sort_keys=True)
# js_str = json.dumps(data, indent =4,skipkeys=True)
# print(js_str)
#
# client ={
#     "name": "VVV",
#     "age": "56",
#     "courser": ["History","Python"],
#     "adress": {"city":"Bro",
#                "code":"07404"
#                }
#
# }
# try:
#     with open("data.json", "w", encoding="utf-8") as file:
#         json.dump(client,file,indent=4,ensure_ascii=False)
#     print("Data is saved")
#     with open("data.json","r", encoding="utf-8") as file:
#         client = json.load(file)
#     print("Дані десерелізовано", data)
# except IOError:
#     print("File error")
# except json.JSONDecodeEror:
#     print("помилка декодування")

# import json
# from  datetime import datetime
# class CustonEncoder(json.JSONEncoder):
#
#     def default(self,obj):
#         if isinstance(obj,datetime):
#             return obj.strftime("%B %d,%Y")
#         return super().default(obj)
# def custom_decoder(dct):
#     for key, value in dct.items():
#         try:
#             dct[key]= datetime.strptime(value,"%B %d %Y")
#         except (ValueError,TypeError):
#             pass
#     return dct
# data = {
#     "name" :"Alice",
#     "data": datetime.now()
# }
# js_string = json.dumps(data, cls=CustonEncoder, indent =4)
# print(js_string)
# dec_data = json.load(js_string, object_hook=custom_decoder)
# print(dec_data)
#
# class Author:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return  f"{self.name}"
#
# class Publish:
#     def __init__(self, name , country):
#         self.name = name
#         self.country = country
#
#     def __str__(self):
#         return f"{self.name},{self.country}"
#
# class Book:
#
#     def __init__(self,title, author,publisher, year):
#         self.title = title
#         self.author = author
#         self.publisher = publisher
#         self.year = year
#
#     def __str__(self):
#         return (f"done")
#
# class CustonEncoder(json.JSONEncoder):
#
#     def default(self, obj):
#         if isinstance(obj,Author):
#             return {"__Author__":True,"name":obj.name}
#         elif isinstance(obj, Author):
#             return {"__Pblish__":True, "name":obj.name,"country": obj.country}
#         elif isinstance(obj,Book):
#             return {
#                 "__Book__": True,
#                 "title":obj.title,
#             "author":obj.author,
#             "publisher":obj.publisher,
#             "year":obj.year}
#
# def custoom_dec(dct):
#     if"__Author__" in dct:
#         return Author(name=dct["name"])
#     elif"__Publish__"  in dct:
#         return Publish(name=dct["name"],country=dct["country"])
#     elif "__Publish__" in dct:
#         return Publish(name=dct["name"],counry=dct["country"])
#     elif "__Book__" in dct:
#         return  Book(
#             title=dct["title"],
#             author=dct["author"],
#             publisher=dct["publisher"],
#             year=dct["year"]
#
#
#         )
#
# library = [
#     Book(title="BookTitle",
#          author=Author(name="Harry"),
#          publisher=Publish(name="Company",country="Ua"),
#          year=1967),
#     Book(title="BookTitle2",
#          author=Author(name="Harry"),
#          publisher=Publish(name="Company2", country="Ua"),
#          year=1997
#          )
# ]
#
# with open("library.json", "a", encoding="utf-8")as file:
#     json.dump(library, file,indent=4,ensure_ascii=False, cls=CustonEncoder)
#
# with open("Library.json", "r",encoding="utf-8") as file:
#     load = json.load(file,object_hook=custoom_dec)
# for book in load:
#     print(book)
#

#pr1

import pickle

class Airplane:
    def __init__(self, model, capacity, range_km, airline):
        self.model = model
        self.capacity = capacity
        self.range_km = range_km
        self.airline = airline

    def fly(self):
        print(f"{self.airline} {self.model} is flying.")

    def display_info(self):
        return f"Model: {self.model}, Capacity: {self.capacity}, Range: {self.range_km} km, Airline: {self.airline}"

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Object saved to {filename} using pickle.")

    @staticmethod
    def load_from_pickle(filename):
        with open(filename, 'rb') as file:
            obj = pickle.load(file)
        print(f"Object loaded from {filename} using pickle.")
        return obj


airplane = Airplane("Boeing 747", 400, 13000, "Lufthansa")
print(airplane.display_info())


airplane.save_to_pickle("airplane.pkl")# Стиснення


loaded_airplane = Airplane.load_from_pickle("airplane.pkl")
print(loaded_airplane.display_info())



import json
# Стиснення у JSON
class AirplaneJSON(Airplane):
    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)
        print(f"Object saved to {filename} using JSON.")

    @staticmethod
    def load_from_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Object loaded from {filename} using JSON.")
        return AirplaneJSON(data['model'], data['capacity'], data['range_km'], data['airline'])


airplane.save_to_json("airplane.json")


loaded_airplane_json = AirplaneJSON.load_from_json("airplane.json")
print(loaded_airplane_json.display_info())


#pr
class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Clock saved to {filename} using pickle.")

    @staticmethod
    def load_from_pickle(filename):
        with open(filename, 'rb') as file:
            obj = pickle.load(file)
        print(f"Clock loaded from {filename} using pickle.")
        return obj

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)
        print(f"Clock saved to {filename} using JSON.")

    @staticmethod
    def load_from_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Clock loaded from {filename} using JSON.")
        return Clock(data['hours'], data['minutes'], data['seconds'])


clock = Clock(12, 30, 45)
print(clock.display_time())


clock.save_to_pickle("clock.pkl")
clock.save_to_json("clock.json")


loaded_clock_pickle = Clock.load_from_pickle("clock.pkl")
loaded_clock_json = Clock.load_from_json("clock.json")
print(loaded_clock_pickle.display_time())
print(loaded_clock_json.display_time())


#pickleдля бінарної серфалізації/дес-ї, робота за складними обєктами
#json для текстової сер-ї , обмін данними між різними системами.

#dz
import json
import pickle

class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        return f"{self.brand} {self.model} ({self.year}) - ${self.price}"

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.__dict__, file)
        print(f"Дані автомобіля збережено у файл {filename} (pickle).")

    @staticmethod
    def load_from_pickle(filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        print(f"Дані автомобіля завантажено з файлу {filename} (pickle).")
        return Car(**data)

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)
        print(f"Дані автомобіля збережено у файл {filename} (json).")

    @staticmethod
    def load_from_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Дані автомобіля завантажено з файлу {filename} (json).")
        return Car(**data)


car = Car("Tesla", "Model S", 2022, 79999)
print(car.display_info())


car.save_to_pickle("car.pkl")
car.save_to_json("car.json")


car_from_pickle = Car.load_from_pickle("car.pkl")
car_from_json = Car.load_from_json("car.json")
print(car_from_pickle.display_info())
print(car_from_json.display_info())


class Stadium:
    def __init__(self, name, location, capacity, year_built):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.year_built = year_built

    def display_info(self):
        return f"{self.name} ({self.year_built}), {self.location} - Capacity: {self.capacity}"

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.__dict__, file)
        print(f"Дані стадіону збережено у файл {filename} (pickle).")

    @staticmethod
    def load_from_pickle(filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        print(f"Дані стадіону завантажено з файлу {filename} (pickle).")
        return Stadium(**data)

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)
        print(f"Дані стадіону збережено у файл {filename} (json).")

    @staticmethod
    def load_from_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Дані стадіону завантажено з файлу {filename} (json).")
        return Stadium(**data)


stadium = Stadium("Camp Nou", "Barcelona, Spain", 99354, 1957)
print(stadium.display_info())


stadium.save_to_pickle("stadium.pkl")
stadium.save_to_json("stadium.json")


stadium_from_pickle = Stadium.load_from_pickle("stadium.pkl")
stadium_from_json = Stadium.load_from_json("stadium.json")
print(stadium_from_pickle.display_info())
print(stadium_from_json.display_info())




class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def display_info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages - ${self.price}"

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.__dict__, file)
        print(f"Дані книги збережено у файл {filename} (pickle).")

    @staticmethod
    def load_from_pickle(filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        print(f"Дані книги завантажено з файлу {filename} (pickle).")
        return Book(**data)

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)
        print(f"Дані книги збережено у файл {filename} (json).")

    @staticmethod
    def load_from_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Дані книги завантажено з файлу {filename} (json).")
        return Book(**data)


book = Book("Python Programming", "John Doe", 350, 29.99)
print(book.display_info())


book.save_to_pickle("book.pkl")
book.save_to_json("book.json")


book_from_pickle = Book.load_from_pickle("book.pkl")
book_from_json = Book.load_from_json("book.json")
print(book_from_pickle.display_info())
print(book_from_json.display_info())

