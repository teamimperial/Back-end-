/**
 * Created by Nazar on 22.12.2017.
 */

$('#save-button').click(function() {
    var hashes = window.location.href.slice(window.location.href.indexOf('!')).split("/");
    var data = {
        "link": hashes
    }
    $.ajax({
            url: '/apply', //the page containing python script
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(data),
            type: 'POST',
            success: function(response) {
                if (response.redirect=="false"){
                    var msg = response.message;
                    alert(msg);
                }
                if (response.redirect=="true"){
                    }
                var redirect_url = response.redirect_url
                window.location.href = redirect_url;
            },
            error: function() {
                console.log('error');
            }
        });
});

$('#confirm').click(function() {
    //input для id_apply (idStudent_Apply)
    var data = {"id_apply" : id_apply, "status" : 1};
    $.ajax({
        url: '/set_status',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
        success: function(response) {
            if(response.redirect=='true'){
                alert(response.message)
                window.location.href = response.redirect_url;
            }
            if(response.redirect=='false'){
                alert(response.message);
            }
        },
        error: function() {
            console.log('error');
        }
    })
});

$('#delete').click(function() {
    //input для id_apply (idStudent_Apply)
    var data = {"id_apply" : id_apply, "status" : 0};
    $.ajax({
        url: '/set_status',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        type: 'POST',
        success: function(response) {
            if(response.redirect=='true'){
                alert(response.message)
                window.location.href = response.redirect_url;
            }
            if(response.redirect=='false'){
                alert(response.message);
            }
        },
        error: function() {
            console.log('error');
        }
    })
});