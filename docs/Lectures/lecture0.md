---
layout: default
title: Theme 0. Introduction
parent: Lectures
nav_order: 0
nav_exclude: false
---
### Theme 0
# Introduction.

- - -

## CS1
정보 과학 1은 그냥 프로그래밍을 하는 방법을 배우는 과목입니다.      
즉 정보 과학과 관련한 심화된 개념 (알고리즘 등)은 전혀 배우지 않습니다.         
오직 파이썬 문법을 공부하고, 이를 활용해 문제를 푸는게 다 입니다.

> 결과적으로        
> 1. 파이썬 문법을 제대로 아는 것       
> 2. 문제를 여러번 풀어보면서 감을 익히는것        
이 가장 중요합니다.     

## Python
<img src = "https://upload.wikimedia.org/wikipedia/commons/f/f8/Python_logo_and_wordmark.svg" width = "50%">
파이썬은 간결하면서도 다양한 기능을 제공하는 프로그래밍 언어입니다.         
그런 만큼 다양한 자료들이 인터넷에 떠돌고 있어서        
굉장히 활용성이 높은 언어입니다.        
또한, 기존의 언어들 (C, C++, JAVA 등)에 비해서      
훨씬 간단한 문법을 통해 입문하기에 그나마 쉬운 언어입니다.      
파이썬이라는 언어를 깊게 팔 필요는 없으니 이 정도만 알아둡시다.         

{: .note } 추가적인 정보가 궁금하다면 <a href = "https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%B4%EC%8D%AC">이 웹사이트</a>를 참고하세요.

## Python 설치
이건 정보 시간에 충분히 설치 방법을 도와주니 깊게 설명하지는 않겠습니다.            
1. <a href = "https://www.python.org/">Python 공식 웹사이트</a>에서 원하는 버전의 파이썬 설치 파일을 다운로드 받습니다. 
(학교에서는 Python 3.7.0 버전의 사용을 권장합니다.)
2. 설치 파일을 실행시켜 설치를 진행합니다.
{: .note} 설치 시 Add Python to PATH 항목을 **반드시** 선택하시길 바랍니다. 또한, Customize installation을 선택하여 모든 Optional Features를 다운로드 받습니다.
3. Pillow 5.2.0 이미지 라이브러리를 설치합니다.
4. Robot을 사용하기 위한 설정을 합니다. 하지만 3번과 4번 내용은 중요하지도 않고 정보 시간에 충분히 도와줄 것이니 걱정하지 않으셔도 됩니다.

## 코드 편집기
솔직히 말해서 파이썬 코드는 메모장에서도 작성할 수 있습니다.        
하지만 코드 편집기를 활용하면 훨씬 편하게 코드를 짤 수 있습니다.        
(메모장으로 코딩하는 사람을 보면 그 사람은 심하게 이상한 사람이 분명하니 멀리하는게 맞습니다.)      

아래 코드 편집기들을 보고 원하는걸 선택하시면 됩니다.           

### 1. Wing IDE
<img src = "https://wingware.com/images/screenshots/wing7-screenshot-classic-small.jpg" width = "80%">

> 학교에서 사용하길 권장하는 IDE입니다.            
> 나름 자동 완성도 지원하고, 디버깅 기능도 나쁘지 않습니다.          
> 하지만 자동 완성 기능을 쓸 때 마다 키를 눌러야 한다는 점,        
> 마지막으로 UI 및 코드 하이라이트가 많은 학생들의 의견에 따르면 별로라는 점이 단점입니다.        

{: .highlight }
> 학교에서 권장하는 만큼 안정성을 원한다면 Wing IDE를 쓰셔도 좋지만,      
> 코드를 작성하는데 있어서 그리 좋은 편집기는 아닙니다.       

