import pickle
data = [1,2,3,4]
try:
    with open('list.pkl','wb') as file:
        pickle.dump(data,file)
except pickle.PickleError as e:
    print(f"Error{e}")
try:
    with open('list.pkl','rb') as file:
        load_data = pickle.load(file)
except pickle.UnpicklingError as e:
    print(f"Error{e}")

print(load_data,type(load_data))

ser_data = pickle.dumps(data)
print(ser_data)
load_d = pickle.loads(ser_data)
print(load_d)



class CustomClass:
    def __init__(self,value):
        self.value = value

    def __reduce__(self):
        return (self.__class__,(self.value))

    def __str__(self):
        return f"value = {self.value}"

obj = CustomClass(67)
ser = pickle.dump(obj)
print(f"Ser:{ser}")
dser = pickle.load(ser)
print(f"Dser:{dser}")


class CustomClass2:
    def __init__(self,value):
        self.value = value
        self.note = "my note"

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["note"]
        return state
    def __setstate__(self, state):
        self.__dict__.update(state)
        self.note = "new note"

    def __str__(self):
        return f"value ={self.value} , note ={self.note}"
obj = CustomClass2
print(obj)
ser2 = pickle.dump(obj)
print(ser2)
deser2 = pickle.load(ser2)
print(deser2)


#збереження стану кешу
class Cache:
    def __init__(self):
        self.cache_data ={}
        self.expired_data ={}

    def add_to_cache(self,key,value, expired =False):
        if expired:
            self.cache_data[key] = value
        else:
            self.expired_data[key] = value

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["expired_data"]
        return state
    def __setstate__(self, state):
        self.__dict__.update(state)
        self.expired_data = {}

cache =Cache()
cache.add_to_cache("Chrome","data1")
cache.add_to_cache("Exployer","data1",expired=True)
ser = pickle.dumps(cache)
dser = pickle.loads(ser)
print(dser.cache_data)
print(dser.expired_data)

#pr1

class UserInfo:
    def __init__(self):
        self.users ={}

    def add_user(self,login,password):
        if login in self.users:
            return login
        else:
            self.users[login] = password
            print(f"User '{login}' added successfully.")
    def delet_user(self,login):
        if login in self.users:
            del self.users[login]
            print(f"User {login} was successfully removed ")
        else:
            print(f"User {login} doesn`t exist")

    def find_user(self,login):
        if login in self.users:
            print({login},{self.users[login]})
        else:
            print(f"User {login} not found")

    def change_pass(self,login,new_pass):
        if login in self.users:
            self.users[login] = new_pass
            print(f"Password for user{login} changed successfully")

    def save_in_file(self,file_n):
        with open(file_n, 'wb') as file:
            pickle.dump(self.users,file)
            print(f"info saved to {file_n}")

    def load_file(self,file_n):
        with open(file_n, "rb") as file:
            self.users = pickle.load(file)
            print(f"info loaded from {file_n}")


user_d =UserInfo()
user_d.add_user("Milly", "8888")
user_d.add_user("Hamster","7777")

user_d.find_user("Milly")

user_d.change_pass("Milly",1111)

user_d.delet_user("Hamster")

user_d.save_in_file("output.pkl")

user_d.load_file("output.pkl")


#pr2

class UserSession:
    def __init__(self, username, token, data):
        self.username = username
        self.token = token
        self.data = data

    def __getstate__(self):

        state = self.__dict__.copy()
        if "token" in state:
            del state["token"]
        return state

    def __setstate__(self, state):
         self.__dict__.update(state)
         self.token = None


session = UserSession("Bob", "token_333", {"last_login": "2024-11-22"})

serialized_session = pickle.dump(session)
print("Серіалізований об'єкт:", serialized_session)

deserialized_session = pickle.load(serialized_session)
print("Відновлений об'єкт:")
print("Ім'я користувача:", deserialized_session.username)
print("Дані:", deserialized_session.data)
print("Токен:", deserialized_session.token)

#pr
class DatabaseConnection:
    def __init__(self, db_name, host, user, password):
        self.db_name = db_name
        self.host = host
        self.user = user
        self.password = password

    def __getstate__(self):
        pass

    def __setstate__(self, state):
        pass





music_library = {}


def add_band(band, albums):
    music_library[band] = albums
    print(f"Додано: {band} -> {albums}")


def remove_band(band):
    if band in music_library:
        del music_library[band]
        print(f"Видалено: {band}")
    else:
        print(f"Виконавець '{band}' не знайдений.")


def search_band(band):
    if band in music_library:
        print(f"Альбоми {band}: {music_library[band]}")
    else:
        print(f"Виконавець '{band}' не знайдений.")

def edit_band(band, new_albums):
    if band in music_library:
        music_library[band] = new_albums
        print(f"Альбоми {band} оновлено на: {new_albums}")
    else:
        print(f"Виконавець '{band}' не знайдений.")

#збереження
def save_library(filename):
    pass

# завантаження
def load_library(filename):
    pass

#PR

class TaskQueue:
    def __init__(self):
        self.tasks = []  # Черга завдань
        self.completed = []  # Список завершених завдань

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Завдання '{task}' додано до черги.")

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.completed.append(task)
            print(f"Завдання '{task}' позначено як завершене.")
        else:
            print(f"Завдання '{task}' не знайдено в черзі.")

    def show_tasks(self):
        if not self.tasks:
            print("Черга завдань порожня.")
        else:
            print("Незавершені завдання:")
            for task in self.tasks:
                print(f"- {task}")

    def __getstate__(self):
        state = self.__dict__.copy()
        state['completed'] = []  # Не серіалізуємо завершені завдання
        return state

    def __setstate__(self, state):
        self.__dict__ = state
        print("Стан черги завдань відновлено.")

queue = TaskQueue()
queue.add_task("Task 1")
queue.add_task("Task 2")
queue.add_task("Task 3")

queue.complete_task("Task 2")

queue.show_tasks()


serialized_queue = pickle.dumps(queue)
print("\nЧерга завдань серіалізована.")

deserialized_queue = pickle.loads(serialized_queue)
print("\nЧерга завдань десеріалізована:")
deserialized_queue.show_tasks()
