$('#send-review-s').click(function() {
    var data = {
        "student_login": document.getElementById('student_login').innerHTML,
        "review": $('#review').val()
    };
    $.ajax({
        url: '/comment/student', //the page containing python script
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
        success: function(response) {
            if (response.redirect=='true'){
                var msg = response.message;
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

$('#send-review-c').click(function() {
    var data = {
        "company_login": $('#company-login').innerHTML,
        "review": $('#review-c').val()
    };
    $.ajax({
        url: '/comment/course', //the page containing python script
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
        success: function(response) {
            if (response.redirect=='true'){
                var msg = response.message;
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

$('#send-review-course').click(function() {
    var data = {
        "course_id": document.getElementById('course_id').innerHTML,
        "review": $('#review').val()
    };
    $.ajax({
        url: '/comment/course', //the page containing python script
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
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