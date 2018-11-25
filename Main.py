"""
    Run process
"""
import K_MeansData as dper
import K_MeansMain as algorithm
import K_MeansTool as tool
import numpy as np


def main():
    data = dper.getIrisData()
    np.random.shuffle(data)
    print(data)
    xs, ys = dper.cutDataSet(data)
    print(xs)
    print(ys)
    div = algorithm.K_Means((xs, ys), 2, tool.Euclid_distance)

    print("cluster : ", div)

    mapper = dict()

    for y in ys:
        if y not in mapper.keys():
            mapper[y] = dict()

    for kind, y in zip(div,ys):
        if kind not in mapper[y].keys():
            mapper[y][kind] = 0
        mapper[y][kind] += 1

    for y in mapper.keys():
        index = np.argmax(np.array(mapper[y].values()))

    print(mapper)




if __name__ == '__main__':
    main()
