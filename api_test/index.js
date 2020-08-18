var celsius = kelvin => {
    return kelvin-273.15;
}

let lat = '33.450701',
    lon = '126.570667',
    appid = '2c86b5e6c3f717a8696ad85e1a858e3d';

$.ajax({
    url: `//api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${appid}`,
    type: "GET",
    success: function(result) {
        if (result) {
            var iwContent = `<div style="padding:5px;">${celsius(result.main.temp)}도</div>`; // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
            // 인포윈도우를 생성합니다
            var infowindow = new kakao.maps.InfoWindow({
                position: iwPosition,
                content: iwContent
            });

            // 마커 위에 인포윈도우를 표시합니다. 두번째 파라미터인 marker를 넣어주지 않으면 지도 위에 표시됩니다
            infowindow.open(map, marker);
        } else {
            alert("불러오기 실패");
        }
    }
});

var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = { 
        center: new kakao.maps.LatLng(lat, lon), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

// 마커가 표시될 위치입니다 
var markerPosition  = new kakao.maps.LatLng(lat, lon); 

// 마커를 생성합니다
var marker = new kakao.maps.Marker({
    position: markerPosition,
});

// 마커가 지도 위에 표시되도록 설정합니다
marker.setMap(map);

var iwPosition = new kakao.maps.LatLng(lat, lon); //인포윈도우 표시 위치입니다