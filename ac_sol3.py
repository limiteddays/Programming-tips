def solution(X, Y, A):
    N = len(A)
    result = -1
    nX = 0
    nY = 0
    gmax = 0
    lmax = 0
    for i in range(N):
        lmax += 1
        if A[i] == X:
            nX += 1
        elif A[i] == Y:
            nY += 1
        if nX == nY:
            gmax = max(lmax, gmax)
    return gmax-1

if __name__ == '__main__':
    
