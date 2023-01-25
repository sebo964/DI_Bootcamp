// 🌟 Exercise 1 : List Of People

// Instructions

// const people = ["Greg", "Mary", "Devon", "James"];


// Part I - Review About Arrays

// Write code to remove “Greg” from the people array.

// Write code to replace “James” to “Jason”.

// Write code to add your name to the end of the people array.

// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

// Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method

// Write code that gives the index of “Foo”. Why does it return -1 ?

// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?


// Part II - Loops

// Using a loop, iterate through the people array and console.log each person.

// Using a loop, iterate through the people array and exit the loop after you console.log “Jason” . 
// Hint: take a look at the break statement in the lesson.


const people = ["Greg", "Mary", "Devon", "James"];

console.log(people);

people.splice(0, 1); // remove Greg

console.log(people);

people.splice(2, 1,"Jason"); // replace james with jones 

console.log(people);

people.push("Sebastien"); // add sebastien

console.log(people);

console.log(people.indexOf("Mary")) // finds the index of mary

console.log(people.length);

let people2 = people.slice(1, people.length-1); // create a new array with all the people except Sebastien and Mary which are located at the start and end of the array. 

console.log(people2);

console.log(people.indexOf("foo"))  // foo is not in the array.

let lastitemindex = (people.length-1); // finds the index of the last item

let last = people[lastitemindex]; // take the content of the last item index and place in the variable. 

console.log(last);  // prints the content of the last item of the array. 

for (let i = 0; i < people.length; i++) {      /// lists all the names in the array line by line in the console log. 

    console.log(people[i]);

};



for (let i = 0; i < people.length; i++) {      /// lists all the names in the array line by line in the console log. 
    console.log(people[i]);  

   if (people[i].toLowerCase()==='jason') {
   
    break;}
}; // exits the loop once Jason is reached. 


