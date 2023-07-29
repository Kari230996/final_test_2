'''
14. Написать программу, имитирующую работу реестра домашних животных.
В программе должен быть реализован следующий функционал:
14.1 Завести новое животное
14.2 определять животное в правильный класс
14.3 увидеть список команд, которое выполняет животное
14.4 обучить животное новым командам
14.5 Реализовать навигацию по меню
'''


class animals:
    def __init__(self, name):
        self.name = name
        self.team = []

    def add_team(self, team):
        self.team.append(team)

    def team_list(self):
        return self.team


class pets(animals):
    pass


class dogs(pets):
    pass


class cats(pets):
    pass


class hamsters(pets):
    pass


# Функция для создания нового животного

def get_new_animal():
    name = input("Введите имя нового животного: ")
    animal_type = input("Введите вид животного (Собаки/Кошки/Хомяки): ")

    if animal_type == 'Собаки':
        return dogs(name)
    elif animal_type == 'Кошки':
        return cats(name)
    elif animal_type == 'Хомяки':
        return hamsters(name)
    else:
        print("Неподдерживаемый вид животного")
        return None


# Функция для определения животного в правильный класс
def determine_animal_type(animals):
    if isinstance(animals, dogs):
        print(f"{animals.name} - Собака")
    elif isinstance(animals, cats):
        print(f"{animals.name} - Кошка")
    elif isinstance(animals, hamsters):
        print(f"{animals.name} - Хомяк")
    else:
        print("Не удалось определить вид животного")


# Функция для определения животного в правильный класс

def show_team_list(animals):
    print(f"{animals.name} выполняет следующие команды:")
    teams = animals.team_list()

    for team in teams:
        print(f"- {team}")


# Функция для обучения новой команды животного

def learn_team(animals):
    team = input(f"Введите новую команду для {animals.name}: ")
    animals.add_team(team)
    print(f"{animals.name} теперь выполняет новую команду: {team}")


# Основной код программы
if __name__ == "__main__":
    registry = []

    while True:
        print("\nМеню:")
        print("1. Завести новое животное")
        print("2. Определить вид животного")
        print("3. Показать список команд животного")
        print("4. Обучить новой команде животное")
        print("5. Выйти")

        choice = input("Введите номер пункта меню: ")

        if choice == "1":
            new_animal = get_new_animal()
            if new_animal:
                registry.append(new_animal)
                print(f"Животное {new_animal.name} добавлено в реестр")
        elif choice == "2":
            name_of_animal = input("Введите имя животного: ")
            for animal in registry:
                if animal.name == name_of_animal:
                    determine_animal_type(animals)
                    break
            else:
                print("Животное с таким именем не найдено в реестре")
        elif choice == "3":
            name_of_animal = input("Введите имя животного: ")
            for animal in registry:
                if animal.name == name_of_animal:
                    show_team_list(animal)
                    break
            else:
                print("Животное с таким именем не найдено в реестре")
        elif choice == "4":
            name_of_animal = input("Введите имя животного: ")
            for animal in registry:
                if animal.name == name_of_animal:
                    learn_team(animal)
                    break
            else:
                print("Животное с таким именем не найдено в реестре")
        elif choice == "5":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
