// $(document).ready(function () {
//   $('.drawer').drawer();
// });


// <
// a href = "javascript:history.go(-1)" > [戻る] < /a>


$(function () {
  $('.menu-btn').on('click', function () {
    $('.menu').toggleClass('is-active');
  });
}());