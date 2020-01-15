// import { Car } from "./models/car";

// let car=new Car(123);
// console.log(car.id);

//DOM and BOM
//window is the global object-work only if you don't have modules
// year1=1956;
// console.log(window.year1);
// console.log(innerHeight);

//executes once
// let timeoutId=setTimeout(function(){
//     console.log('1 second passed');
// },1000);

//if need to cancel
//clearTimeout(timeoutId);

let intervalId=setInterval(function(){
    console.log('1 second passed');
},1000);

//if need to cancel
clearInterval(intervalId);

//location object
console.log(document.location.href);//location.href);

let el=document.getElementById('first');
console.log(el);

let elClass=document.getElementsByClassName('p1');
console.log(elClass[1]);

let elTag=document.getElementsByTagName('p');
console.log(elTag);

//modify DOM element
el.textContent='new text here';
el.setAttribute('name','nameValue');
el.classList.add('myClassName');
el.style.color='blue';
console.log(el);

try{
    let car=null;
    throw new Error('my custom error');
}
catch(error)
{
    console.log('error: ', error);
}
finally{
    console.log('continuing');
}

//promise
let promise=new Promise(
    function(resolve,reject){
        setTimeout(resolve,100,'someValue');
    }
);
console.log(promise);