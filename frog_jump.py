def solution(X, Y, D):
    # write your code in Python 3.6

    jumps = (Y-X) // D
    if (Y - X) % D > 0:
        return jumps + 1
    return jumps

if __name__ == '__main__':

    print(solution(10,85,30))
