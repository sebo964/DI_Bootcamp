// Instructions

// Exercise 1:

// Using this array :

// const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
// Remove Banana from the array.
// Sort the array in alphabetical order.
// Add “Kiwi” to the end of the array.
// Remove “Apples” from the array. Don’t use the same method as in part 1.
// Sort the array in reverse order. (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])
// At the end you should see this outcome:
// ["Kiwi", "Oranges", "Blueberries"]
// Exercise 2:

// Using this array :

// const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
// Access and then console.log “Oranges”.
// Bonus: If you would like more array exercises take a look at the link below.

// Array Exercises

//Exercise 1

const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

console.log(fruits);

fruits.splice(0,1);

console.log(fruits);

fruits.sort();

console.log(fruits);

fruits.push("kiwi");

console.log(fruits);

fruits.reverse();

console.log(fruits);

fruits.pop();

console.log(fruits);

//Excersice 2 

const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

let fruits_1=moreFruits[1];

let fruits_2=fruits_1[1];

console.log(fruits_2);