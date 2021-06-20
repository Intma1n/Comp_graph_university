import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def my_function(x, y):
    f = np.cos(x*y)*np.cos(np.sqrt(x**2 * y**2))
    return f


def build_3d_graph(my_type_of_graph, my_color, r_my_step, c_my_step):
    my_fig = plt.figure(figsize=(10, 7))
    ax_3d = my_fig.add_subplot(projection='3d')

    x = np.arange(-np.pi, np.pi, 0.2)
    y = np.arange(-np.pi, np.pi, 0.2)
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = my_function(xgrid, ygrid)  # Наша функция

    if my_type_of_graph == 'surface':
        ax_3d.plot_surface(xgrid, ygrid, zgrid, rstride=r_my_step, cstride=c_my_step, cmap='plasma')

    elif my_type_of_graph == 'wireframe':
        ax_3d.plot_wireframe(xgrid, ygrid, zgrid, rstride=r_my_step, cstride=c_my_step, color=my_color)

    elif my_type_of_graph == 'scatter':
        ax_3d.scatter(xgrid, ygrid, zgrid, color=my_color)

    elif my_type_of_graph == 'contour':
        ax_3d.contour(xgrid, ygrid, zgrid)

    else:
        raise ValueError

    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('y')
    ax_3d.set_zlabel('z')

    plt.show()


def second_graph():
    pass


def main():
    my_type_of_graph = input('Enter your graph type(surface, wireframe, scatter, contour): ')
    my_color = input('Enter your color(red,green,blue,yellow): ')
    r_my_step = int(input('Enter your x step: '))
    c_my_step = int(input('Enter your y step: '))
    build_3d_graph(my_type_of_graph, my_color, r_my_step, c_my_step)


if __name__ == '__main__':
    main()