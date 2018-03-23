/**
 * Created by Antonina on 09.12.2017.
 */

$('#save-button').click(function() {
    var data = {
        "Photo": $('#profile-img').attr('src'),
        "CompanyName": $('#company-name').val(),
        "City": $('#city').val(),
        "Country": $('#country').val(),
        "webSite": $('#link').val(),
        "AboutCompany": $('#bio').val(),
        "Email": $('#email').val(),
        "OldPassword": $('#password').val(),
        "NewPassword": $('#new-password').val(),
        "ConfirmPassword": $('#confirm-new-password').val()
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