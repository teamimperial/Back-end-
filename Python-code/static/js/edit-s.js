/**
 * Created by Antonina on 09.12.2017.
 */

/*var files; // змінна з файлами

$('input[type=file]').on('change', function(){
    files = this.files;
});
*/
$('#save-button').click(function() {
   /* event.stopPropagation();
    event.preventDefault();  // зупинка всього,що відбувається

    // Создадим данные формы и добавим в них данные файлов из files
    var file_data = new FormData();
    $.each( files, function( key, value ){
        file_data.append( key, value );
    });
*/
    var data = {
        "img": $('#profile-img').attr('src'),
        "first_name": $('#first-name').val(),
        "last_name": $('#last-name').val(),
        "city": $('#city').val(),
        "country": $('#country').val(),
        "date_of_birth": $('#date-of-birth').val(),
        "university": $('#university').val(),
        "time_of_studing": $('#time-of-studing').val(),
        "link": $('#link').val(),
        "bio": $('#bio').val(),
        "email": $('#email').val(),
        "new_password":  $('#new-password').val(),
        "old_password": $('#password').val(),
        "confirm_password": $('#confirm-new-password').val()
        /*"cv": file_date*/
    };
    $.ajax({
        url: '/student/update', //the page containing python script
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
        success: function(response) {
            if(response.redirect==='true'){
                alert(response.message);
                window.location.href = response.redirect_url;
            }
            if(response.redirect=='false'){
                alert(response.message);
            }
/*
            if( typeof respond.error === 'undefined' ){
                // Файли успішно завантажені
                // виводимо в консоль шлях до них
                var files_path = respond.files;
                var html = '';
                $.each( files_path, function( key, val ){ html += val +'<br>'; } )
                console.log(html)
            }
            else{
                console.log('SERVER RESPONSE ERROR: ' + respond.error );
            }*/
        },
        error: function() {
            console.log('AJAX error');
        }
    });
});