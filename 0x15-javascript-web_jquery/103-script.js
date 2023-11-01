$(function() {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('#btn_translate').click(function() {
    const langCode = $('#language_code').val();
    $.get(`${url}lang=${langCode}`, function(data) {
      $('#hello').html(data.hello);
    });
  });
});
