export class Point
{
    constructor (private _x?:number,private _y?:number){
    }
    draw(){
        console.log('X: ' + this.x+ ', Y: '+ this.y);
    }
}