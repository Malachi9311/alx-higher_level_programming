// script that fetches the name from Star Wars API URL
// URL: https://swapi-api.hbtn.io/api/people/5/?format=json
// using jQuery API

$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  success: function (data) {
    $('DIV#character').text(data.name);
  }
});
