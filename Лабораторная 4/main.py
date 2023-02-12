from typing import Union
from math import pi


class Hyperserface:
    def __init__(self, dimension: int) -> None:
        ''' Инициализация объекта "Гиперповерхность"
        
        Аргументы:
        dimension -- размерность гиперповерхности

        Примеры:
        >>> surface1 = Hyperserface(3)
        >>> surface2 = Hyperserface(1)
        
        '''
        self.dim = dimension

    @property
    def dim(self) -> int:
        return self._dim    # непубличный атрибут

    @dim.setter     #dim можно поменять, если выполняются все условия
    def dim(self, set_dim: int) -> None:
        if not isinstance(set_dim, int):
            raise TypeError('Ожидается тип "int"')
        if set_dim < 0:
            raise ValueError('Ожидается размерность >= 0')
        self._dim = set_dim
        
    def __str__(self) -> str:
        ''' Магический метод.

        Пример:
        >>> surface1 = Hyperserface(2)
        >>> print(surface1)
        Гиперповерхность размерности 2

        '''
        return f'Гиперповерхность размерности {self.dim}'

    def __repr__(self) -> str:
        ''' Магический метод.

        Пример:
        >>> surface1 = Hyperserface(2)
        >>> print(repr(surface1))
        Hyperserface(dimension=2)

        '''
        return f'{self.__class__.__name__}(dimension={self.dim})'

    def print_space_dim(self) -> None:
        ''' Метод выводит размерность евклидова пространства,
        в котором задана гиперповерхность.
        
        Примеры:
        >>> surface1 = Hyperserface(2)
        >>> surface1.print_space_dim()
        3

        >>> surface2 = Hyperserface(0)
        >>> surface2.print_space_dim()
        1

        '''
        print(self.dim + 1)

    def area(self) -> None:
        ''' Метод выводит площадь поверхности, если вызван в
        дочернем классе. Т.к. не всякая поверхность имеет конечную
        площадь, то она рассчитывается для каждой гиперповерхности
        отдельно.
            
        '''
        print(f'Гиперповерхность неопределена.')


class Hypersphere(Hyperserface):
    def __init__(self, dim: int, rad: Union[int, float]) -> None:
        ''' Инициализация объекта "Гиперсфера", принадлежащего классу,
        производному от класса Hyperserface.

        Аргументы:
        dim -- размерность гиперсферы
        rad -- её радиус

        Примеры:
        >>> sphere1 = Hypersphere(4, 7)
        >>> sphere2 = Hypersphere(1, 5e-8)

        '''
        super().__init__(dimension=dim)
        self.radius = rad

    @property
    def radius(self) -> Union[int, float]:
        return self._rad    # непубличный атрибут

    @radius.setter     # radius можно поменять, если выполняются все условия
    def radius(self, set_rad: Union[int, float]) -> None:
        if not isinstance(set_rad, int | float):
            raise TypeError('Ожидается тип "int" или "float"')
        if set_rad <= 0:
            raise ValueError('Радиус должен быть больше 0')
        self._rad = set_rad
        
    def __str__(self) -> str:
        ''' Магический метод.

        Пример:
        >>> sphere1 = Hypersphere(2, 40)
        >>> print(sphere1)
        Гиперфера размерности 2 с радиусом 40

        '''
        return f'Гиперфера размерности {self.dim} с радиусом {self.radius}'
        
    def __repr__(self) -> str:
        ''' Магический метод.

        Пример:
        >>> sphere1 = Hypersphere(3, 1.1)
        >>> print(repr(sphere1))
        Hypersphere(dim=3, rad=1.1)

        '''
        return f'{self.__class__.__name__}(dim={self.dim}, rad={self.radius})'

    def area(self) -> Union[int, float]:
        ''' Метод возвращает площадь поверхности гиперсферы.

        Примеры:
        >>> sphere1 = Hypersphere(2, 1)
        >>> print(sphere1.area())
        12.57

        >>> sphere2 = Hypersphere(3, 2)
        >>> print(sphere2.area())
        157.91

        '''

        def recursive(n, r) -> Union[int, float]:
            if n == 0:
                return 2
            elif n == 1:
                return 2*pi*r
            else:
                return 2*pi*r**2/(n-1)*recursive(n-2, r)

        return round(recursive(self.dim, self.radius), 2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

