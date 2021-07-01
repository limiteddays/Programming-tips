def solution(A):
    # write your code in Python 3.6


    A.sort()
    min = 1

    for x in A:

        if (x == min):
            min += 1

    return min


if __name__ == '__main__':

    A = [1, 3, 6, 4, 1, 2]
    print(solution(A))
