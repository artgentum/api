import json
from utils.api import Google_maps_api
from utils.checking import Checking

class Test_create_place():
    """Создание, получение информации, изменение данных и удаление локации."""

    def test_create_new_place(self):

        print("""Метод POST""")
        result_post = Google_maps_api.create_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        token = json.loads(result_post.text)
        assert list(token) == ['status', 'place_id', 'scope', 'reference', 'id'], "ОШИБКА, список полей различен с ожидаемым."
        print("Все поля присутствуют!")
        Checking.check_json_value(result_post, 'status', 'OK')
        print("\n")

        print("""Метод GET""")
        result_get = Google_maps_api.get_place(place_id)
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        assert list(token) == ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'], "ОШИБКА, список полей различен с ожидаемым."
        print("Все поля присутствуют!")
        Checking.check_json_value(result_get, 'accuracy', '10')
        print("\n")

        print("Метод PUT")
        result_put = Google_maps_api.change_place(place_id)
        Checking.check_status_code(result_put, 200)
        token = json.loads(result_put.text)
        assert list(token) == ['msg'], "ОШИБКА, список полей различен с ожидаемым."
        print("Все поля присутствуют!")
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')
        print("\n")

        print("""Метод GET после изменения локации""")
        result_get = Google_maps_api.get_place(place_id)
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        print(list(token))
        assert list(token) == ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'], "ОШИБКА, список полей различен с ожидаемым."
        print("Все поля присутствуют!")
        Checking.check_json_value(result_get, 'address', '101, Gagarina avenue, Russia')
        print("\n")
    
        print("Метод DELETE")
        result_delete = Google_maps_api.delete_place(place_id)
        Checking.check_status_code(result_delete, 200)
        token = json.loads(result_delete.text)
        assert list(token) == ['status'], "ОШИБКА, список полей различен с ожидаемым."
        print("Все поля присутствуют!")
        Checking.check_json_value(result_delete, 'status', 'OK')
        print("\n")

        print("Метод GET после удаления локации")
        result_get = Google_maps_api.get_place(place_id)
        Checking.check_status_code(result_get, 404)
        token = json.loads(result_get.text)
        assert list(token) == ['msg'], "ОШИБКА, список полей различен с ожидаемым."
        print("Все поля присутствуют!")
        Checking.check_json_value_word(result_get, 'msg', 'failed')
        print("\n")

        print("Тестирование создания, получения информации, изменения и удаления локации успешно.")