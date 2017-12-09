/**
 * Created by Antonina on 09.12.2017.
 */

$('#save-button').click(function() {
    var img = $('#profile-img').src;
    var first_name = $('#first-name').val();
    var last_name = $('#last-name').val();
    var geolocation = $('#geolocation').val();
    var date_of_birth = $('#date-of-birth').val();
    var university = $('#university').val();
    var time_of_studing = $('#time-of-studing').val();
    var link = $('#link').val();
    var bio = $('#bio').val();
    var email = $('#email-sign-up').val();
    var password = $('#new-password').val();
    var data = {
        "img": img,
        "first_name": first_name,
        "last_name": last_name,
        "geolocation": geolocation,
        "date_of_birth": date_of_birth,
        "university": university,
        "time_of_studing": time_of_studing,
        "link": link,
        "bio": bio,
        "email": email,
        "password": password
    };
    $.ajax({
        url: '/', //the page containing python script
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