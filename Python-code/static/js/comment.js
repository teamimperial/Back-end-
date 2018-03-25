$('#comment-student').click(function() {
    var name_student = $('#name_student').val();
    var comment = $('#comment').val();
    var data = {
        "name_student": name_student,
        "comment": comment
    };
    $.ajax({
        url: '/comment_about_student', //the page containing python script
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
        success: function(response) {
            if (response.redirect == 'true'){
                window.location.href = response.redirect_url;
            }
        },
        error: function() {
            console.log('error');
        }
    });
});