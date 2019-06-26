def roate(array, n):
    length = len(array)
    myreverse(array, 0, n-1)
    myreverse(array, n, length-1)
    myreverse(array, 0, length-1)

def myreverse(array, start, end):
    for i in range(0, (end-start)//2 + 1):
        swap(array, start+i, end-i)

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def juggle_rotate(array, i):
    length = len(array)


def gcd(a, b):
    pass




if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6]
    # myreverse(array, 0, len(array)-1)
    roate(array, 5)
    print(array)
    # myreverse(array, 0, len(array)-1)
    # print(array)