#main_url_of_api = https://api.chucknorris.io/
import requests 

class New_joke2(): #создаем класс для получения шуток
    def __init__(self): #метод для инициализации
        pass
    """Инициализация"""

    def create_joke(self, category):
        """Метод получения шутки по конкретной категории"""

        url = f"https://api.chucknorris.io/jokes/random?category={category}"
        print(f"URL: {url}")#вывод URL для визуального контроля 
        result = requests.get(url) #присваиваем переменной значения данных ответа на запрос
        
        print(f"Статус-код: {result.status_code}") #выводим статус-код
        assert 200 == result.status_code #проверка на статус-код (если код не равен 200 код исполняться далее не будет) 
        if result.status_code == 200: #проверка на статус-код 200, вывод сообщения в терминал
            print("Успешно")
        else:
            print("Безуспешно, статус-код не равен 200")
        if "Chuck" in result.json().get("value"): # проверка на содержание в тексте шутки подстроки "Chuck"
            print("Все хорошо, это шутка про Чака Норриса")
        else: 
            print("Эта шутка не про Чака...")
        result.encoding = "utf-8" #перевод в систему кодирования UTF-8
        print(f"Эта шутка из категории: {category}") #вывод в терминал категории шутки
        print(f"Текст шутки: {result.json().get("value")}") #вывод в терминал текста шутки
        
# category = input("Введите категорию шутки: ") #ввод пользователем необходимой категории
category = 'sport'
url = "https://api.chucknorris.io/jokes/categories" #URL получения категорий шуток
categories = requests.get(url).json() #присваиваем переменной данные ответа в JSON формате
if category in categories: #проверка наличия введенной категории в списке существующих категорий
    joke = New_joke2() # создание экземпляра класса
    joke.create_joke(category) #вызов метода по созданию шутки по текущей категории (они меняются на каждом шаге цикла)
else: 
    print(f"К сожалению, данная категория в перечне доступных категорий шуток отсутствует.\nОзнакомьтесь с перечнем доступных категорий: {categories}") #сообщение, что такой категории нет; вывод пользователю доступных категорий