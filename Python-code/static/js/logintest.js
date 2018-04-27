$('#test').click(function() {
    var data = {
        "test_login": $('#login-sign-in').val(),
        "test_password": $('#password-sign-in').val()
    };
    $.ajax({
        url: '/test/iphone/request', //the page containing python script
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
        success: function(response) {
                var msg = response.status;
                alert(msg);
        },
        error: function() {
            console.log('error');
        }
    });
});