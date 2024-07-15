class Checking():
    """Методы проверки ответов на запросы"""
    
    @staticmethod
    def check_status_code(result, status_code):
        """Метод проверки статус-кода"""
        assert status_code == result.status_code, f"ОШИБКА, статус-коды различны. Ожидаемый статус-код: {status_code}, фактический статус-код: {result.status_code}."
        print("ОК, фактический и ожидаемый статус-коды совпадают.")

    @staticmethod
    def check_json_fields(result, expected_value):
        """Метод проверки соответствия полей в ответе на запрос"""
        fields = result.json()
        assert list(fields) == expected_value, "ОШИБКА, фактический перечень полей не совпадает с ожидаемым."
        print("ОК, ожидаемый перечень полей совпадает с фактическим.")

    @staticmethod
    def check_json_value(result, field_name, expected):
        """Метод проверки значений полей"""
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected, "ОШИБКА, фактическое значение поля не совпадает с ожидаемым значением.\n"
        print(f"Поле {field_name} содержит значение, совпадающее с ожидаемым значением.")

    @staticmethod
    def check_json_value_word(result, field_name, word):
        """Метод проверки значений полей по слову"""
        check = result.json()
        check_info = check.get(field_name)
        assert word in check_info, "ОШИБКА, результат не содержит ожидаемой подстроки.\n"
        print(f"Подстрока {word} присутствует в поле {field_name}.")