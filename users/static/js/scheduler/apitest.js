$(function(){
$('#submit').on("click", function(){
var url = $('#url').val();
var method= $('#method').val();
var content= $('#content').val();
if(content){
var datapack = JSON.parse(content);
}
else{
var datapack = '';
}
var csrftoken = $("[name=csrfmiddlewaretoken]").val();
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});

$.ajax({
type:method,
url:url,
data: datapack,
dataType: 'json',
error:function(e){console.log(e)},
success:function(e){console.log(e);},
});

})
})
