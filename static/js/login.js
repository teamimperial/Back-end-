/**
 * Created by Antonina on 21.11.2017.
 */

$(function() {
    $("#login-form").validate({
        rules: {
            login: {
                required: true,
                minlength: 3
            },
            password: {
                required: true,
                minlength: 8,
                maxlength: 15
            }
        },
        messages: {
            login: "please enter your login",
            password: {
                required: "please provide a password",
                minlength: "password at least have 8 characters"
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
        submitHandler: signIn()
    });
});

function signIn() {
    $('#sign-in-button').click(function() {
        var login = $('#login-sign-in').val();
        var password = $('#password-sign-in').val();
        var data = {
            'login': login,
            'password': password
        };
        $.ajax({
            url: '/login', //the page containing python script
            dataType: "json",
            data: JSON.stringify(data),
            type: 'POST',
            success: function() {
                console.log('user created');
                window.location = '#'; // profile-s.html or profile-c.html
            },
            error: function() {
                console.log('error');
            }
        });
    });
}
