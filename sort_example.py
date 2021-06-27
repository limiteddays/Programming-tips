strs = ["flower","flow","flight"]
dir = ["bruh", "bruh", "bruh"]

strs.sort()

print(strs)

# for x,y in zip(strs[0], strs[-1]):
#     print(x)
#     print(y)


for x in zip(strs[0]):
    print(x)
