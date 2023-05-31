// script that updates the text color of the HTML tag header to red
// when the user clicks on the tag DIV#red_header
// using jQuery API

$('DIV#red_header').click(function () {
  $('HEADER').css({ color: '#FF0000' });
});
