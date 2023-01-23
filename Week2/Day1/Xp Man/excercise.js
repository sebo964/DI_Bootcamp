// Exercise 1: Your Favorite Food

// Instructions

// Store your favorite food into a variable.

// Store your favorite meal of the day into a variable (ie. breakfast, lunch or dinner)

// Console.log I eat <favorite food> at every <favorite meal>

// For example

// If your favorite food is "chocolate", 
// and your favorite meal of the day is "dinner", 
// you will console.log 
// I eat chocolate at every dinner

let favfood="mine";
let meal="dinner";
let sen= `I eat ${favfood} at every ${meal}`

console.log(sen)
 


// 🌟 Exercise 2 : Series

// Instructions

// Part I

// Using this array : const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

// Create a variable named myWatchedSeriesLength that is equal to the number of series in the myWatchedSeries array.

// Create a variable named myWatchedSeriesSentence, that is equal to a sentence describing the series you watched
// For example : black mirror, money heist, and the big bang theory

// Console.log a sentence using both of the variables created above
// For example : I watched 3 series : black mirror, money heist, and the big bang theory

const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

let myWatchedSeriesLength=myWatchedSeries.length;

console.log(myWatchedSeriesLength);

let myWatchedSeriesSentence = `I like to watch ${myWatchedSeries[0]}, ${myWatchedSeries[1]} and ${myWatchedSeries[2]}.`;

console.log(myWatchedSeriesSentence);


// Part II

// Change the series    “the big bang theory” to “friends”. Hint : You will need to use the index of “the big bang theory” series.
// Add, at the end of the array, the name of another series you watched.
// Add, at the beginning of the array, the name of your favorite series.
// Delete the series “black mirror”.
// Console.log the third letter of the series “money heist”.
// Finally, console.log the myWatchedSeries array, to see all the modifications you’ve made.

myWatchedSeries.splice(2,1,"friends");

console.log(myWatchedSeries);

myWatchedSeries.splice(3,0,"Superstore")

console.log(myWatchedSeries)

myWatchedSeries.splice(0,0,'The Office')

console.log(myWatchedSeries)

myWatchedSeries.splice(1,1)

console.log(myWatchedSeries)

let money=myWatchedSeries[1]

console.log(money.charAt(2))



// 🌟 Exercise 3 : The Temperature Converter

// Instructions

// Store a celsius temperature into a variable.

// Convert it to fahrenheit and console.log <temperature>°C is <temperature>°F.
// Hint : Should you create another variable to hold the temperature in fahrenheit? (ie. point 2)
// Hint: To convert a temperature from celsius to fahrenheit : Divide it by 5, then multiply it by 9, then add 32

let tempc=30

let tempf=((tempc/5)*9)+32

const tempsen=`${tempc}°C is ${tempf}°F`

console.log(tempsen)

// 🌟 Exercise 4 : Guess The Answers #1

// Instructions

// For each expression, predict what you think the output will be in a comment (//) without first running the command. 
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.



// For example

// console.log(2+3)
// // Prediction: It will output 5, because 2 and 3 are numbers
// // Actual: 5


// Using the code below:

//   let c;
//   let a = 34;
 //   let b = 21;

 //   console.log(a+b) //first expression
//     // Prediction:55
//     // Actual:55

 // a = 2;

 //console.log(a+b) //second expression
//     // Prediction:23 a has been reassigned value of 2 
//     // Actual:23 



// What will be the outcome of a + b in the first expression ?

// ANSWER  55 - number additions.  

// What will be the outcome of a + b in the second expression ?

// ANSWER 23 - a was reassigned value 2 

// What is the value of c?

//ANSWER -1 - c has not been given any value. 

// Analyse the code below, what will be the outcome?
// console.log(3 + 4 + '5');

// ASNWER 75 the number '5' was declared was string, 3 and 4 will be added as number and 5 will be concatened with the result of 3 plus 4. 


// Exercise 5 : Guess The Answers #2

// Instructions

// For each expression, predict what you think the output will be in a comment (//) without first running the command. 
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.



// For example

// typeof("potato")
// // Prediction: Vegetable
// // Actual: String


// What is the output of each of the expressions below?


// typeof(15)
// // Prediction: number - it is is number 
// // Actual: number 

// typeof(5.5)
// // Prediction:float - it is decimal number
// // Actual: number

// typeof(NaN)
// // Prediction:text - appears to be a text 
// // Actual:number 

// typeof("hello")
// // Prediction:text - the text is in ""
// // Actual: string 

// typeof(true)
// // Prediction: boolean - one of the 2 boolean value, true false. 
// // Actual: boolean 

// typeof(1 != 2)
// // Prediction: true
// // Actual:boolean - type of only describes the output not the actual output 

// "hamburger" + "s"
// // Prediction: hamburgers - text concatenation 
// // Actual: hamburgers 

// "hamburgers" - "s"
// // Prediction:invalid - operation if for numbers and text was declared. 
// // Actual:NaN 

// "1" + "3"
// // Prediction:13 - 1 and 3 are declared strings so the are concatenanted 
// // Actual:13

// "1" - "3"
// // Prediction: -2  - the operation - is for numbers only, the value 1 and 3 are converted to numbers and the mathematical operation is done. 
// // Actual:-2 

// "johnny" + 5
// // Prediction:johnny5
// // Actual:johnny5

// "johnny" - 5
// // Prediction:NaN - operator does not operate on a strng and a number
// // Actual:NaN

// 99 * "hello"
// // Prediction:NaN - * Operator does not work with string values. 
// // Actual:NAN 

// 1 != 1
// // Prediction:false - boolean computation is false 
// // Actual:false

// 1 == "1"
// // Prediction:true - 1 is greater or equal to 1 
// // Actual:true

// 1 === "1"
// // Prediction: false - strictly speaking the values are not the same as one is a string and one a number, hence false. 
// // Actual:false 


// Exercise 6 : Guess The Answers #3

// Instructions

// For each expression, predict what you think the output will be in a comment (//) without first running the command. 
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.



// What is the output of each of the expressions below?


// 5 + "34"
// // Prediction: 534
// // Actual:534 - concatenation of numbers. 

// 5 - "4"
// // Prediction:54
// // Actual:1

// 10 % 5
// // Prediction:0
// // Actual:0

// 5 % 10
// // Prediction:2
// // Actual:5

// "Java" + "Script"
// // Prediction:JavaScript
// // Actual:JavaScript

// " " + " "
// // Prediction: -- nothing blank 
// // Actual: -- nothing blank

// " " + 0
// // Prediction: 0
// // Actual: nothing

// true + true
// // Prediction: truetrue
// // Actual: nothing

// true + false
// // Prediction: 1 - true and false hold values of 1 and zero 
// // Actual: 1

// false + true
// // Prediction: 1 
// // Actual: 1 same as above

// false - true
// // Prediction: -1 the same as 0 minus 1 
// // Actual: -1 

// !true
// // Prediction: false operator return the oppposite of true 
// // Actual: false 

// 3 - 4
// // Prediction: -1 simople mathematical substraction. 
// // Actual: -1 

// "Bob" - "bill"
// // Prediction:Nan - string cannot be subtracted this is why it generates an error. 
// // Actual: NaN 



