// script that fetches the value of hello from French API URL
// URL: https://fourtonfish.com/hellosalut/?lang=fr
// using jQuery API

$(document).ready(function () {
  $.ajax({
    method: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
});
