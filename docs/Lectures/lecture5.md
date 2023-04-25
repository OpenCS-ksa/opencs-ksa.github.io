---
layout: default
title: Theme 5. For-Loops
parent: Lectures
nav_order: 5
nav_exclude: false 
---
### Theme 5
{: .no_toc }
# For Loops
{: .no_toc }
- - -         
## Contents
{: .no_toc .text-delta }
1. TOC
{:toc}
- - -     

## For-Loops
지금까지 코드에서 반복적인 동작을 해주려면 하나하나 다 코드를 짜주는 방법만 있었습니다. 이는 부정확하고, 효율성이 떨어집니다. 이에 대한 해결책이 바로 for-loop입니다. 아래 예시를 통해 알아봅시다. 

```python
def sum(n):
    sum = 0
    sum = sum + 1
    sum = sum + 2
    sum = sum + 3
    sum = sum + 3  
    sum = sum + n
return sum
```

```python
def sum(n):
    sum = 0
    for i in range(1,n+1):  
        sum = sum + i
    return sum
```
위의 예시에선 i가 하나씩 증가하면서 코드가 진행되게됩니다. 
for-loop는 기본적으로 위처럼
```python
for i in range(i,j):
```
의 형태를 가집니다. 이에 대해선 아래에서 더 자세히 알아보겠습니다. 

## Range grammar
많은 실수가 일어나는 Range 입니다. 
```python
for i in range(1,10):
```
에서, is