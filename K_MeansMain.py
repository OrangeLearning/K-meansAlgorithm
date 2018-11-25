"""

    @author: GeekVitaminC
"""
import numpy as np
import K_MeansTool as tool


def K_Means(dataSet, k, dist_function):
    """
    :param dataSet:
    :param k:
    :param distance:
    :param random_center:
    :return:
    """
    xs, ys = dataSet
    # data_n = len(xs)
    n = xs[0].shape[0]
    points = tool.random_K_Point(k, n, xs)
    new_div = tool.divide_cluster(xs, points, dist_function)
    div = np.zeros(new_div.shape)

    while np.sum(new_div - div) != 0:
        print("new_div = ", new_div)
        print("div = ", div)
        div = np.copy(new_div)
        new_points = tool.calc_new_points(xs, div , points)
        new_div = tool.divide_cluster(xs, new_points, dist_function)

    return new_div


def Mytest():
    pass


def main():
    pass


if __name__ == '__main__':
    # main()
    Mytest()
