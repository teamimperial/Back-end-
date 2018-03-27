$('#comment-student').click(function() {
    var student_login = document.getElementById('student_login').innerHTML;
    var review = $('#review').val();
    var data = {
        "student_login": student_login,
        "review": review
    };
    $.ajax({
        url: '/comment/student', //the page containing python script
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
        success: function(response) {
            if (response.redirect == 'true'){
                window.location.href = response.redirect_url;
            }
            if (response.redirect == 'false'){
                alert(response.message)
            }
        },
        error: function() {
            console.log('error');
        }
    });
});