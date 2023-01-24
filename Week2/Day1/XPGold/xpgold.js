// Exercise 1 : Favorite Color

// Instructions

// let sentence = ["my","favorite","color","is","blue"];
// Write some simple Javascript code that will join all the items in the array above, and console.log the result.

let sentence = ["my","favorite","color","is","blue"];

let sen2=`${sentence[0]} ${sentence[1]} ${sentence[2]}${sentence[3]} ${sentence[4]}`;


console.log(sen2);

// Exercise 2 : Mixup

// Instructions

// Create 2 variables. The values should be strings. For example:
// let str1 = "mix";
// let str2 = "pod";

let str1 = "mix";
let str2 = "pod";

// 2. Slice out and swap the first 2 characters of the two strings from part 1.

let astr1= Array.from(str1)
let astr2= Array.from(str2)

astr1.splice(0,2,"q","w")
astr2.splice(0,2,"q","w")
console.log(astr1)
console.log(astr2) 
    

// 3. Create a third variable where the value is the concatenation of the two strings from the part 1 (separated by a space).

let full=str1+str2



// 4. Finally console.log the new concatenated string.

console.log(full)


// Some Examples

// let str1 = "mix";
// let str2 = "pod";
// let newWord should be equal to 'pox mid'

// let firstWord = "Hello";
// let secondWord = "World";
// let thirdWord should be equal to 'Wollo Herld'


// Exercise 3 : Calculator

// Instructions

// Make a Calculator. Follow the instructions:

// Prompt the user for the first number.
// Store the first number in a variable called num1. 
// Hint : console.log the type of the variable num1. What should you do to convert it to a number ?
// Prompt the user for the second number.
// Store the second number in a variable called num2.
// Create an Alert where the value is the SUM of num1 and num2.
// BONUS: Make a program that can subtract, multiply, and also divide!
