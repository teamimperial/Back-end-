/**
 * Created by Antonina on 17.12.2017.
 */

$('#create-course').click(function() {
    var name = $('#name').val();
    var amount = $('#amount').val();
    var city = $('#city').val();
    var country = $('#country').val();
    var date_of_start = $('#date-of-start').val();
    var date_of_end = $('#date-of-end').val();
    var info = $('#info').val();
    var data = {
        "name": name,
        "amount": amount,
        "city": city,
        "country": country,
        "date_of_start": date_of_start,
        "date_of_end": date_of_end,
        "info": info
    };
    $.ajax({
        url: '/', //the page containing python script
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
        success: function() {
            console.log('info changed');
        },
        error: function() {
            console.log('error');
        }
    });
});