import os

DEFAULT_SURE = 'Fatiha'
DEFAULT_DATA_FOLDER = 'data/'
DEFAULT_SURE_FOLDER = DEFAULT_DATA_FOLDER + 'sureler/'
DEFAULT_OUTPUT_FOLDER = 'output/'
DEFAULT_SURE_EXTENSION = '.htm.txt'


def mean(xlist):
    total = 0
    for x in xlist:
        total += x
    return int(total / len(xlist))


def check_dir(d):
    p = os.path.join(os.getcwd(), d)
    if not os.path.exists(p) and not os.path.isdir(p):
        os.makedirs(p)


def read_sure(f):
    fname = DEFAULT_SURE_FOLDER + f + DEFAULT_SURE_EXTENSION
    with open(fname, "r", encoding="utf-8") as my_file:
        wlist = my_file.readlines()
    return [x.strip().lower() for x in wlist]
