$(function(){
$('#submit').on("click", function(){
var username = $('#username').val();
var passwd= $('#password').val();
var datapack = {'username': username, 'passwd': passwd};

var csrftoken = $("[name=csrfmiddlewaretoken]").val();
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});

$.ajax({
type:'POST',
url:"/sign_in/api",
data: datapack,
dataType: 'json',
error:function(e){alert(e.responseJSON.message);console.log(e)},
success:function(e){window.location = "/";},
});

})
})
