/**
 * Created by Antonina on 09.12.2017.
 */

$('#save-button').click(function() {
    var img = $('#profile-img').src;
    var first_name = $('#first-name').val();
    var last_name = $('#last-name').val();
    var city = $('#city').val();
    var country = $('#country').val();
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
        "city": city,
        "country": country,
        "date_of_birth": date_of_birth,
        "university": university,
        "time_of_studing": time_of_studing,
        "link": link,
        "bio": bio,
        "email": email,
        "password": password
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