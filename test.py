import numpy as np
import matplotlib.pyplot as plt


def my_function(x):
    f = np.cos(x) * np.cos(np.sqrt(x ** 2))
    return f


def my_3d_function(x, y):
    f = np.cos(x * y) * np.cos(np.sqrt(x ** 2 * y ** 2))
    return f




def fill_graph():
    my_fig = plt.figure(figsize=(10, 7))
    ax_3d = my_fig.add_subplot(projection='3d')
    fig, ax = plt.subplots()
    my_ax = plt.axes()

    # x = np.arange(-np.pi, np.pi, 0.2)
    # y = np.arange(-np.pi, np.pi, 0.2)
    # xgrid, ygrid = np.meshgrid(x, y)
    # zgrid = my_function(xgrid, ygrid)

    x = np.linspace(-np.pi, np.pi, 30)
    y = np.linspace(-np.pi, np.pi, 30)

    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = my_3d_function(xgrid, ygrid)  # Наша функция

    ax_3d.plot_wireframe(xgrid, ygrid, zgrid)

    my_ax.plot(ygrid, zgrid)
    for i in range(len(ygrid)):
         my_ax.fill_between(xgrid[i], zgrid[i], zgrid[5])
    my_ax.set_facecolor('seashell')

    fig.set_facecolor('floralwhite')
    ax.set_facecolor('seashell')

    plt.show()


def main():
    fill_graph()


if __name__ == '__main__':
    main()
