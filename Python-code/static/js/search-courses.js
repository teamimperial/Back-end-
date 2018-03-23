/**
 * Created by Nazar on 22.12.2017.
 */

$('#save-button').click(function() {
    var search = $('#search').val();
    var redirect = '/praxis/search/' + search;
    window.location.href = redirect;
});