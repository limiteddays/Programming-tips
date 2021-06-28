def solution(N):
    # write your code in Python 3.6

    binary = list(str(bin(N)))
    binary.pop(0)
    binary.pop(0)

    print(binary)

    longest_index = None
    current_space = 0
    zero_exist = False
    i = 0
    while i < len(binary):
        if binary[i] == "0":
            zero_exist = True

        if binary[i] == "1":
            if longest_index == None:
                longest_index = current_space

            if longest_index < current_space:
                longest_index = current_space
                current_space = 0

        i += 1
        current_space += 1

    if not zero_exist:
        return 0

    if longest_index - 1 < 0:
        return 0

    return longest_index -1

if __name__ == '__main__':

    print(solution(15))
