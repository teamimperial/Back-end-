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
    var confirm_password =$('#confirm-new-password').val();
    var new_password = $('#new-password').val();
    var password = $('#password').val();
    var data = {
        "Photo": img,
        "CompanyName": company_name,
        "City": city,
        "Country": country,
        "webSite": link,
        "AboutCompany": bio,
        "Email": email,
        "OldPassword": password,
        "NewPassword": new_password,
        "ConfirmPassword": confirm_password
    };
    $.ajax({
        url: '/company/update', //the page containing python script
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
        success: function(response) {
            if (response.redirect=='true'){
                var msg = response.message;
                alert(msg);
                window.location.href = response.redirect_url;
            }
            if (response.redirect=='false'){
                var msg = response.message;
                alert(msg);
            }
        },
        error: function() {
            console.log('error');
        }
    });
});