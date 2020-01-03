# First write code to sort two merged arrays
def merge(left, right):
    i = j = 0
    l = len(left) + len(right)
    combined = [0] * l
    while (i + j) < l:
        if (j == len(right)) or (i < len(left) and left[i] < right[j]):
            combined[i + j] = left[i]
            i += 1
        else:
            combined[i + j] = right[j]
            j += 1
    return combined


def merge2(left, right):
    result = []
    while left and right:
        result.append((left if left[0] <= right[0] else right).pop(0))
    return result + left + right


def insertion_sort(collection):
    c = collection.copy()
    for loop_index in range(1, len(collection)):
        insertion_index = loop_index
        while (insertion_index > 0 and collection[insertion_index - 1] > collection[insertion_index]):
            collection[insertion_index], collection[insertion_index - 1] = (collection[insertion_index - 1],collection[insertion_index],)
            insertion_index -= 1

    return collection


def selection_sort(collection):
    length = len(collection)
    c = collection.copy()
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k
        if least != i:
            collection[least], collection[i] = (collection[i], collection[least])
    return collection


l = [6, 10, 15, 33,64,69]
r = [7,12]
c = [15,33,12,96,5,10,83,2]

x = selection_sort(c)
print(x)
x = merge2(l, r)
print(x)
