$(document).ready(function () {
    // td의 각 행에 있는 star1을 누르면 star1이 display:none이 되면서 star2가 display:block으로 바뀌고 star2를 누르면 반대로 되게 하기
    $(".star-icon[name='star1']").click(function () {
        var parentRow = $(this).closest('tr');
        parentRow.find(".star-icon[name='star1']").toggle();
        parentRow.find(".star-icon[name='star2']").toggle();
        updateCheckAllStars(); // 전체 선택 상태 업데이트
    });

    $(".star-icon[name='star2']").click(function () {
        var parentRow = $(this).closest('tr');
        parentRow.find(".star-icon[name='star2']").toggle();
        parentRow.find(".star-icon[name='star1']").toggle();
        updateCheckAllStars(); // 전체 선택 상태 업데이트
    });

    // star2 전체가 클릭되면 star_chkAll2가 보이고 star1 전체가 클릭되면 star_chkAll1이 보이게 하기
    $("#star_chkAll1, #star_chkAll2").click(function (event) {
        event.preventDefault();
        $(".star-icon[name='star1']").toggle();
        $(".star-icon[name='star2']").toggle();
        updateCheckAllStars(); // 전체 선택 상태 업데이트
    });

    // 전체 선택 상태 업데이트 함수
    function updateCheckAllStars() {
        var anyStar1Visible = $(".star-icon[name='star1']:visible").length > 0;
        var anyStar2Visible = $(".star-icon[name='star2']:visible").length > 0;

        // 만약 td에 star1이 하나도 안 보이는 경우면 th에 star_chkAll1은 클릭 비활성화
        $("#star_chkAll1").css("display", anyStar1Visible ? "block" : "none");
        // 만약 td에 star2가 하나라도 보이는 경우면 th에 star_chkAll1은 클릭시 td에 별아이콘이 star2가 되게 설정
        if (anyStar2Visible) {
            $("#star_chkAll1").click(function (event) {
                event.preventDefault();
                $(".star-icon[name='star2']").show();
                $(".star-icon[name='star1']").hide();
                updateCheckAllStars(); // 전체 선택 상태 업데이트
            });
        }
        // 만약 td에 star1이 하나도 안 보이는 경우면 th에 star_chkAll2는 보이게 설정
        $("#star_chkAll2").css("display", anyStar1Visible ? "none" : "block");
    }
});