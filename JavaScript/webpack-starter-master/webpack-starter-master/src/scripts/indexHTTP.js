//XHR

//  let xhttp=new XMLHttpRequest();
//  xhttp.onreadystatechange=function(){
//     if(this.readyState==4 && this.status==200)
//     {
//         console.log(this.responseText);
//     }
//  };
//  xhttp.open("GET","http://5e20256ee31c6e0014c6031d.mockapi.io/api/v1/users",true);
//  xhttp.send();

//jquery
import $ from 'jquery';

let promise=$.get("http://5e20256ee31c6e0014c6031d.mockapi.io/api/v1/users");
promise.then(
    data=> console.log('success: ', data),
    error=> console.log('error: ', error)
);

//POST
let user={
    id:2,
    items:"moto",
    count:2
};
let promises=$.post("http://5e20256ee31c6e0014c6031d.mockapi.io/api/v1/users",user);
promises.then(
    data=> console.log('success: ', data),
    error=> console.log('error: ', error)
);