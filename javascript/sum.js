var sum = (num1, num2) =>{
	if (num2 !== undefined){
		return num1 + num2
	}
	return (num2) => num1 + num2;
	}
console.log(sum(1)(2));
console.log(sum(1, 2));