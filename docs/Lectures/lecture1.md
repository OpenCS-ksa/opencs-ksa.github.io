---
layout: default
title: Theme 1. Basics
parent: Lectures
nav_order: 1
nav_exclude: false
---
### Theme 1
{: .no_toc }
# Basics
{: .no_toc }
- - -         
## Contents
{: .no_toc .text-delta }
1. TOC
{:toc}
- - -     
 
## Variables and Values 

모든 프로그램은 data를 기반으로 합니다. 이런 data들을 value라고 하죠. value들을 저장하는 메모리 위치를 variable이라고 합니다. 예시를 통해 알아봅시다.

```python
x=2
y=4
```
x,y 등은 variable 입니다.
x에는 2라는 value가, y에는 4라는 value가 할당되어 있죠
variable의 이름은 문자, 숫자, 그리고 _ 만 사용할 수 있습니다. python 자체에 사용되는 min, max등의 이름은 사용할 수 없습니다. 이는 나중에 여러분이 다른 이름들은 짓게 될때에도 해당합니다. 

{: .highlight }         
코드에서 x,y 등을 variable 혹은 변수라고 합니다. 이에 할당된 값을 value, 혹은 값이라고 합니다. 앞으로 기본이 될 예정이니 잘 익혀두시기 바랍니다.            

## Assigning Values to Variables           
변수에 값을 지정하는 것을 **"Assign (할당)"** 한다 라고 합니다. 변수의 조작을 통해 결론을 내는 것이 CS1 수업의 전부라고 볼 수도 있죠. 기본적인 assignment부터, variable을 조작하는 것 까지 알아봅시다. 
```python
x=2
print(x) # output: 2
```
x라는 variable에 2라는 value를 assign했습니다. 

```python
x=2
print(x) # output: 2
x=4
print(x) # output: 4 
x,y=4,1
print(x) # output: 4 
print(y) # output: 1
```
하나의 variable에 여러 value를 덮어 쓸 수 있습니다. 그대신 이전에 assign한 value는 소실되겠죠. 
한번에 여러개의 variable에 value를 지정할수도 있습니다. 

```python 
x=4
print(x) # output: 4 
y=1
x,y=y,x
print(x) # output: 1
print(y) # output: 4
x,y,z=0,1,2
print(x) # output: 0
print(y) # output: 1
print(z) # output: 2
```
두개의 variable을 서로 swap할 수 있습니다. 또한, 여러개의 value를 여러개의 variable에 한번에 지정할 수 있습니다. 새로 variable에 value를 지정할때마다 이전 내용이 덮일 수 있다는 점을 명심합시다. 

## Operators, Expressions

위에 지정한 variable을 Operator들을 사용해서 조작할 수 있습니다. 
순위가 가장 낮은 Operator, 즉 연산자부터 알아봅시다. 
> `+` : 합에 해당합니다.      
> `-` : 차에 해당합니다.   

그다음으로 낮은 순위에 해당하는 연산자들입니다. 
> `*` : 곱      
> `/` : 단순 나숫셈     
> `//` : 몫      
> `%` : 나머지   
에 해당합니다. 
위의 연산자들을 상황에 알맞게 사용하는 것이 중요합니다. 

두번째로 순위가 높은 연산자입니다. 
> `**` : 지수에 해당합니다.     

마지막으로 가장 순위가 높은 연산자입니다. 
> `()` : 흔히 위계도를 수동으로 정할때 사용합니다.             

위의 위계도 순서를 어느정도 외워두는 것도 좋겠지만, 여러분들이 시험을 볼때 Lecdture Slide를 볼 수 있고, 모르겠다 싶으면 ()을 사용해서 수동적으로 위계도를 정해주는것이 가장 편하고 확실한 방법입니다.           
(수학에서의 연산자 우선순위와 일치합니다.)          
(<a href = "https://www.scaler.com/topics/operator-precedence-in-python/">참고자료</a>)

이런 연산자들을 사용하여 여러분은 ㅍariable을 조작하고, 값을 도출해내게 될 예정입니다. 
아래 코드를 통해 예시를 봅시다.

```python
x=3
y=2
x=x+2
x+=2
p=(x+y**4)**(x*3+y**4)
a
```
4번째 줄과 5번째 줄이 하는 역할은 같습니다. 이와 비슷한 맥락에서 -=, *=, /= 등이 있습니다. 
6번째 줄과 그 이후는 중요한 차이를 보여줍니다. Variable들을 사용해 식을 나타내야 하는 경우들이 생길 것 입니다. 이 식이 복잡한 경우가 많은데, 6번처럼 한번에 모아서 써도 되기는 하지만, 그 이후 줄처럼 나눠서 쓰는것이 가독성에 훨씬 좋습니다. 코드를 나중에 다시 볼때, 특히 시험이라면 가독성이 중요합니다. 



이런 연산자들을 사용하여
## Data Types

위에서 언급된 data들은 모두 종류가 있습니다. Data가 어떤 형식으로 어떤 정보를 저장하는지에 따라 다른 data type들이 있습니다. 다양한 data type들은 매우 유용하고, 다양한 data type을 효과적으로 사용하는 것이 CS1시험에서 매우 중요하게 작용합니다. 흔한 것들부터 알아봅시다. 

> `int` : 정수를 나타냅니다.             
> `float` : 실수를 나타냅니다. 파이썬에서 float을 사용할시 무한소수의 경우 표현을 못하기에 정확성이 살짝 떨어집니다. 유의하시기 바랍니다.         
> `str` : 문자열을 나타냅니다.     
> `bool` : True 또는 False를 나타냅니다. 나중에 loop에서 유용하게 사용됩니다. 이건 나중에 더 자세히 다룰 예정입니다.       
> `list` : 집합을 나타냅니다. 나중에 더 자세히 다룰 예정입니다.     

파이썬은 data type이 유동적인 언어입니다. 처음 변수를 만들때 따로 data type을 명시해주지 않아도 알아서 정해주고, data type을 바꿔줄 수 있습니다. 

```python
x=3
x=str(x)
print(type(x)) #output: <class 'str'>
```
첫째줄에서 3은 자동적으로 int로 인식합니다. 두번째 줄을 통해 x의 data type을 str으로 바꿔줍니다. 이때 x는 '3' 의 형태로 표현되죠. 또한 type 기능을 사용해 data type을 확인할 수 있습니다. 


## Input

Input을 받는 방식이 교재에 나와있기는 하나, 시험에서 이가 나올 일은 없습니다. 백준 등 OJ에서 사용되기는 하니 궁금하신 분들은 잠깐 읽어보시면 될 것 같습니다. 

```python
k = input("Write a number")
```
위의 코드를 사용하면 k 에 input받은 data를 저장하게 됩니다. 이때 Write a number이라는 글이 터미널 창에 나타나게 되죠. 

{: .warning }
모든 input은 str, 즉 문자열로 받게 됩니다. 아래의 코드를 통해 자신이 원하는 data type으로 바꿔줘야 합니다. 
```python
x = input("Write a number")
x=int(x)
print(x)
```

