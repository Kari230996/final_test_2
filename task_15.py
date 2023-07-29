'''
15.Создайте класс Счетчик, у которого есть метод add(), увеличивающий̆
значение внутренней̆ int переменной̆ на 1 при нажатие “Завести новое
животное” Сделайте так, чтобы с объектом такого типа можно было работать в
блоке try-with-resources. Нужно бросить исключение, если работа с объектом
типа счетчик была не в ресурсном try и/или ресурс остался открыт. Значение
считать в ресурсе try, если при заведения животного заполнены все поля.
'''


class Counter:
    def __init__(self):
        self.value = 0
        self.opened = False

    def add(self):
        if not self.opened:
            raise ValueError(
                "The counter is not in a resource block or the resource is still open")
        self.value += 1

    def __enter__(self):
        if self.opened:
            raise ValueError("The counter is already opened")
        self.opened = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.opened = False


class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


if __name__ == "__main__":
    try:
        with Counter() as counter:
            animals = []
            while True:
                name = input(
                    "Введите имя нового животного (для выхода введите 'exit'): ")
                if name.lower() == "exit":
                    break
                animal = Animal(name)
                animals.append(animal)
                counter.add()

        print("Животные заведены:")
        for animal in animals:
            print(f"- {animal}")

        print(f"Общее количество животных: {counter.value}")

    except ValueError as e:
        print(f"Error: {e}")
