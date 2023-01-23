// let name='seb'
 //console.log(name);
 

// console.log('To be or not to be'.indexOf('To'));
// console.log('To be or not to be'.indexOf(' '));
// console.log('To be or not to be'.indexOf('o', 2));
// console.log('To be or not to be'.indexOf('be', 4));
// console.log('To be or not to be'.indexOf('to'));
// console.log('To be or not to be'.indexOf('B'));
// console.log('To be or not to be'.indexOf('', 9));

let pets=['cat','dog','fish','rabbit','cow'];
console.log(pets)
console.log(pets [1])
pets.splice(0,0,"horse")
pets.splice(4,1)
console.log(pets)


//exercise 1 
let address_number='12'
let address_street='royal road'
let country='mauritius'

let global_address= address_number + address_street+country
console.log(global_address)

console.log(`${address_number} ${address_street} ${country}`)

//Exercise 2 

let table=['first','second','three']

console.log(table)

//push (add at the end) pop  slice join shift unshift

console.log(table.toString());

table.splice(1,1,"sploice");

console.log(table);

table.splice(0,0,"foice");

console.log(table);

