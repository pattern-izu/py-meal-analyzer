import os
import cryp as cr
import distance as dist
from graph import draw
import util


def data(h, xaxis, d):
    m = util.mean(xaxis)
    result = {
        "x": xaxis,
        "y": [d(m, h, x) for x in xaxis]
    }
    return result


def runall():
    for file in os.listdir(util.DEFAULT_SURE_FOLDER):
        sure = file.split('.')[0]
        run(sure)


def run(sure=util.DEFAULT_SURE):
    datas = util.read_sure(sure)
    for cfolder, cryp in cr.cryps().items():
        for dfolder, dfunc in dist.distances().items():
            folder = os.path.join(cfolder, dfolder)
            c = cryp(sure)
            wordlist = [cryp(x.strip().lower()) for x in datas]
            x = data(c, wordlist, dfunc)
            util.check_dir(folder)
            draw(folder, sure, x['x'], x['y'])
            print('executed ' + os.path.join(cfolder, dfolder))
