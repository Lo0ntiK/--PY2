from typing import Optional, Union


class Guitar:
    def __init__(self, guitar_type: str,
                 number_of_strings: int):
        ''' Инициализация объекта "Гитара"

        Аргументы:
        guitar_type -- тип
        number_of_strings -- число струн

        Примеры:
        >>> guitar1 = Guitar('acoustic', 6)
        >>> guitar2 = Guitar('bass', 4)

        '''
        if not isinstance(guitar_type, str):
            raise TypeError('Ожидается тип "str"!')
        self.type = guitar_type
        if not isinstance(number_of_strings, int):
            raise TypeError('Число струн - целое, т.е. типа "int".')
        if number_of_strings < 0:
            raise ValueError('Такого не может быть!')
        if number_of_strings == 0:
            raise ValueError('Ну и что это за гитара?')
        self.strings = number_of_strings

    def tune(self) -> None:
        ''' Настройка гитары.

        Примеры:
        >>> guitar = Guitar('electric', 7)
        >>> guitar.tune()

        '''
        ...

    def play(self, song_filename: str) -> None:
        ''' Сыграть песню на гитаре.

        Аргументы:
        song_filename -- путь к файлу с аккордами

        Примеры:
        >>> guitar = Guitar('electric', 7)
        >>> guitar.play('~/Music/song1.txt')

        '''
        if not isinstance(song_filename, str):
            raise TypeError('Ожидается тип "str"!')
        ...


class Cat:
    def __init__(self, cat_name: str,
                 cat_purrs: bool,
                 cat_colour: Optional[str]):
        ''' Инициализация объекта "Кошка"

        Аргументы:
        name -- кличка
        purrs -- мурлычет
        colour -- цвет шерсти (если она есть)

        Примеры:
        >>> kitten = Cat('Pushok', False, 'White')
        >>> cat = Cat('Murka', True, None)

        '''
        if not isinstance(cat_name, str):
            raise TypeError('Кличка типа "str"!')
        self.name = cat_name
        if not isinstance(cat_purrs, bool):
            raise TypeError('Ожидается тип "bool"!')
        self.purrs = cat_purrs
        if not isinstance(cat_colour, str | type(None)):
            raise TypeError('Цвет шерсти или типа "str", или "None"')
        self.colour = cat_colour

    def is_hungry(self) -> bool:
        ''' Функция, которая проверяет, голоден ли кот.

        Примеры:
        >>> cat = Cat('Murzik', False, 'Red')
        >>> cat.is_hungry()

        '''
        ...

    def feed(self) -> None:
        ''' Покормить

        Примеры:
        >>> cat = Cat('Murzik', False, 'Red')
        >>> cat.feed()

        '''
        ...


class SturmLiouvilleProblem:
    def __init__(self, px, qx, rx: Union[int, str],
                 condition1, condition2: int,
                 point1, point2: Union[int, float, str]):
        ''' Инициализация объекта "Задача Штурма-Лиувилля"

        Аргументы:
        px, qx, rx -- функции от x в задаче Штурма-Лиувилля:
                      (p(x)*y')'+[l*r(x)-q(x)]*y=0
        condition1, condition2 -- тип граничных условий
                                  (1, 2 или 3-го рода)
        point1, point2 -- точки отрезка [point1, point2]

        Примеры:
        >>> problem1 = SturmLiouvilleProblem(1, 0, 1, 1, 3, 0, 'a')
        >>> problem2 =SturmLiouvilleProblem('x', 0, 'x', 2, 2, 'a', 'b')

        '''
        if not (isinstance(px, int | str) and
                isinstance(rx, int | str) and
                isinstance(qx, int | str)):
            raise TypeError('Ожидается тип "int" или "str"!')
        self.px = px
        self.rx = rx
        self.qx = qx
        if not (isinstance(condition1, int) and
                isinstance(condition2, int)):
            raise TypeError('Нет такого условия!')
        if not (condition1 in {1, 2, 3} and
                condition2 in {1, 2, 3}):
            raise ValueError('Решаем задачу для условий 1, 2 или 3-го рода')
        self.cond1 = condition1
        self.cond2 = condition2
        if not (isinstance(point1, (int, float, str)) and
                isinstance(point2, (int, float, str))):
            raise TypeError('Ожидается тип "int", "float" или "str"!')
        self.x1 = point1
        self.x2 = point2

    def spectrum(self) -> str:
        ''' Метод находит спектр собственных значений l оператора
        Штурма-Лиувилля.
        Возвращает выражение для l в виде строки.

        Примеры:
        >>> problem = SturmLiouvilleProblem('x^2', 0, 'x^2', 1, 1, 'a', 'b')
        >>> problem.spectrum()

        '''
        ...

    def solve(self) -> str:
        ''' Метод находит нетривиальные решения задачи Штурма-Лиувилля.
        Возвращает выражение для y в виде строки.

        Примеры:
        >>> problem = SturmLiouvilleProblem('x^2', 0, 'x^2', 1, 1, 'a', 'b')
        >>> problem.solve()

        '''
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()

