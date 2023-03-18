---
layout: default
title: Theme 4. Booleans
parent: Lectures
nav_order: 4
nav_exclude: false 
---
### Theme 4
{: .no_toc }
# Booleans
{: .no_toc }
- - -         
## Contents
{: .no_toc .text-delta }
1. TOC
{:toc}
- - -     

## Booleans
저번 단원에서 명제의 참또는 거짓으로 코드의 흐름을 바꾸는 방법에 대해 알아보았습니다. 어떤 명제를 코드에 활용할때, 그 명제의 참 여부를 변수로 사용할 수 있는 data type이 있습니다. 바로 Boolean 변수 입니다.        

Boolean 변수는 결국 조건문입니다. 즉, 다음과 같이 조건문이 사용되는 곳에는 모두 사용 될 수 있습니다. 

```python
if True:
    print(".")
```
또한, 변수 타입인 만큼 변수에 값을 저장할 수도 있습니다. 

```python
s = True
if s:
    print(".")
```
함수의 리턴에 사용할 수도 있죠. 

```python
def is_zero(a):
    return a==0
print(is_zero(0)) # Output: True
```

Boolean 변수는 둘 중 하나의 값을 가집니다. True와 False입니다. Boolean 변수를 단순 True, False가 아닌 방법으로 표현하는 방법은 나중에 더 자세히 알아보도록 하겠습니다. 

```python
if x==1:
    return True
else:
    return False
```
위 코드는 Boolean 변수의 예시 중 하나입니다. 

{: .warning}
> Boolean 변수의 표현 과정에서, 다음과 같은 실수를 많이들 합니다. 컴퓨터는 융통성이 없으므로, 꼭 True, False 형식을 맞춰주셔야 합니다.
> - "True", "False"
> - true, false

## Boolean 변수의 형태
Boolean 변수는 기본적으로 True, False의 값을 가지지만, 가지는 형태는 이보다 다양합니다. 대표적의 예로는
> Boolean expression                
> 0,1           
> True, False           
등이 있습니다. 

먼저, 비교 연산자들을 사용하여 Boolean Expression 이라는 것을 만들 수 있습니다. 아래와 같이 비교문을 리턴하면 그것이 참인지를 Boolean으로 리턴해줍니다. 

```python
def is_zero(a):
    return a==0
print(is_zero(0)) # Output: True
```

{: .warning}
Boolean 변수의 표현 과정에서 ==을 Float에 사용하는 것은 불안정합니다. Int에서의 ==사용은 안정합니다.  

또한, 0,1 을 조건문에 넣으면, 파이썬이 Boolean으로 인식하여 코드를 진행합니다. 0은 False, 1은 True에 대응됩니다. 많이 사용되지는 않지만, 출제될 여부는 언제나 있으니 알아두기만 하면 될 것 같습니다.

```python
if 1:
    print ("hello")
```

## Boolean expression의 연산자
위에서 말한 Boolean exoression을 논리 연산자를 사용하여 원하는 형태로 가공할 수 있습니다. 

> not: True를 False로, False를 True로 바꿔줍니다.           
> and: 둘다 만족하면 True, 아니면 False를 리턴해줍니다.         
> or: 하나만이라도 만족하면 True를, 아니면 False를 리턴해줍니다.            
```python
a=0
b=1
c=2
print(a==0 and b==1)
print(a==0 or b==0)
print(not a==0)
print(a==0 and (b==1 or c==3))
```
코드를 Boolean expression의 가공으로 코드를 많이 간단하게 만들 수 있습니다. 또한, 복잡한 Boolean expression이 나오면 헷갈리거나 실수 할 수 있으니 순서대로 차근차근 문제를 해결하시면 될 것 같습니다.

