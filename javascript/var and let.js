var -> 1. function scope 2. hoisted

let -> 1. ES6 2. block scope

example:

let x = function(){
	if (true){
		var v = 2;
		let l = 1;
	}
	console.log(v);
	console.log(l);
}

result: 2
		error: l is not defined  