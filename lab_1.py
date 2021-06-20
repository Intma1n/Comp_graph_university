import matplotlib.pyplot as plt
from math import *


class DrawGraph:
    def __init__(self,  my_color,  my_marker, my_linestyle, my_transparency, my_width, min_x, max_x, my_step):
        self.color_dict = {
            1: 'blue',
            2: 'red',
            3: 'violet',
            4: 'green',
            5: 'yellow'
        }
        self.my_color = my_color

        self.marker_dict = {
            1: '.',
            2: '_',
            3: 'x',
            4: 'o'
        }
        self.my_marker = my_marker

        self.linestyles_dict = {
            1: '-',
            2: '--',
            3: '-.',
            4: ':'
        }
        self.my_linestyle = my_linestyle

        self.my_transparency = my_transparency

        self.my_width = my_width



        self.min_x = min_x

        self.max_x = max_x

        self.my_step = my_step


    my_color = property()
    my_marker = property()
    my_linestyle = property()
    my_transparency = property()
    my_width = property()
    min_x = property()
    max_x = property()
    my_step = property()

    @my_width.setter
    def my_width(self, value):
        if not isinstance(value, float):
            raise ValueError
        else:
            self.__my_width = value

    @my_width.getter
    def my_width(self):
        return self.__my_width

    @my_transparency.setter
    def my_transparency(self, value):
        if value>1.0 or value<0.0:
            value = 1.0
        elif not isinstance(value, float):
            raise ValueError
        self.__my_transparency = value

    @my_transparency.getter
    def my_transparency(self):
        return self.__my_transparency

    @my_step.setter
    def my_step(self, value):
        if not isinstance(value, int):
            raise ValueError
        self.__my_step = value

    @my_step.getter
    def my_step(self):
        return self.__my_step

    @min_x.setter
    def min_x(self, value):
        if not isinstance(value, int):
            print(value)
            raise ValueError
        self.__min_x = value

    @min_x.getter
    def min_x(self):
        return self.__min_x

    @max_x.setter
    def max_x(self, value):
        if not isinstance(value, int):
           raise ValueError
        self.__max_x = value

    @max_x.getter
    def max_x(self):
        return self.__max_x

    @my_color.setter
    def my_color(self, value):
        if not isinstance(value, int):
            print(value)
            raise ValueError
        else:
            self.__my_color = self.color_dict[value]

    @my_marker.setter
    def my_marker(self, value):
        if not isinstance(value, int):
            print(value)
            raise ValueError
        else:
            self.__my_marker = self.marker_dict[value]

    @my_linestyle.setter
    def my_linestyle(self, value):
        if not isinstance(value, int):
            raise ValueError
        else:
            self.__my_linestyle = self.linestyles_dict[value]

    @my_linestyle.getter
    def my_linestyle(self):
        return self.__my_linestyle

    @my_marker.getter
    def my_marker(self):
        return self.__my_marker

    @my_color.getter
    def my_color(self):
        return self.__my_color

    @staticmethod
    def apply_function(i):
        res = 10**(-3)*(abs(i))**2.5+log(abs(i+35.4))
        return res

    @staticmethod
    def get_all_x(minx, maxx, step):
        res = [i for i in range(minx, maxx, step)]
        return res

    @staticmethod
    def get_all_y(my_x):
        res = [DrawGraph.apply_function(i) for i in my_x]
        return res

    def draw_line(self):
        my_x = DrawGraph.get_all_x(minx=self.min_x,
                                   maxx=self.max_x,
                                   step=self.my_step)
        my_y = DrawGraph.get_all_y(my_x)
        ax = plt.axes()
        ax.set_title('Лабораторная работа №1')
        ax.set_xlabel("X")
        ax.set_ylabel('Y')
        label_string = '10**(-3)*(abs(i))**2.5+log(abs(i+35.4))'
        ax.text(0, 600, f'{label_string}', fontsize=15)
        ax.plot(my_x, my_y,
                color=self.my_color,
                linestyle=self.my_linestyle,
                marker=self.my_marker,
                alpha=self.my_transparency,
                linewidth=self.my_width)
        plt.grid(True)
        plt.show()

    def __str__(self):
        return f'my_marker = {self.__my_marker},' \
               f'my_color = {self.__my_color}'\
               f'my_linestyle = {self.__my_linestyle}' \
               f'my_transparency = {self.__my_transparency}' \
               f'my_width = {self.__my_width}'\
               f'min_x = {self.__min_x}' \
               f'my_step = {self.__my_step}' \
               f'max_x = {self.__max_x}'


def main():
    my_marker = int(input('Тип маркера (1, - . ;2, - _ ; 3, - х ; 4 - о  ) маркера: '))
    my_color = int(input('Цвет(1-синий, 2 -красный, 3 - фиолетовый, 4 - зеленый, 5 - желтый): '))
    my_linestyle = int(input('Тип линии(1 - -, 2 - --, 3 - -., 4 - :): '))
    my_transparency = float(input('Прозрачность:'))
    my_width = float(input('Толщина: '))
    min_x = int(input('Минимальный х: '))
    max_x = int(input('Максимальный х:'))
    my_step = int(input('Шаг:'))
    my_graph = DrawGraph(my_color, my_marker, my_linestyle, my_transparency, my_width, min_x, max_x, my_step)
    print(my_graph)
    my_graph.draw_line()


if __name__ == '__main__':
    main()