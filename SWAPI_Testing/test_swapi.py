import requests

class Test_SW():
    """Класс для работы с SW API"""

    def test_Darth_Vader(self):
        """Метод для тестирования API"""

        result_get = requests.get("https://swapi.dev/api/people/4/") #запрос GET по персонажу 
        token_dv = result_get.json() #информация о персонаже Дарт Вейдер
        films = token_dv.get('films') #массив с URL всех фильмов, где был персонаж ДВ
        array_of_characters = [] #массив для хранения персонажей фильмов
        
        for film in films: #прохождение по массиву URL
            result_get_film = requests.get(film) #запрос GET по фильму
            characters_of_the_film = result_get_film.json().get("characters") #получение списка персонажей конкретного фильма
            array_of_characters.extend(characters_of_the_film) #добавление персонажей конкретного фильма в общий массив ВСЕХ персонажей

        f = open('text.txt', 'a', encoding='utf-8')# открытие файла для записи и установка кодировки
        set_of_characters = set(array_of_characters) #при помощи множества убираем дубликаты персонажей (все значения массива становятся уникальными)
        
        for character in set_of_characters: #прохождение по всем URL персонажей 
            result_get_character = requests.get(character) #запрос GET по персонажу
            token_of_character = result_get_character.json() #получение токена по конкретному персонажу
            name_of_character = token_of_character.get("name") #получение имени персонажа
            f.write(name_of_character + "\n") #запись имени персонажа в текстовый файл
        
        f.close() #закрытие файла