# Frontend

## Mockup


## 리액트 컴포넌트 디자인

["Thinking in React"](https://reactjs.org/docs/thinking-in-react.html)의 가이드를 따라 다음과 같은 단계로 개발을 진행합니다.

1. 목업 데이터 준비
2. 화면을 나눠서 컴포넌트 만들기
3. 정적(static) 버전 만들기(state 사용 금지)
4. state와 props 구별


### 컴포넌트 구조

* App
    * Template
        * Heading
        * SearchBar
        * WordList
            * WordItem


### 컴포넌트 설계

#### 1. Template

* 클래스 컴포넌트
* state
  * lang
  * word
  * langCase
  * 위에서 서치한 결과 얻은 variables
* functions
  * SearchBar onChange = handleInputChange
  * SearchBar onSubmit = handleSubmit
  * SearchBar onKeyPress = handleSubmit


#### 2. Heading



#### 3. SearchBar

* 클래스 컴포넌트


#### 4. WordList

* 무상태 함수형 컴포넌트


#### 5. WordItem

* 클래스 컴포넌트
  * 각각 copy 횟수 저장


#### 참고

* https://reactjs.org/docs/thinking-in-react.html
* https://d2.naver.com/helloworld/4966453
