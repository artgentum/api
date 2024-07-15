#main_url_of_api = https://api.chucknorris.io/
import requests 

url = "https://api.chucknorris.io/jokes/categories" #URL получения категорий шуток
categories = requests.get(url).json() #присваиваем переменной данные ответа в JSON формате
print(categories) #выводим в терминал все категории

class New_joke1(): #создаем класс для получения шуток
    def __init__(self): #метод для инициализации
        pass
    """Инициализация"""

    def create_joke(self, category): #метод для создания шутки, один из параметров - категория шутки
        """Получение шутки по конкретной категории"""

        url = f"https://api.chucknorris.io/jokes/random?category={category}" #url локально переопределяем, т.к. используем внутри метода
        print(f"URL: {url}")#вывод URL для визуального контроля 
        result = requests.get(url) #присваиваем переменной значения данных ответа на запрос
        
        print(f"Статус-код: {result.status_code}") #выводим статус-код
        assert 200 == result.status_code #проверка на статус-код (если код не равен 200 код исполняться далее не будет) 
        if result.status_code == 200: #проверка на статус-код 200, вывод сообщения в терминал
            print("Успешно, статус код совпадает с ожидаемым")
        else:
            print("Ошибка, статус-код не равен 200")
        if "Chuck" in result.json().get("value"): # проверка на содержание в тексте шутки подстроки "Chuck"
            print("ОК, это шутка про Чака Норриса")
        else: 
            print("Эта шутка не про Чака...")
        result.encoding = "utf-8" #перевод в систему кодирования UTF-8
        print(f"Эта шутка из категории: {category}") #вывод в терминал категории шутки
        print(f"Текст шутки: {result.json().get("value")}") #вывод в терминал текста шутки

number_of_joke = 1 #переменная для счетчика шуток
for category in categories: #цикл для прохода по списку категорий шуток
    joke = New_joke1() #создание экземпляра класса
    print(f"Шутка № {number_of_joke}:") #вывод в терминал порядкового номера шутки
    joke.create_joke(category) #вызов метода по созданию шутки по текущей категории (они меняются на каждом шаге цикла)
    number_of_joke += 1 #увеличение счетчика шуток на 1