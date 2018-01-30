// Simple Example
let myPromise = new Promise((resolve, reject) =>{
	let isClean = false;
	if (isClean){
		resolve('Clean');
	}
	else{
		reject("not Clean");
	}
})

// Complicated example
myPromise.then((fromResolve)=>{
	console.log(fromResolve)
}).catch((fromReject) => {
	console.log(fromReject);
})

let cleanRoom = function() {
  return new Promise(function(resolve, reject) {
    resolve('Cleaned The Room');
  });
};

let removeGarbage = function(message) {
  return new Promise(function(resolve, reject) {
    resolve(message + ' remove Garbage');
  });
};

let winIcecream = function(message) {
  return new Promise(function(resolve, reject) {
    resolve( message + ' won Icecream');
  });
};

cleanRoom().then(function(result){
	return removeGarbage(result);
}).then(function(result){
	return winIcecream(result);
}).then(function(result){
	console.log('finished ' + result);
})

// Race and All
Promise.all([cleanRoom(), removeGarbage(), winIcecream()]).then(() =>{
	console.log("ALl Done");
})
Promise.race([cleanRoom(), removeGarbage(), winIcecream()]).then(() =>{
	console.log("One of them is  Done");
})