[다운로드 사이트](https://wingware.com/downloads/wing-101){: .btn }

### 2. Visual Studio Code (VSC)
<img src = "https://code.visualstudio.com/assets/docs/languages/typescript/overview.png" width = "80%">

> Microsoft에서 제작한 코드 편집기로, 가벼우면서도 기능이 강력하다는 것이 특징입니다.      
> 이 웹사이트 역시 VSC를 활용해 제작되었으며, 많은 사람들이 파이썬 코드를 작성하는데에 애용하는 편집기 입니다.        
> 우수한 자동 완성 기능을 제공하고, 코드 하이라이트 및 UI가 꽤 직관적입니다.      
> 디버깅 기능 역시 나쁘지 않습니다.       

{: .highlight }
> 정보 전공이든 정보 전공이 아니든 가볍게 사용하기 좋으며,        
> Open CS 멘토링에서 가장 추천하는 편집기 입니다.     

[다운로드 사이트](https://code.visualstudio.com/download){: .btn }

### 3. Pycharm
<img src = "https://www.jetbrains.com/pycharm/img/screenshots/complexLook@2x.jpg" width = "80%">

> Jetbrain에서 제작한 파이썬 특화 IDE로 전문적인 파이썬 개발에 있어서 가장 강력한 편집기입니다.       
> 높은 수준의 지능화된 자동 완성 기능을 제공하며, 디버깅 기능 역시 매우 탁월합니다.       
> 앞으로 파이썬을 자주 활용하게 된다면 아마도 가장 사용하기 좋은 편집기 일 것입니다.      
> 다만, 많은 유용한 기능을 제공하는 만큼 프로그램 자체가 무겁다는 것이 단점입니다.        
> 켜지거나 중간중간 파일을 분석하는 과정에서 컴퓨터의 성능이 부족하다면 쾌적하게 이용하기 힘들 수 있습니다.       

{: .highlight }
> 입문자에게는 사용하기 좀 번거로울 수 있습니다.      
> 다만, 앞으로 정보를 전공할 예정이라면 한 번 쯤은 활용해볼 만한 IDE 입니다.      

[다운로드 사이트](https://www.jetbrains.com/ko-kr/pycharm/){: .btn }

{: .note } 
> 세부적인 사용 방법은 멘토링 및 멘토의 설명을 참고하거나,          
> 또는 <a href = "https://google.com">이 친구</a> 또는 <a href = "https://chat.openai.com/">이 친구</a>에게 물어봐주세요.

## 파이썬 파일 실행시키기
파이썬 파일은 `파일명.py`의 형태이며, 이를 파이썬 코드 편집기에서 작성하고, 실행할 수 있습니다.     

우선 아래 버튼을 눌러 파일을 다운로드 받아 봅시다.      
[test.py](https://www.jetbrains.com/ko-kr/pycharm/){: .btn }

설치한 파이썬 코드 편집기 (Wing IDE or VSC or Pycharm or ...)를 실행시키고          
위에서 다운로드 받은 파일을 열어봅시다.         
(대부분 File > Open 을 클릭하거나, 파일을 드레그해서 코드 편집기 화면 위로 올리거나, 혹은 단순히 파일을 더블 클릭 해서 열 수 있습니다.)         
그러면 아마 여러분들의 화면에는 아래와 같은 코드가 작성된 파일이 열릴 것 입니다.            
```python
# Open CS Mentoring
# Testing Development Environment

def func():
    print ("Test")
    a = 1
    b = 2
    print (a + b)
    return

func()
```

이제 이 코드를 실행시켜 봅시다.         
소스코드 편집기 위쪽을 보면 삼각형 모양의 실행 표시가 있을 것 입니다.           
{: .코드 실행 단축키}
> 아래 단축키를 이용하면 코드를 쉽게 실행할 수 있습니다.            
> - Wing IDE : F5
> - VSC : Ctrl + F5
> - Pycharm : Ctrl + Shift + F10

코드를 실행시키면 아래 콘솔창 (터미널, Python Shell 등으로 표기)에
```
Test
3
```
이렇게 출력되는 것을 확인할 수 있습니다.

우리는 이제 파이썬 코드를 실행할 수 있습니다.