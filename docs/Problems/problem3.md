---
layout: default
title: Problem 3
parent: Problems
nav_order: 3
nav_exclude: false
---

# Problem 3
{: .no_toc }
Theme 3 Problems

- - -           
## Problems
{: .no_toc .text-delta }
1. TOC
{:toc}
- - -         

## Q1. Minimum (Easy)
Write a function <U>min</U>:          
> input parameter : two integers a and b          
> return value : the minimum value among a and b        

```python
def min(a, b):
    # ADD ADDITIONAL CODE HERE!
    return

print(min(1, 4))        # 1
print(min(987, 924))    # 924
print(min(-826, 331))   # -826
```     

## Q2. Discriminant (Easy)
Write a function <U>discriminant</U> that returns the number of real roots of the given quadratic equation          
> input parameter :  three integers a, b, c (ax² + bx + c = 0)  (a is not a zero)          
> return value : the number of real roots of quadratic equation         

```python
def discriminant(a, b, c):
    # ADD ADDITIONAL CODE HERE!
    return

print(discriminant(1, 4, 4))    # 1
print(discriminant(1, -6, 5))   # 2
print(discriminant(1, 0 ,0))    # 0
```     

## Q3. Leap Year (Easy)
Write a function <U>isLeapYear</U>          
> input parameter :  a integer year (1 <= year <= 4000)          
> return value : returns 1 if the year is leap year (윤년); returns 0 otherwise        

참고로 윤년은 연도가 4의 배수이면서 100의 배수가 아니거나 400의 배수인 해이다.          

```python
def isLeapYear(a):
    # ADD ADDITIONAL CODE HERE!
    return

print(isLeapYear(2023)) # 0
print(isLeapYear(2024)) # 1
print(isLeapYear(3000)) # 0
```     
[외부 출처] : https://www.acmicpc.net/problem/2753

## Q4. Advanced Minimum (Medium)
Write a function <U>min</U>:       
> input parameter :  three integers a, b, c          
> return value : the minimum value among a, b and c          

```python
def min(a, b, c):
    # ADD ADDITIONAL CODE HERE!
    return

print(min(1, 10, 100))      # 1
print(min(324, -21, 235))   # -21
print(min(5, 5 ,0))         # 0
```     

## Q5. IsTriangle (Medium)
Write a function <U>isTriangle</U>:       
> input parameter :  three positive integers a, b, c (length of each edges)          
> return value : returns 1 if it can be a triangle; returns 0 otherwise          

```python
def isTriangle(a, b, c):
    # ADD ADDITIONAL CODE HERE!
    return

print(isTriangle(3, 4, 5))    # 1
print(isTriangle(2, 10, 7))   # 0
print(isTriangle(8, 4 ,4))    # 0
```     

## Q6. Triangle (Hard)
Write a function <U>triangle</U>:       
> input parameter :  three positive integers a, b, c (length of each edges)          
> return value : type of the triange ("Acute Triangle" or "Obtuse Triangle" or "Right Triange")          

```python
def triangle(a, b, c):
    # ADD ADDITIONAL CODE HERE!
    return

print(triangle(3, 4, 5))    # Right Triangle
print(triangle(2, 3, 3))    # Acute Triangle
print(triangle(5, 5, 9))    # Obtuse Triangle
```     

## Q7. Circle Intersection (Hard)
Write a function <U>intersection</U>:       
> input parameter : two (x, y) coordinates and radii x1, y1, r1, x2, y2, r2         
> return value : returns 1 if they intersect (include the case meeting at one point); returns 0 otherwise       

```python
def intersection(x1, y1, r1, x2, y2, r2):
    # ADD ADDITIONAL CODE HERE!
    return

print(intersection(0, 0, 3, 2, 3, 2))    # 1
print(intersection(1, 3, 2, 4, 0, 1))    # 0
```     

## Q8. Formula Creator (Hard)
There are three integers a, b, and c.
We can append one of four arithmetic operators (+, -, *, /) and an equal sign.         
Write a function <U>formula</U> that returns the complete math formula by inserting appropriate operators between the numbers.            

+ Numbers cannot be swapped with each other.            
+ Return one of them if there exist more than one complete formulas            
+ You should not insert space or other unnecessary characters in the return value.          
+ There always exists complete formula(s).

> input parameter : three integers a, b, c         
> return value : complete math formula by inserting appropriate operators between the numbers.       

```python
def formula(a, b, c):
    # ADD ADDITIONAL CODE HERE!
    return

print(formula(5, 2, 3)) # 5=2+3 or 5-2=3
print(formula(9, 3, 6)) # 9=3*6 or 9/3=6 or 9-3=6 or 9=3+6
print(formula(2, 2, 4)) # 2+2=4 or 2*2=4
```     

{: .tip}
이 문제는 단순히 조건문을 나열해서도 풀 수 있지만,          
함수로 기능을 묶어두면 훨씬 간단하게 풀 수 있습니다.        
        
## Q9. Three Dices (Hard)
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다. 

같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  
예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 함수 <U>score</U>을 작성하시오.

```python
def score(dice1, dice2, dice3):
    # ADD ADDITIONAL CODE HERE!
    return

print(score(3, 3, 6))    # 1300
print(score(2, 2, 2))    # 12000
print(score(6, 2, 5))    # 600
```     
[외부 출처] 한국정보올림피아드 지역본선 2010 중등부 1번 : https://www.acmicpc.net/problem/2480