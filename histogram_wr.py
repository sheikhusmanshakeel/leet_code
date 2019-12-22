import typing as t

"""
    Histogram
    Some of our data have integers ranges that need need some kind of quality check.
    Creating histograms is a good way to do this so we need a
    python script that will create an histogram, from a data set
    That script will be called by other scripts when needed and
    will need to return a the histogram (a list) and the bucket edges (a list of tuples).

    You will only need to implement the creation of the histogram

    Example input 1:
        arr = [0, 3, 2, 6, 7, 1, 3, 50, 5]
        num_bucket = 10

    Example output:
        histogram - [5, 3, 0, 0, 0, 0, 0, 0, 0, 1]
        edges - [(0, 5), (5, 10), (10, 15), (15, 20), (20, 25), (25, 30),
                  (30, 35), (35, 40), (40, 45), (45, 50)]
        note that each bin is equally sized (in this case, it's 5)

    Example input 2:
        arr = [1, 3, 2, 6, 9, 1, 3, 3, 5]
        num_bucket = 5

    Example output:
        histogram - [3, 3, 1, 1, 1]
        edges - [(1, 2.6), (2.6, 4.2), (4.2, 5.8), (5.8, 7.4), (7.4, 9.0)]
"""


def histogram(data: t.List, number_of_buckets: int):
    # calculate the number of buckets
    min_val, max_val = min(data), max(data)
    width = (max_val - min_val) / number_of_buckets
    list_edges = []
    for i in range(number_of_buckets):
        left_edge = min_val+ (i* width)
        right_edge = width*(i + 1)
        t = (left_edge, right_edge)
        list_edges.append(t)
    hist = dict{}

    for n, t in enumerate(list_edges):
        left = t[0]
        right = t[1]
        hist[n] =0

        for e in data:
            if left <= e < right:





    return 'histogram'


arr = [0, 3, 2, 6, 7, 1, 3, 50, 5]
num_bucket = 10
histogram(arr, num_bucket)
