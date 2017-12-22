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
                if (response.redirect=="true"){
                    window.location.href = response.redirect_url;
                }if(response.redirect=="false"){
                    var msg = response.message;
                    alert(msg);
                }
            },
            error: function() {
                console.log('error');
            }
        });
});