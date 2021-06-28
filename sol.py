# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    A.sort()
    res = sorted(A, key = lambda i: 0 if i == 0 else -1 / i)
    A = set(A)
    print(A)

    i = 1
    is_positive = False

    for x in A:

        if x > 0:
            is_positive = True

        if x > i:
            return i

        else:
            i += 1

    else:
        if is_positive:
            A = list(A)
            return A[len(A) -1 ] + 1

        else:
            return 1



if __name__ == '__main__':

    print(solution([1, 3, 6, 4, 1, 2]))
