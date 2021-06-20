import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def my_function(x, y):
    f = np.cos(x*y)*np.cos(np.sqrt(x**2 * y**2))
    return f


def build_3d_graph(my_type_of_graph, my_color, r_my_step, c_my_step,xgrid,ygrid,zgrid):
    my_fig = plt.figure(figsize=(10, 7))
    ax_3d = my_fig.add_subplot(projection='3d')


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

    #for i in y:
    my_ax.fill_between(x[1], y[1], y[2])
    my_ax.set_facecolor('seashell')
    plt.show()


def main():

    x = np.arange(-np.pi, np.pi, 0.2)
    y = np.arange(-np.pi, np.pi, 0.2)
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = my_function(xgrid, ygrid)  # Наша функция

    my_type_of_graph = input('Enter your graph type(surface, wireframe, scatter, contour): ')
    my_color = input('Enter your color(red,green,blue,yellow): ')
    r_my_step = int(input('Enter your x step: '))
    c_my_step = int(input('Enter your y step: '))
    size_slice = int(input('Enter slice size: '))
    new_xgrid = []
    new_ygrid = []
    new_zgrid = []
    zero_new_zgrid = []
    for i in range(32):
        zero_new_zgrid.append([])
        for j in range(32):
            zero_new_zgrid[i].append(0)

    print(zero_new_zgrid)

    for i in range(size_slice):
        zero_new_zgrid.pop(i)
        zero_new_zgrid.append(zgrid[i])

    build_3d_graph(my_type_of_graph, my_color, r_my_step, c_my_step,xgrid=xgrid, ygrid=ygrid, zgrid=zero_new_zgrid)



if __name__ == '__main__':
    main()