var palindrome = (str) =>{
	str = str.replace(/\W/g, '').toLowerCase();
	return str === str.split('').reverse().join('');
}
console.log(palindrome("sasasda"));
console.log(palindrome('A but tuba'));