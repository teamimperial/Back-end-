$('#save-button').click(function() {
    var img = $('#profile-img').src;
    var company_name = $('#company-name').val();
    var company_city = $('#company-city').val();
    var company_country = $('#company-country').val();
    var link = $('#link').val();
    var bio = $('#bio').val();
    var email = $('#email-sign-up').val();
    var password = $('#new-password').val();
    var data = {
        "Photo": img,
        "CompanyName": company_name,
        "City": company_city,
        "Country": company_country,
        "webSite": link,
        "AboutCompany": bio,
        "Email": email,
    };
    $.ajax({
        url: '/update/company', //the page containing python script
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
        success: function(response) {
            if (response.redirect !== undefined && response.redirect){
                    window.location.href = response.redirect_url;
                }
        },
        error: function() {
            console.log('error');
        }
    });
});