// let year=1967;
// console.log(++year);
// console.log(year++);
// console.log(year);
// let anotherYear="1967";
// console.log(typeof(+anotherYear));
// console.log(-anotherYear);

let userSettings=null;//{name:'Joe'};
let defaultSettings={name:'Default'};
console.log(userSettings || defaultSettings);
console.log(5>44 ? 'yes' : 'no');

let var1=5;
var1<<=1; //*2
console.log(var1); 
var1>>=2; // /2 /2
console.log(var1); 

//apply and call
//will not make a copy, just call an existing one and changing this
let o={
    carId:123,
    getId:function(prefix='id:'){
        return prefix + this.carId;
    }
};

console.log(o.getId());
let newCar={carId:456};
console.log(o.getId.call(newCar));//pass the new context

//in apply we can pass arguments
console.log(o.getId.apply(newCar,['ID: ']));

//bind-copy of the function
let newFn=o.getId.bind(newCar);
console.log(newFn());

//arrow fct
let getId=(prefix,suffix)=>prefix + 123 + suffix;
console.log(getId('ID: ','!'));

let get=prefix=>{
    return prefix+123;
};

let getSimple=()=>123;
let getS= _ => 123;
console.log(get('ID: '));