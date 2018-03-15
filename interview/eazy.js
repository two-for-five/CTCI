function reverseString(str){
	// 1 javascript build-in functions
	//return str.split('').reverse().join('');

	// 2 for loop
	// reversed = ''
	// for (let char of str){
	// 	reversed = char + reversed
	// }
	// return reversed;

	// 3 forEach alternatives
	// let reversed = ''
	// str.split('').forEach( char => reversed = char + reversed);
	// return reversed;

	// 4 reduce
	return str.split('').reduce((revString, char) => char + revString, '');
}
// console.log(reverseString('hello'));

function isPalindrome(str){
	length = str.length;
	for(let i = 0; i < length/2; i++){
		if (str[i] != str[length - i - 1]){
			return false
		}
	}
	return true;
}
//console.log(isPalindrome('racecar'));

function capitalizeLetters(str){
	//return str.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');

	// replace and regular express
	return str.replace(/\b[a-z]/gi, (char) => char.toUpperCase());
}
//console.log(capitalizeLetters("i like javascript"));

function maxCharacter(str){
	var dictionary = {}
	var maxChar = '';
	var maxNum = 0;
	for (let char of str){
		if (char in dictionary){
			dictionary[char] += 1
		}
		else{
			dictionary[char] = 1
		}
	}
	for (let char in dictionary){
		if (dictionary[char] > maxNum){
			maxChar = char;
			maxNum = dictionary[char];
		}
	}
	return maxChar;
}
console.log(maxCharacter("11223333"))
