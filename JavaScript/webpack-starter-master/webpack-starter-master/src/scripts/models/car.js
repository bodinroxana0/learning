export class Car {
    constructor(id){
        this.id=id;
    }
}
// class Vehicle{
//     constructor(){
//         this.type='car';
//     }
//     start(){
//         return `Starting: ${this.type}`;
//     }
// }

// class Car extends Vehicle{
//     constructor(){
//         super();
//     }
//     start(){
//         return 'in Car start '+super.start();
//     }
// }
// let car=new Car();
// console.log(car.type);
// console.log(car.start());