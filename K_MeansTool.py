"""
    This file is used for preparing tools for main function
"""

import numpy as np
import random
import time


def Euclid_distance(x: np.ndarray, y: np.ndarray):
    """
        calc the Euclid distance in two arrays
        :param x:
        :param y:
        :return:
    """
    if x.shape != y.shape:
        raise ValueError('vector shape is different !')

    z = (x - y) * (x - y)
    return np.sqrt(np.sum(z))


def random_K_Point(k, n, xs):
    """
    :param k: the number of points
    :param n: ths length of the vector
    :param xs: the data
    :return: points
    """
    random.seed(time.time())

    points = []
    min_s = []
    max_s = []

    for j in range(n):
        tmp = np.array([item[j] for item in xs])
        min_s.append(np.min(tmp))
        max_s.append(np.max(tmp))

    for i in range(k):
        point = []
        for j in range(n):
            delta = max_s[j] - min_s[j]
            point.append(delta * random.random() + min_s[j])

        print("point = ", point)
        points.append(np.array(point))

    return points


def divide_cluster(xs, points, dist_function):
    """

    :param xs:
    :param points:
    :param dist_function:
    :return:
    """
    div = []
    points_n = len(points)
    for x in xs:
        index = 0
        dist = dist_function(points[index], x)
        for k in range(1, points_n):
            d = dist_function(points[k], x)
            if d < dist:
                dist = d
                index = k

        div.append(index)

    return np.array(div)


def get_means(xs):
    """

    :param xs:
    :return:
    """
    if len(xs) == 0:
        return np.array([])
    x_sum = np.zeros(xs[0].shape)
    length = float(len(xs))
    for x in xs:
        x_sum += x

    return x_sum / length


def calc_new_points(xs, div: np.ndarray , pre_points):
    print("in calc_new_points div = ", div)
    points = []

    clusters = [[] for i in range(np.max(div) + 1)]

    # collect clusters
    for i in range(div.shape[0]):
        clusters[div[i]].append(xs[i])

    # calc means
    for i in range(np.max(div) + 1):
        # print("clusters length = ", len(clusters))
        res = get_means(clusters[i])
        if res.shape[0] == 0:
            res = pre_points[i]
        points.append(res)

    return points


def main():
    # print(random_K_Point(3,3))
    pass


if __name__ == '__main__':
    main()
