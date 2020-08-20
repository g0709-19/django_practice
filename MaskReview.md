# 마스크 알리미
멋쟁이사자처럼 마스크 알리미 강의 내용 정리
<a href="https://ofcourse.kr/">HTML, CSS, JS 정리</a>

<br>

## 실습 환경
* <a href="https://code.visualstudio.com/">VisualStudioCode</a> - IDE
* <a href="https://www.postman.com/downloads/">Postman</a> - API 테스트
* <a href="https://www.python.org/downloads/">Python3</a> - 언어

<br>

## HTTP
* Hyper Text: 참조를 통해 한 문서에서 관련된 다른 문서들로 넘나들며 원하는 정보를 얻을 수 있게 해주는 텍스트

* Transfer Protocol: 인터넷을 통해서 정보를 주고받을 때 지켜야하는 규칙

### 구성
Request(요청), Response(응답)

### Request Method
* GET: URL(Uniform Resource Locator)에 표시된 리소스를 가져오기
* POST: body에 정보를 담아 서버에 입력
* PUT: URL에 표시된 리소스와 바꿔 치기
* PATCH: PUT과 다르게 일부만 수정
* DELETE: URL에 표시된 특정 리소스를 삭제

<br>

## JSON
Java Script Object Notation
* Key : Value 형식
* 데이터 교환

- 기존 XML보다 가볍다
- 많은 프로그래밍 언어가 지원한다
- 전송 시: 직렬화 과정을 거친다(JSON -> String)
- 수신 시: 역직렬화 과정을 거친다(String -> JSON)

<a href="https://developer.mozilla.org/ko/docs/Learn/JavaScript/Objects/JSON">MDN JSON 문서</a>

<a href="https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json">같은 페이지의 Superhero data</a>

* 직렬화: JSON.stringify({json})
* 역직렬화: JSON.parse(serialized)

<br>

## API
* Application: 우리가 사용하는 다양한 서비스들
* Programming Interface: 서비스들이 제공해주는 데이터들에 접근하고 사용할 수 있도록 도와주는 도구(ex. 리모콘)

### 종류
* SOAP(Simple Object Access Protocol): XML을 쉽게 주고 받기 위한 프로토콜
* REST(Representational State Transfer): 아키텍처
* GraphQL(Graph Query Language): 페이스북에서 만든 API

<br>

## REST API
Representational State Transfer  
하나의 아키텍처

* 소프트웨어 아키텍처: 소프트웨어를 설계하는 지침과 원칙
* 꼭 다 지켜야 되는 것은 아니라서 완전히 Restful한 API는 많지 않다.

### 구성요소
* 자원(URL...)
* 행위(GET, PATCH, ...)
* 표현(데이터 표현 방식)

<br>

## JSONPlaceholder
<a href="https://jsonplaceholder.typicode.com/">사이트</a>
* Fake online REST API
* REST API를 테스트, 프로토타이핑

<br>

## URL
* 프로토콜: http, https, ftp 등
* 호스트주소: www.google.com
* 파일경로: /index.html
* Query parameter: ?id=1&postid=1(검색, 필터링, 데이터 교환 시 사용)

<br>

## Postman
### GET
### POST
id는 unique 해야 돼서 값을 줘도 적용이 안 됨
### PUT
### PATCH
### DELETE

<br>

## 비동기 처리
### Promise 객체
* 대기
* 이행
* 거부

### 패턴
async, await 키워드 활용
```
async function asyncFunction() {
    await [Promise객체]
}
```

```
[Promise 객체]
.then(콜백함수)
.then(콜백함수)
.catch(콜백함수)
```

사용 예
```
let promiseObj = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('안녕하세요');
    }, timer);
});

promiseObj.then((value) => console.log(value));
```

<br>

## Fetch API
네트워크 통신을 위해서 제공되는 API  
반환: Promise 객체  
Request, Response 객체 사용

사용 예(GET)
```
const url = '';
fetch(url)
    .then(response => response.json())
    .then(json => console.log(json));
```

사용 예(POST)
```
let newPost = {
    title: 'foo',
    body: 'bar',
    userid: 1
};

const url = '';
fetch(url, {
    method: 'POST',
    body: JSON.stringify(newPost),
    headers: {
        "Content-type": "application/json; charset=UTF-8"
    }
})
    .then(response => {
        console.log('response 타입: " + typeof(response));
        return response.json();
    });
```