def solution(A, K):
    # write your code in Python 3.6


    new = []
    new_re = []
    first = True

    i = 0
    while i < K:

        if first == True:

            new.append(A.pop(-1))
            while A:
                new.append(A.pop(0))

            first = False

        elif first == False:

            A.append(new.pop(-1))
            while new:
                A.append(new.pop(0))

            first = True

        i += 1

    if not first:
        return new
    else:
        return A


if __name__ == '__main__':

    A = [0,1,1]
    K = 1
    print(solution(A,K))
