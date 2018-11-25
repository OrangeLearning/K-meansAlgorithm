"""
    This file is provide data
"""
import numpy as np

data_address = "/home/orangeluyao/Data/data/IrisData/iris2.data"


def loadFile(file):
    xs = []
    ys = []
    with open(file, 'r', encoding="utf-8") as fr:
        lines = fr.readlines()
        for line in lines:
            line = str(line).strip()

            ss = line.split(',')
            tmp = []
            for x in ss[:-1]:
                tmp.append(float(x))

            xs.append(tmp)
            ys.append(ss[-1])

    return (xs, ys)


def getIrisData():
    xs, ys = loadFile(data_address)
    data = [(x, y) for x, y in zip(xs, ys)]
    return data


def cutDataSet(dataSet):
    xs = []
    ys = []
    for data in dataSet:
        xs.append(np.array(data[0]))
        ys.append(data[1])
    return xs, ys


def main():
    xs, ys = loadFile(data_address)


if __name__ == '__main__':
    main()
