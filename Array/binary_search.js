// Given a sorted array of integers, return the index of the given key. Return -1 if not found.

function binary_search(array, key){
	let low = 0;
	let high = array.length - 1;
	while (low <= high){
		let middle = parseInt((low + high)/2);
		if (array[middle] === key){
			return middle;
		}
		else if (array[middle] > key ){
			high = middle - 1;
		}
		else{
			low = middle + 1;
		}
	}
	return -1;
}

console.log(binary_search([0,1,2,3,4,5,6], 0));
console.log(binary_search([0,1,2,3,4,5,6], 1));
console.log(binary_search([0,1,2,3,4,5,6], 2));
console.log(binary_search([0,1,2,3,4,5,6], 3));
console.log(binary_search([0,1,2,3,4,5,6], 4));
console.log(binary_search([0,1,2,3,4,5,6], 5));
console.log(binary_search([0,1,2,3,4,5,6], 6));

