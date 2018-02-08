$(function(){
var controller = {
'events':false,
'calendar':true,
'emergency':true,
'dependency':true
}
var tc = new Vue({
  el: '#tabControl',
  data: controller,
  methods:{
  tabchange: function(e){
    console.log(e.target.target);
    var key=e.target.target;
    for(var entry in controller){
    this[entry]=true;
    }
    this[key]=false;

  }
  }
});

var tp = new Vue({
el: '#tabpanel',
data: controller

});
});
