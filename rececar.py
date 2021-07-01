def solution(S):
    # write your code in Python 3.6

    if not S:
        return -1

    if len(S) == 1:
        return 0

    i = 0
    while i < len(S)/2:
        if S[i] == S[-(i + 1)]:
            i += 1

        else:
            return -1


    return i -1

if __name__ == '__main__':

    print(solution("theworld2dlroweht"))
