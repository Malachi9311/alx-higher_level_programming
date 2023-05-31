// script that fetches the value of hello from language API URL
// URL: https://fourtonfish.com/hellosalut/?lang=
// where the language is the value of the tag INPUT#language_code
// using jQuery API

$(document).ready(function () {
  function translate () {
    $('DIV#hello').empty();
    const len = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=' + len,
      success: function (data) {
        $('DIV#hello').append(data.hello);
      }
    });
  }
  $('INPUT#btn_translate').click(function () {
    translate();
  });
  $('INPUT#language_code').keypress(function (e) {
    const key = e.which;
    if (key === 13) {
      translate();
    }
  });
});
