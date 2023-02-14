---
layout: default
title: 제목
nav_order: 2
---

# 제목
{: .no_toc }

개요개요개요개요
{: .fs-6 .fw-300 }

## 파이썬

파이썬이란 무엇무엇이다...

## 어쩌구 저쩌구

```yaml
이런 네모에 내용 넣을수도 있음
-> 아마도 여기에 예시 코드가 들어가겠지
```

대충 그거에 대한 설명

## 어쩌구 저쩌구 2

ㅁㄴㅇ리ㅏㅓㅁ니아;ㅓ리;ㅏ먼ㅇㄹ`이런식의 레이아웃도 가능`

## 어쩌구 저쩌구 3

asdfaslkdjflkjaslkdjflk;jalksdjf[구글 바로가기 하이퍼링크](http://www.google.com)

### 이것은
내용~~~~~~~~

### 세부
내용~~~~~~~~

### 사항
내용~~~~~~~~

## 다크모드 버튼
<button class="btn js-toggle-dark-mode">Preview dark color scheme</button>

<script>
const toggleDarkMode = document.querySelector('.js-toggle-dark-mode');

jtd.addEvent(toggleDarkMode, 'click', function(){
  if (jtd.getTheme() === 'dark') {
    jtd.setTheme('light');
    toggleDarkMode.textContent = 'Preview dark color scheme';
  } else {
    jtd.setTheme('dark');
    toggleDarkMode.textContent = 'Return to the light side';
  }
});
</script>

## 오류 코드

{: .warning }
> 와 이건 좀 개쩌는데? 여기다가 오류 예시 첨부 가능함