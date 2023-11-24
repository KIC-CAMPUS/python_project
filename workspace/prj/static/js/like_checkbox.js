$(".like").click(function(){
    var pk = $(this).attr('name')
    $.ajax({ // .like 버튼을 클릭하면 <새로고침> 없이 ajax로 서버와 통신하겠다.
        type: "POST", // 데이터를 전송하는 방법을 지정
        url: "{% url 'post:post_like' %}", // 통신할 url을 지정
        data: {'pk': pk, 'csrfmiddlewaretoken': '{{ csrf_token }}'}, // 서버로 데이터 전송시 옵션
        dataType: "json", // 서버측에서 전송한 데이터를 어떤 형식의 데이터로서 해석할 것인가를 지정, 없으면 알아서 판단
      // 서버측에서 전송한 Response 데이터 형식 (json),
        error: function(request, status, error){ // 통신 실패시 - 로그인 페이지 리다이렉트
            alert("로그인이 필요합니다.")
            window.location.replace("login/")
        },
    });
})