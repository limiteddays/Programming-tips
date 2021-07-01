import sys

def balanced(small, caps):

    for i in range(26):
        if (small[i] != 0 and (caps[i] == 0)):
            return 0

        elif((small[i] == 0) and (caps[i] != 0)):
            return 0
    return 1

def solution(s):

    small = [0 for i in range(26)]
    caps = [0 for i in range(26)]

    for i in range(len(s)):
        if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
            caps[ord(s[i]) - 65] += 1
        else:
            small[ord(s[i]) - 97] += 1

    mp = {}
    for i in range(26):
        if (small[i] and caps[i]==0):
            mp[chr(i + 97)] = 1

        elif (caps[i] and small[i]==0):
            mp[chr(i + 65)] = 1

    for i in range(len(small)):
        small[i] = 0
        caps[i] = 0

    i = 0
    st = 0

    start = -1
    end = -1

    minm = sys.maxsize

    while (i < len(s)):
        if(s[i] in mp):

            while (st < i):
                if (ord(s[st]) >= 65 and ord(s[st]) <= 90):
                    caps[ord(s[st]) - 65] -= 1
                else:
                    small[ord(s[st]) - 97] -= 1

                st += 1
            i += 1
            st = i
        else:
            if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
                caps[ord(s[i]) - 65] += 1
            else:
                small[ord(s[i] )- 97] += 1

            while (1):
                if (ord(s[st]) >= 65 and ord(s[st])<= 90 and caps[ord(s[st])- 65] > 1):
                    caps[ord(s[st]) - 65] -= 1
                    st += 1
                elif (ord(s[st]) >= 97 and ord(s[st]) <= 122 and small[ord(s[st]) - 97] > 1):
                    small[ord(s[st]) - 97] -= 1
                    st += 1
                else:
                    break

            if (balanced(small, caps)):
                if (minm > (i - st + 1)):
                    minm = i - st + 1
                    start = st
                    end = i
            i += 1

    if (start == -1 or end == -1):
        return -1

    else:
        ans = ""
        for i in range(start,end+1,1):
            ans +=  s[i]
        return ans

# Driver Code
if __name__ == '__main__':

    # Given string
    s = "AcZCbaBz"
    print(smallestBalancedSubstring(s))
