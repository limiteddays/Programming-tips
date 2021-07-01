def solution(A, B, K):
    # write your code in Python 3.6

    if A % K == 0:
        return (B-A) // K+1
    else:
        return (B- (A - A % K)) //K

if __name__ == '__main__':

    print(solution(6,11,2))
