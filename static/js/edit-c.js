/**
 * Created by Antonina on 09.12.2017.
 */

$('#save-button').click(function() {
    var img = $('#profile-img').src;
    var company_name = $('#company-name').val();
    var geolocation = $('#geolocation').val();
    var link = $('#link').val();
    var bio = $('#bio').val();
    var email = $('#email-sign-up').val();
    var password = $('#new-password').val();
    var data = {
        "img": img,
        "company_name": company_name,
        "geolocation": geolocation,
        "link": link,
        "bio": bio,
        "email": email,
        "password": password
    };
    $.ajax({
        url: '/update/company', //the page containing python script
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
        success: function() {
            if (response.redirect !== undefined && response.redirect){
                window.location.href = response.redirect_url;
            }
            console.log('info changed');
        },
        error: function() {
            console.log('error');
        }
    });
});