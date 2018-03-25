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
    var status = $('#status').val();
    var info = $('#info').val();
    var data = {
        "name": name,
        "amount": amount,
        "city": city,
        "country": country,
        "date_of_start": date_of_start,
        "date_of_end": date_of_end,
        "status": status,
        "info": info
    };
    $.ajax({
        url: '/create_course', //the page containing python script
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
        success: function(response) {
            if (response.redirect == 'true'){
                window.location.href = response.redirect_url;
            }
        },
        error: function() {
            console.log('error');
        }
    });
});

