/**
 * Created by Antonina on 21.11.2017.
 */

$(function() {
    $("#register-form").validate({
        rules: {
            company_name: "required",
            email: {
                required: true,
                email: true
            },
            login: {
                required: true,
                minlength: 3
            },
            password: {
                required: true,
                minlength: 8,
                maxlength: 15
            },
            confirm_password: {
                required: true,
                equalTo: '#password-sign-up'
            }
        },
        messages: {
            first_name: "please enter your first name",
            last_name: "please enter your last name",
            login: "please enter your login",
            email: "please enter a valid email address",
            password: {
                required: "please provide a password",
                minlength: "password at least have 8 characters"
            },
            confirm_password: {
                required: "please retype your password",
                equalTo: "password doesn't match!"
            }
        },
        focusCleanup: true,
        focusInvalid: false,
        invalidHandler: function(event, validator) {
            $(".js-form-message").text("Please correct all errors.");
            return false;
        },
        onkeyup: function(element) {
            $(".js-form-message").text("");
        },
        errorPlacement: function(error, element) {
            return true;
        },
        errorClass: "form-input_error",
        validClass: "form-input_success",
        submitHandler: createProfile()
    });
});

function createProfile() {
    $('#sign-up-button').click(function() {
        var company_name = $('#company-name-sign-up').val();
        var email = $('#email-sign-up').val();
        var login = $('#login-sign-up').val();
        var password = $('#password-sign-up').val();
        var confirm = $('#confirm-password-sign-up').val();
        var data = {
            "name": company_name,
            "email": email,
            "login": login,
            "password": password,
            "confirm": confirm
        };
        $.ajax({
            url: '/api/register/company', //the page containing python script
            dataType: 'json',
            contentType: 'application/json',
            type: 'POST',
            data: JSON.stringify(data),
            success: function(response) {
                if (response.redirect=='true'){
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
}
