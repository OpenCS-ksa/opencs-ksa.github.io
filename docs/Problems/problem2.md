---
layout: default
title: Problem 2
parent: Problems
nav_order: 2
nav_exclude: false
---

# Problem 2
{: .no_toc }
Theme 2 Problems

- - -           
## Problems
{: .no_toc .text-delta }
1. TOC
{:toc}
- - -         

## Q1. Average (Easy)
Write a function <U>average</U> that returns the arithmetic mean (산술 평균) of two integers a and b          
> input parameter : two integers a and b          
> return value : the arithmetic mean of a and b        

```python
def average(a, b):
    # ADD ADDITIONAL CODE HERE!
    return

print(average(8, 2))        # 5.0
print(average(247, -893))   # -323.0
print(average(4628, 1241))  # 2934.5
```     

## Q2. Slope (Easy)
Write a function <U>slope</U> that returns the slope of the equation of a straight line (ax + by + c = 0)          
> input parameter : three integers a, b, c (a is not a zero)          
> return value : the float slope value        

```python
def slope(a, b, c):
    # ADD ADDITIONAL CODE HERE!
    return

print(slope(1, 1, 1))   # -1.0
print(slope(2, -3, -7)) # 1.5
print(slope(3, 0, 6))   # 0.0
```     

## Q3. Root of Quadratic Equation (Easy)
Write a function <U>solve</U> that returns any real root of given quadratic equation          
(All of the quadratic equations given by inputs have at least one root)          
> input parameter : three integers a, b, c (ax² + bx + c = 0)  (a is not a zero)          
> return value : any real root of quadratic equation         

```python
def solve(a, b, c):
    # ADD ADDITIONAL CODE HERE!
    return

print(solve(1,-4,4))    # 2.0
print(solve(1,-7,12))   # 3.0 or 4.0
```     

## Q4. Time to Second (Easy)
Write a function <U>time2second</U>:
> input parameter : three integers hour, minute and second          
> return value : total second of the given time         

```python
def time2second(hour, minute , second):
    # ADD ADDITIONAL CODE HERE!
    return

print(time2second(1, 6, 32))    # 3992
print(time2second(5, 42, 3))    # 20523
print(time2second(15, 23, 39))  # 55419
```     

## Q5. Sum of Digits (Medium)
Write a function <U>sum</U>:
> input parameter : an integer n where 1000 <= n <= 9999 (i.e. 4-digit integer)          
> return value : sum of digits         

```python
def sum(n):
    # ADD ADDITIONAL CODE HERE!
    return

print(sum(8271))    # 18
print(sum(1032))    # 6
print(sum(4100))    # 5
```     

## Q6. Second to Time (Medium)
Write a function <U>second2time</U>:
> input parameter : an positive integer second          
> return value : string of that time (Hour : Minute : Second)         

```python
def second2time(second):
    # ADD ADDITIONAL CODE HERE!
    return

print(second2time(3992))     # 1:6:32
print(second2time(20523))   # 5:42:3
print(second2time(55419))   # 15:23:39
```     

## Q7. Sum of Odd (Hard)
Write a function <U>oddSum</U>:
> input parameter : five positive integers x1, x2, x3, x4, x5          
> return value : sum of the odd numbers         

+ Do not use condition statements or other advanced concepts           
조건문 및 다른 상위 개념 없이 푸시오         

```python
def oddSum(x1, x2, x3, x4, x5):
    # ADD ADDITIONAL CODE HERE!
    return

print(oddSum(1,2,3,4,5))    # 9
print(oddSum(2,4,6,8,10))   # 0
print(oddSum(1,3,5,7,9))    # 25
```     

## Q8. Round (Hard)
Write a function <U>round</U>:
> input parameter : an positive float n and an positive integer k         
> return value : number n rounded to the kth decimal place     
(k번째 자리에서 반올림 된 숫자 n)           

+ Do not use condition statements or other advanced concepts           
조건문 및 다른 상위 개념 없이 푸시오              

```python
def round(n, k):
    # ADD ADDITIONAL CODE HERE!
    return

print(round(0.324, 3))  # 0.32
print(round(0.387, 2))  # 0.4
print(round(0.512, 1))  # 1.0
```     
