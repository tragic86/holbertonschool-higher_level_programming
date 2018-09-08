$(function(){ 
    $.ajax({
        type: 'GET',
        url: 'https://swapi.co/api/people/5/?format=json',
        success: function(home) {
            $('DIV#character').text(home['name']);
        }
    });
});
