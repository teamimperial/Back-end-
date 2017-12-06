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
            company_name: "please enter your company name",
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
        var name = $('#company-name-sign-up').val();
        var email = $('#email-sign-up').val();
        var login = $('#login-sign-up').val();
        var password = $('#password-sign-up').val();
        var data = {
            'name': name,
            'email': email,
            'login': login,
            'password': password
        };
        $.ajax({
            url: '/api/register/company', //the page containing python script
            type: 'POST',
            dataType: "json",
            data: JSON.stringify(data),
            success: function() {
                console.log('user created');
                window.location = 'profile-c.html';
            },
            error: function() {
                console.log('error');
            }
        });
    });
}