import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def my_function(x, y):
    f = np.cos(x*y)*np.cos(np.sqrt(x**2 * y**2))
    return f


def second_graph(x,y,color_line): #my_linestyle, my_marker, step, transparency, width, x, y):
    my_ax = plt.axes()
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

    my_ax.fill_between(x[1], y[1], y[2])
    my_ax.set_facecolor('seashell')
    plt.show()


def main():
    my_fig = plt.figure(figsize=(10, 7))
    ax_3d = my_fig.add_subplot(projection='3d')
    x = np.arange(-np.pi, np.pi, 0.2)
    y = np.arange(-np.pi, np.pi, 0.2)
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = my_function(xgrid, ygrid)  # Наша функция

    ax_3d.contour(xgrid, ygrid, zgrid)
    second_graph(x=xgrid, y=zgrid, color_line='green')
    print(ygrid)
    plt.show()


if __name__ == '__main__':
    main()