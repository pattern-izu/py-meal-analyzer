import math


def distance(m, f, k):
    x = math.pow(f, 2) - math.pow((m - k), 2)
    return x


def distance2(m, f, k):
    x = math.pow(f, 2) - math.pow((m - k), 2)
    return abs(x)


def distance3(m, f, k):
    x = math.sqrt(abs(math.pow(f, 2) - math.pow((m - k), 2)))
    return abs(x)


def distance4(m, f, k):
    sq = math.sqrt(abs(math.pow(f, 2) - math.pow(m - f, 2)))
    return k - sq


def distances():
    return {"distance_v1": distance,
            "distance_v2": distance2,
            "distance_v3": distance3,
            "distance_v4": distance4}
