
if(true){
    var carId=100;
    // var carId=100;
}
console.log(carId);

//REST param
function sendCars(day,...carIds){
    carIds.forEach(id=> console.log(id));
}

sendCars('Monday',1,2,3);

//destructuring arrays
let carIds=[1,2,5];
// let [car1,car2,car3]=carIds;
let car1,remainingCars;
[car1,... remainingCars]=carIds;

console.log(car1);
console.log(remainingCars);

//destructuring objects
let car ={
    id:5000,
    style:'convertible'
};
let {id,style}=car;
console.log(id,style);

//spread syntax
function startCars(car1,car2)
{
    console.log(car1,car2);
}
let carCodes='abc';
startCars(...carCodes);

//converting, ! start with a number 
let foo=1;
foo.toString();
console.log(Number.parseInt('55A'));
console.log(Number.parseFloat('55.99'));