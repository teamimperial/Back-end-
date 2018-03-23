/**
 * Created by Antonina on 09.12.2017.
 */

$('#save-button').click(function() {
    var data = {
        "img": $('#profile-img').attr('src'),
        "first_name": $('#first-name').val(),
        "last_name": $('#last-name').val(),
        "city": $('#city').val(),
        "country": $('#country').val(),
        "date_of_birth": $('#date-of-birth').val(),
        "university": $('#university').val(),
        "time_of_studing": $('#time-of-studing').val(),
        "link": $('#link').val(),
        "bio": $('#bio').val(),
        "email": $('#email').val(),
        "password":  $('#new-password').val()
    };
    $.ajax({
        url: '/student/update', //the page containing python script
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
        success: function(response) {
            if(response.redirect=='true'){
            alert(response.message)
            window.location.href = response.redirect_url;
            }
            if(response.redirect=='false'){
            alert(response.message);
            }
        },
        error: function() {
            console.log('error');
        }
    });
});