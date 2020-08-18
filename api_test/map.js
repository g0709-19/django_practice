// 기본값 선언
const appid = '2c86b5e6c3f717a8696ad85e1a858e3d';
let lat = '33.450701',
    lon = '126.570667';

// 장소 검색 객체를 생성합니다
var ps = new kakao.maps.services.Places();

// 절대온도 -> 섭씨온도
var celsius = kelvin => {
    return kelvin - 273.15;
}

var getParameters = function (paramName) {
    // 리턴값을 위한 변수 선언
    var returnValue;

    // 현재 URL 가져오기
    var url = location.href;

    // get 파라미터 값을 가져올 수 있는 ? 를 기점으로 slice 한 후 split 으로 나눔
    var parameters = (url.slice(url.indexOf('?') + 1, url.length)).split('&');

    // 나누어진 값의 비교를 통해 paramName 으로 요청된 데이터의 값만 return
    for (var i = 0; i < parameters.length; i++) {
        var varName = parameters[i].split('=')[0];
        if (varName.toUpperCase() == paramName.toUpperCase()) {
            returnValue = parameters[i].split('=')[1];
            return decodeURIComponent(returnValue);
        }
    }
};

// 좌표로부터 날씨 정보 가져옴
function getWeatherFromCoord(lat, lon) {
    var result = "";
    $.ajax({
    url: `//api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${appid}`,
    type: "GET",
    async: false, // 동기로 바꿔주면서 리턴값 얻음
    success: function (data) {
        if (data) {
            result = data;
        } else {
            alert("불러오기 실패");
        }
    }
    });
    return result;
};

// 키워드 검색 완료 시 호출되는 콜백함수 입니다
function placesSearchCB(data, status) {
    if (status === kakao.maps.services.Status.OK) {
        // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
        // LatLngBounds 객체에 좌표를 추가합니다
        var bounds = new kakao.maps.LatLngBounds();
        for (var i = 0; i < data.length; i++) {
            displayMarker(data[i]);
            bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
        }

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
        map.setBounds(bounds);
    }
}

// 지도에 마커를 표시하는 함수입니다
function displayMarker(place) {

    let visible = true;
    var infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });

    // 마커를 생성하고 지도에 표시합니다
    var marker = new kakao.maps.Marker({
        map: map,
        position: new kakao.maps.LatLng(place.y, place.x)
    });

    // 마커에 클릭이벤트를 등록합니다
    kakao.maps.event.addListener(marker, 'click', function () {
        visible = !visible;

        // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
        if (visible) {
            infowindow.close();
        } else {
            var weather_info = getWeatherFromCoord(place.y, place.x);
            infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + `: ${Math.floor(celsius(weather_info.main.temp))}ºC` + '</div>');
            infowindow.open(map, marker);
        }
    });

}

// 키워드 검색 함수
var searchPlace = function (keyword) {
    // 키워드로 장소를 검색합니다
    ps.keywordSearch(keyword, placesSearchCB);
}

// 지도 생성 함수
var createMap = function (id, lat, lon, _level) {
    var mapContainer = document.getElementById(id), // 지도를 표시할 div 
        mapOption = {
            center: new kakao.maps.LatLng(lat, lon), // 지도의 중심좌표
            level: _level // 지도의 확대 레벨
        };

    var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다
    return map;
}

// 지도 생성
map = createMap('map', lat, lon, 3);
keyword = getParameters('place');
searchPlace(keyword);