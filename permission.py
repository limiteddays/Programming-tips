def solution(A):
    # write your code in Python 3.6
    A.sort()

    if not A:
        return None

    i = 1
    while i <= len(A):
        print(i)
        if i != A[i-1]:
            return i

        i += 1

    else:
        return None

if __name__ == '__main__':
    print(solution([]))
