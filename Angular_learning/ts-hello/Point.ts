class Point
{
    //private x:number;
    //private y:number;
    constructor (private _x?:number,private _y?:number){
       // this.x=x;
       //  this.y=y;
    }
    draw(){
        console.log('X: ' + this.x+ ', Y: '+ this.y);
    }
    get x()
    {
        return this.x;
    }
    set x(value)
    {
        if(value<0)
            throw new Error('value cannot be less than 0');
        
        this.x=value;
    }
}

let point: Point=new Point (1,2);
//let x=point.getX();
let x=point.x;
point.x=10;
point.draw();