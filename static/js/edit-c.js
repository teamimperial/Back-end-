/**
 * Created by Antonina on 09.12.2017.
 */

$('#save-button').click(function() {
    var img = $('#profile-img').src;
    var company_name = $('#company-name').val();
    var city = $('#city').val();
    var country = $('#country').val();
    var link = $('#link').val();
    var bio = $('#bio').val();
    var email = $('#email-sign-up').val();
    var password = $('#new-password').val();
    var data = {
        "Photo": img,
        "CompanyName": company_name,
        "City": city,
        "Country": country,
        "webSite": link,
        "AboutCompany": bio,
        "Email": email,
        "password": password
    };
    $.ajax({
        url: '/company/update', //the page containing python script
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
        success: function(response) {
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