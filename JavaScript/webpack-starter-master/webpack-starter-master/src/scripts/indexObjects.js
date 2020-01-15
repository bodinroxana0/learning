//objects and arrays

//class with a property and a property-functiomn
function Car(id){
    this.carId=id; 
    this.start=function(){
        console.log('start: '+this.carId);
    };
}

/* a simply constructor
function Car(){
    console.log(this);
}
 */
let car=new Car(123);
car.start();

function House(id){
    this.houseId=id;
}

House.prototype.start=function(){
    console.log('start: ' + this.houseId);
};

let house=new House(1);
house.start();

//expanding objects=override
String.prototype.hello=function(){
    return this.toString()+' hello';
};
console.log('foo'.hello());

//JSON
let carJSON={
    id:123,
    style:'convertible'
};
console.log(JSON.stringify(carJSON));

//parse JSON
let jsonIn=
`
[
    {"carId":123},
    {"carId":234}
]
`;
let carIds=JSON.parse(jsonIn);
carIds.forEach(element => console.log(element));