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
