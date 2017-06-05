import util
import matplotlib.pyplot as plt


def draw(folder, title, x, y):
    fname = util.DEFAULT_OUTPUT_FOLDER + folder + '/' + title + '.png'
    plt.plot(x, y, 'ro')
    plt.title(title)
    plt.xlabel('words')
    plt.ylabel('distance')
    plt.savefig(fname)
    plt.close()
