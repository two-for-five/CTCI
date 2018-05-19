var a = 1;
var b = [1,2,4];
var c = b.map((num) =>{
  console.log(this.a);
}.bind(this))
