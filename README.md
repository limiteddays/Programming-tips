# Clean Codes

## Use the join

```python
my_name = " ".join(['firstname','lastname'])
```
이렇게하면, 깔끔하게 variable 들을 정리할 수 있다.

## List comprehension
읽을 수 있는 리스트에는, 모든 코드를 리스트에다가 적을 수 있다.
예를 들어서

```python
numbers = [1,2,3,4,5,6,7,8,9,10]

even_halves = [num/2 for num in numbers if num%2 = 0]
```

## Use the Zip
zip을 쓰면, 빠르게 여러 리스트들을 iterate 하는것이 가능하다.

```python

students = [‘tom’,’dick’,’harry’,’larry’,’tim’,’benny’]
scores = [100,20,40,60,30,40]

for student, score in zip(students, scores):
  print(student, scores)
```

# Don't forget
## Lambda Function

람다펑션은 대학에서 자세하게 가르쳐주지 않는 function 중 하나이다.
확실히 가르치기에는, 너무 생략되어 있는 부분이 많아서 그런 것이라고 추측한다.

예를 들어보자.

```python
def add(x: int, y: int):
  return x + y

add(10, 10)

#이라는 function 이 존재한다고 하면,

(lambda x,y: x + y)(10,10)

이라고 쓰는 것이 가능하다.

```

참고: https://wikidocs.net/64


# algorithms

## BFS

```python
def search(root,key):

    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root

    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)

    # Key is smaller than root's key
    return search(root.left,key)
```

## DFS




## how to choose from them
The best thing to consider will be where our end goal is located.
If our goal is located closer to the root, BFS will be better, since it checks it.
DFS is better when the goal is located near the leaf.


## negative sorting

```python
res = sorted(A, key = lambda i: 0 if i == 0 else -1 / i)
```

## maximum occurence

```python:
max(lst,key=lst.count)

```

this time complexity is worse than the Counter most common.
However, it is very easy to implement, integrated and rapid C implementation.
faster for short list, but not for the larger ones.


## Heap implementation

```python
# Python3 program to find the most
# frequent element in an array.
import math as mt

def mostFrequent(arr, n):

    # Insert all elements in Hash.
    Hash = dict()
    for i in range(n):
        if arr[i] in Hash.keys():
            Hash[arr[i]] += 1
        else:
            Hash[arr[i]] = 1

    # find the max frequency
    max_count = 0
    res = -1
    for i in Hash:
        if (max_count < Hash[i]):
            res = i
            max_count = Hash[i]

    return res

# Driver Code
arr = [ 1, 5, 2, 1, 3, 2, 1]
n = len(arr)
print(mostFrequent(arr, n))

# This code is contributed
# by Mohit kumar 29
```


## tree heap
```python

def traverse(sub_tree, height):
    left_height = 0
    right_height = 0

    if sub_tree.l:
        left_height = traverse(sub_tree.l, height + 1)
    if sub_tree.r:
        right_height = traverse(sub_tree.r, height + 1)

    print(sub_tree.l or sub_tree.r)
    if sub_tree.l or sub_tree.r:

        return max(left_height, right_height)
    else:
        return height

def solution(T):
    # write your code in Python 3.6
    return traverse(T, 0)

```
