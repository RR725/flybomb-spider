


var nspider=require('nspider22')

var nsp=new nspider({name:'baidu'});
nsp.onHtml('.s_tab',function(ele){
   console.log(ele);
})

nsp.visit("http://www.baidu.com");

