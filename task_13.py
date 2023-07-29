'''13.Создать класс с Инкапсуляцией методов и наследованием по диаграмме.'''

# Родительский класс Животное


class animals:
    def __init__(self, name, team, birthdate):
        self.__name = name
        self.__team = team
        self.__birthdate = birthdate

        def get_name(self):
            return self.__name

        def get_team(self):
            return self.__team

        def get_birthdate(self):
            return self.__birthdate

# Класс Домашние животные, наследуем от Животное


class pets(animals):
    def __init__(self, name, team, birthdate):
        super().__init__(name, team, birthdate)

# Класс Вьючные животные, наследуем от Животное


class pack_animals(animals):
    def __init__(self, name, team, birthdate):
        super().__init__(name, team, birthdate)

# Класс Собаки, наследуем от Домашние_животные


class dogs(pets):
    def __init__(self, name, team, birthdate):
        super().__init__(name, team, birthdate)


# Класс Кошки, наследуем от Домашние_животные
class cats(pets):
    def __init__(self, name, team, birthdate):
        super().__init__(name, team, birthdate)


# Класс Хомяки, наследуем от Домашние_животные
class hamsters(pets):
    def __init__(self, name, team, birthdate):
        super().__init__(name, team, birthdate)

# Класс Лошади, наследуем от Вьючные_животные


class horses(pack_animals):
    def __init__(self, name, team, birthdate):
        super().__init__(name, team, birthdate)

# Класс Верблюды, наследуем от Вьючные_животные


class camels(pack_animals):
    def __init__(self, name, team, birthdate):
        super().__init__(name, team, birthdate)

# Класс Ослы, наследуем от Вьючные_животные


class donkeys(pack_animals):
    def __init__(self, name, team, birthdate):
        super().__init__(name, team, birthdate)
