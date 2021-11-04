class Initialization:
    def __init__(self, capacity, food):
        if type(capacity) != int:
            print('Количество людей должно быть целым числом')
        else:
            self.capacity = capacity
            self.food = food


class Vegetarian(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'


class MeatEater(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'


class SweetTooth(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'

    def __eq__(self, other):
        if isinstance(other, int):
            return self.capacity == other
        elif isinstance(other, (MeatEater, Vegetarian)):
            return self.capacity == other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {self.capacity}'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.capacity < other
        elif isinstance(other, (MeatEater, Vegetarian)):
            return self.capacity < other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {self.capacity}'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.capacity > other
        elif isinstance(other, (MeatEater, Vegetarian)):
            return self.capacity > other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {self.capacity}'