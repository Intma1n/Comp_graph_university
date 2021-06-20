import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import *
import numpy as np


def get_func(x,y):
    z = np.sin(x) * np.cos(y)
    return z


def get_xyz(h, minx, maxx, miny, maxy):
    x = [i for i in range(minx, maxx, h)]
    y = [i for i in range(miny, maxy, h)]
    xgrid, ygrid = np.meshgrid(x,y)
    z = list()
    for i in xgrid:
        for j in ygrid:
            z.append(get_func(i,j))
    #y = [get_func(i) for i in x]
    return xgrid, ygrid, z


def set_title(my_ax):
    my_ax.set_title('Лабораторная работа №2')


def set_labels(my_ax):
    my_ax.set_xlabel("X")
    my_ax.set_ylabel('Y')


#def set_text(my_ax):
    #label_string = 'y = sin(x)*cos(y)'
    #my_ax.text(0, 600,120, fontsize = 15, s = label_string)


def get_range_x():
    res = np.arange(0, 2*pi)
    return res


def get_range_y():
    res = np.arange(0, pi)
    return res


def graph(color, step_x, step_y, my_type, xgrid, ygrid):  # color_line, my_linestyle, my_marker, step, transparency, width, minx, maxx, miny, maxy):
    #my_ax = plt.axes()
    my_fig = plt.figure(figsize=(7, 4))
    #my_fig = plt.figure(figsize=(10, 14))
    ax_3d = my_fig.add_subplot(projection = '3d')
    print(xgrid)
    print(ygrid)
    zgrid = get_func(xgrid, ygrid)
    print(zgrid)
    if my_type == 'surface':
        ax_3d.plot_surface(xgrid, ygrid, zgrid, color=color, rstride=step_x, cstride=step_y)  # rstride - step by x, cstride - step by y
    elif my_type == 'scatter':
        ax_3d.scatter(xgrid, ygrid, zgrid, color = color)
    elif my_type == 'wireframe':
        ax_3d.plot_wireframe(xgrid, ygrid, zgrid, cstride=step_y, rstride=step_x, color = color)
    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('y')
    ax_3d.set_zlabel('z')
    set_title(ax_3d)
    #set_text(ax_3d)
    plt.show()
    ax_3d.view_init(zgrid, ygrid)
    plt.show()


def get_linestyle():
    dict_of_linestyles = {
        1: '-',
        2: '--',
        3: '-.',
        4: ':'
    }
    input_string = """Меню выбора стиля линии:
            Нажмите 1, для -
            Нажмите 2, для —
            Нажмите 3, для -.
            Нажмите 4, для :
    Ваш ввод:                                  
        """
    my_style = int(input(input_string) or 1)
    return dict_of_linestyles[my_style]


def get_color():
    dict_of_colors = {
        1: 'blue',
        2: 'red',
        3: 'violet',
        4: 'green',
        5: 'yellow'
    }
    input_string = """Меню выбора цвета графика:
        Нажмите 1, чтобы чтобы цвет графика был голубым (по-умолчанию)
        Нажмите 2, чтобы цвет графика был красным
        Нажмите 3, чтобы цвет графика был фиолетовым
        Нажмите 4, чтобы цвет графика был зеленым
        Нажмите 5, чтобы цвет графика был желтым 
Ваш ввод:                                  
    """
    my_color = int(input(input_string) or 1)
    return dict_of_colors[my_color]


def get_type():
    input_string = 'Введите тип графика (surface, wireframe, scatter): '
    res = str(input(input_string))
    return res


def get_step_x():
    input_string = 'Введите шаг по x: '
    res = int(input(input_string))
    return res

def get_step_y():
    input_string = 'Введите шаг по y: '
    res = int(input(input_string))
    return res


def get_marker():
    dict_of_markers = {
        1: '.',
        2: '_',
        3: 'x',
        4: 'o'
    }
    input_string = """Меню выбора маркера:
            Нажмите 1, для .
            Нажмите 2, для _
            Нажмите 3, для х
            Нажмите 4, для о 
    Ваш ввод:                                  
        """
    my_color = int(input(input_string) or 1)
    return dict_of_markers[my_color]


def get_coef_of_transparency():  # Коэффициент прозрачности
    input_string = "Введите коэффициент прозрачности (от 0.0 до 1.0): "
    res = float(input(input_string) or 1)
    return res


def get_width():
    input_string = "Введите толщину линии: "
    width = float(input(input_string) or 1)
    return width

def checking_odz(x):
    if x<0:
        print('Недопустимое значение для x')
        print('Область допустимых значений для x в данной функции начинается с нуля')
        x = 0
    return x


def get_scatter_x():
    min_x = int(input('Введите минимальное значение для x: '))
    min_x = checking_odz(min_x)
    max_x = int(input('Введите максимальное значение для x: '))
    return min_x, max_x


def get_scatter_y():
    min_y = int(input('Введите минимальное значение для y: '))
    #min_x = checking_odz(min_x)
    max_y = int(input('Введите максимальное значение для y: '))
    return min_y, max_y

def second_graph(x,y,color_line): #my_linestyle, my_marker, step, transparency, width, x, y):
    my_ax = plt.axes()
    set_title(my_ax)
    set_labels(my_ax)
    #x, y = get_xy(step, minx, maxx)
    #set_text(my_ax)
    #x = list(x)
    #y = list(y)
    #print(f'x = {x}. Type(x) = {type(x)}')
    #print(f'y = {y}. Type(y) = {type(y)}')
    #for i in x:
        #for j in y:
            #print(f'i = {i}')
            #print(f'j = {j}')
            #print(f'j[2] = {j[2]}')
            #my_ax.fill_between(i, )
    #for ind, i in enumerate(x):
    #my_ax.set_figwidth(12)
    #my_ax.set_figheight(5)
    my_ax.plot(x, y,
               color=color_line)
               #linestyle=my_linestyle,
               #marker=my_marker,
               #alpha=transparency,
               #linewidth=width)
    plt.grid(True)

    print(f'x = {x}')
    print(f'y = {y}')
    my_new_x = np.linspace(-10,10,100)
    print(f'my_new_x = {my_new_x}')
    #for i in y:
    my_ax.fill_between(x[1], y[1], y[2], where=(y[2]>y[1]))
    my_ax.set_facecolor('seashell')
    plt.show()


def main():
    """
    Пятый вариант
    :return:
    """
    #min_x, max_x = get_scatter_x()
    #min_y, max_y = get_scatter_y()
    my_step_x = get_step_x()
    my_step_y = get_step_y()
    my_color = get_color()
    my_type = get_type()
    x = get_range_x()
    y = get_range_y()

    #y_linestyle = get_linestyle()
    #my_marker = get_marker()
    #my_transp = get_coef_of_transparency()
    #my_width = get_width()
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = get_func(xgrid, ygrid)
    graph(xgrid=xgrid, ygrid=ygrid, color=my_color, step_x = my_step_x, step_y = my_step_y, my_type = my_type)
    second_graph(x=zgrid, y=ygrid, color_line=my_color)
          #my_linestyle=my_linestyle,
          #my_marker=my_marker,
          #tep=my_step,
          #transparency=my_transp,
          #width=my_width,
          #minx = min_x,
          #maxx = max_x,
          #miny = min_y,
          #maxy = max_y)


if __name__ == '__main__':
    main()