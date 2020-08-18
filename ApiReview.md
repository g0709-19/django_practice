# Javascript API

## 세계 날씨 API
1. OpenWeatherMap 가입(<a href="https://home.openweathermap.org/">사이트</a>)
2. My profile -> API keys 복사
3. API Document 참고하며 이용(<a href="https://openweathermap.org/current">사이트</a>)

### 날씨 정보 가져오는 URL
> api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={your api key}

<br>

## 지도 API
1. KaKaoMapAPI 가이드 따라 가입 후 appkey 획득(<a href="https://apis.map.kakao.com/web/guide/">사이트</a>)
2. 샘플 참고하며 이용(<a href="https://apis.map.kakao.com/web/sample/">사이트</a>)

### 로컬 서버 열기
```
python -V

# 위에서 반환된 파이썬 버전이 3.X인 경우
python -m http.server
# 위에서 반환된 파이썬 버전이 2.X인 경우
python -m SimpleHTTPServer
```

### Ajax 리턴 예제
```
function test() {
    var result = "";
    $.ajax({
        type: "post",
        url: "CheckID",
        async: false,     //값을 리턴시 해당코드를 추가하여 동기로 변경
        data: { ID: ID },
        success: function (data) {
            result = data;
        }
    });
    return result;
}
```

<br>

## JQuery
1. JQuery 파일 다운(<a href="https://jquery.com/">사이트</a>)
2. 로컬 저장소에 위치
3. script 태그 통해 읽음

<br>

## CSS
CSS 뷰포트 상대적 길이: vw(viewport width), vh(viewport height)