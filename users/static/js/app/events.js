$(function(){

var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

Vue.component('project',{
props:['project'],
template:'<div class="row border-top py-2"><h5 class="w-100 text-center">{{ project.name }}</h5></div>'
});

Vue.component('event',{
props:['event'],
template:'<div class="row border-top pl-5 pt-2">\
                    <div class="col-md-8"><h5 class="w-100 ">{{event.name}}</h5><p>{{event.description}}</p></div>\
                    <div class="col-md-4"><span class="oi oi-pencil p-2"></span><span class="oi oi-calendar p-2"></span><span class="oi oi-chat p-2"></span><span @click="selfdelete" class="oi oi-x p-2"></span></div>\
                </div>',
methods:{
selfdelete:function(){
var id = this.event.id;
var url = '/scheduler/events/'+id+'/'
this.$http.delete(url).then(response=>{this.$emit('deleted')})
}
},
   http: {
    root: '/',
    headers: {
     "X-CSRFToken": csrftoken
    }
  }
});



Vue.component('projectcol',{
props:[],
template:'<div id="project-col" class="col-md-3 d-none d-sm-none d-md-block border-right px-5">\
                <div class="row"><h3 class="w-100 text-center pt-5 pb-4">Projects</h3></div>\
                <project v-for="project in projects" :project="project" :key="project.id"></project>\
                <div class="row border-top py-2"><span class="mt-3 oi oi-plus w-100 text-center"></span></div>\
            </div>',
  data: function(){return {
  projects:[]
  }
  },
  method:{
  },
  mounted:function(){
  this.$http.get('/scheduler/projects/').then(response=>{this.projects= response.data; })
  }
});

Vue.component('eventcol',{
props:[],
template:'            <div id="event-col" class="col-md-9 col-sm-12 px-5">\
                <div class="row">\
                    <div class="col-sm-8"><h3 class="pt-5 pb-4 px-2">Events</h3></div>\
                    <div class="col-sm-4 pt-3"><span class="oi oi-plus mt-5 ml-4"></span></div>\
                </div>\
                <event v-for="event in events" :event="event" :key="event.id"></event>\
            </div>',
  data: function(){return {
  events:[]
  }
  },
  method:{
  },
  mounted:function(){
  this.$http.get('/scheduler/events/').then(response=>{this.events= response.data; })
  }
});




//var ev = new Vue({
//  el: '#event-col',
//  data: {
//  events:[]
//  },
//  method:{
//  },
//  mounted:function(){
//  this.$http.get('/scheduler/events/').then(response=>{console.log(response.data);this.events= response.data; })
//  },
//
//
//});

});
