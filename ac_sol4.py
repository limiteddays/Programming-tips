def solution(A):
    right = ans = 0
    for i, a in enumerate(A, 1):
        right = max(right, a)
        ans += right == i
    return ans

if __name__ == '__main__':

    A = [2,1,3,5,4]
    print(solution(A))
