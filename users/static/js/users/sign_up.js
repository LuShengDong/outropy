$(function(){
$('#submit').on("click", function(){
var username = $('#username').val();
var email = $('#email').val();
var passwd= $('#password').val();
var datapack = {'username': username, 'email': email, 'passwd': passwd};

var csrftoken = $("[name=csrfmiddlewaretoken]").val();
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});

$.ajax({
type:'POST',
url:"/sign_up/api",
data: datapack,
dataType: 'json',
error:function(e){alert(e.responseJSON.message);console.log(e)},
success:function(e){window.location = "/sign_in";},
});

})
})
